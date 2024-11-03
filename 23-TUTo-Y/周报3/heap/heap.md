- [内存管理器(ptmalloc)的学习](#内存管理器ptmalloc的学习)
    - [chunk的具体实现](#chunk的具体实现)
    - [堆空闲管理结构(bins)](#堆空闲管理结构bins)
        - [fast bin](#fast-bin)
            - [fastbin的安全机制](#fastbin的安全机制)
        - [small bin](#small-bin)
        - [large bin](#large-bin)
        - [unsorted bin](#unsorted-bin)
        - [tcache bin( \>=glibc 2.26 )](#tcache-bin-glibc-226-)
        - [top chunk](#top-chunk)
        - [last remainder](#last-remainder)
    - [漏洞](#漏洞)
        - [Chunk Extend and Overlapping](#chunk-extend-and-overlapping)
        - [unlink](#unlink)
        - [Fastbin Attack](#fastbin-attack)
            - [Fastbin Double Free](#fastbin-double-free)
            - [House Of Spirit](#house-of-spirit)
            - [Alloc to Stack和Arbitrary Alloc](#alloc-to-stack和arbitrary-alloc)
        - [unsorted bin attack(在glibc-2.28及其以后变得难以利用)](#unsorted-bin-attack在glibc-228及其以后变得难以利用)
        - [Large Bin Attack](#large-bin-attack)
        - [tcache bin](#tcache-bin)
            - [tcache poisoning](#tcache-poisoning)
            - [tcache dup](#tcache-dup)
    - [other](#other)
        - [通过`main_arena`地址获取`glibc`基地址的偏移](#通过main_arena地址获取glibc基地址的偏移)
    - [struct malloc\_state (glibc-2.35)](#struct-malloc_state-glibc-235)
    - [\_\_libc\_malloc (glibc-2.35)](#__libc_malloc-glibc-235)
    - [\_\_libc\_free (glibc-2.35)](#__libc_free-glibc-235)
    - [\_int\_malloc (glibc-2.35)](#_int_malloc-glibc-235)

# 内存管理器(ptmalloc)的学习

## chunk的具体实现

```C
# define INTERNAL_SIZE_T size_t
struct malloc_chunk {

    INTERNAL_SIZE_T      mchunk_prev_size;    // 如果前面一个物理相邻的chunk是空闲的, 则表示其大小, 否则用于储存前一个chunk的数据
    INTERNAL_SIZE_T      mchunk_size;         // 当前chunk的大小, 低三位作为flag, 意义如下:
    /*
        A : 倒数第三位表示当前chunk是否属于主线程:1表示不属于主线程, 0表示属于主线程
        M : 倒数第二位表示当前chunk是从mmap(1)[多线程]分配的，还是从brk(0)[子线程]分配的
        P : 最低为表示前一个chunk是否在使用中, 1表示在使用, 0表示是空闲的
            通常堆中的第一个chunk的P位是1, 以便于防止访问前面的非法内存
    */

    /*
        1.用户使用的内存从这里开始分配
        3.只有在free之后, 以下数据才有效
    */
    struct malloc_chunk* fd;            // 当chunk空闲时才有意义,记录后一个空闲chunk的地址
    struct malloc_chunk* bk;            // 同上,记录前一个空闲chunk的地址

    /* 仅用于largebin */
    struct malloc_chunk* fd_nextsize;   // 指向比当前chunk大的第一个空闲chunk
    struct malloc_chunk* bk_nextsize;   // 指向比当前chunk小的第一个空闲chunk
};
```

`chunk`的大小必须是`2 * SIZE_SZ`的整数倍

- __32位下__:`SIZE_SZ = 4`, 因此堆大小为`0x8`的整数倍, 最小堆块为`0x10`
- __64位下__:`SIZE_SZ = 8`, 因此堆大小为`0x10`的整数倍, 最小堆块为`0x20`

## 堆空闲管理结构(bins)

每类`bin`的内部会有多个互不相关的链表来保存 __不同大小__ 的`chunk`
其中，对于`small bin``large bin``unsorted bin`, ptmalloc将其维护在`malloc_state`结构的同一个数组中:

```C
#define NBINS 128
mchunkptr bins[NBINS * 2 - 2];
```

每个双向链表需要占用 __两个索引__

- 第`0`个索引未被使用
- 第`1`个索引存放`unsorted bin`
- 第`2 ~ 63`个索引存放`small bin`, 因此`small bin`一共有`62`条双向链表
- 剩下的索引存放`large bin`, 因此`large bin`一共有`63`条双向链表

### fast bin

32位下存放`0x10 ~ 0x40`字节的堆块
64位下存放`0x20 ~ 0x80`字节的堆块
`fast bin`按单链表结构, `fd`指向下一堆块, 采用`LIFO`机制
防止释放时对`fast bin`合并, 下一堆块的p标志位为`1`

#### fastbin的安全机制

- 在glibc-2.32版本中，对`fastbin`的`fd`指针进行了加密，具体加密过程如下代码

```C
// 使用fd的地址作为密钥，加密fd的值
// ((((size_t) &ptr) >> 12) ^ ((size_t) ptr)))
#define PROTECT_PTR(pos, ptr) \
  ((__typeof (ptr)) ((((size_t) pos) >> 12) ^ ((size_t) ptr)))
#define REVEAL_PTR(ptr)  PROTECT_PTR (&ptr, ptr)
```

- `_int_free` 会检测 `fastbin` 的 `double free`，但是仅验证了 `main_arena` 直接指向的块，因此，我们不能连续释放两次，需要有间隔的`fastbin`
- 对于即将从fastbin中取出的chunk，会检查其size大小是否符合该bin上的大小

### small bin

双向链表, 采用FIFO策略
一共有`62`条双向链表

### large bin

双向链表, 采用FIFO策略
`large bins`中一共包括`63`个`bin`, 每个`bin`中的`chunk`的大小不一致, 处于一定区间范围内

### unsorted bin

双向链表, 采用FIFO策略
`free`的`chunk`大小如果大于`0x80`(64位下), 并且不与`top chunk`相连, 则会放到`unsorted bin`上
当一个`chunk`被分割后, 如果剩下的部分大于`MINSIZE`, 也会被放到`unsorted bin`中

### tcache bin( >=glibc 2.26 )

`tcache`是一个线程特定的数据结构, 每个线程都有自己的`tcache`, 它包含了一组`tcache bin`
使用`export GLIBC_TUNABLES=glibc.malloc.tcache_count=0`禁用`tcache`
在 `glibc 2.32` 版本中，引入了对 `tcache bin` 中 `chunk` 的 `next` 指针的加密，加密过程如[fastbin的安全机制](#fastbin的安全机制)
注意，`tcache bin` 中 `chunk` 的 `next` 指向 `mem` 

- `tcache`的两个重要的结构体如下:

```C
# define TCACHE_MAX_BINS 64
// 链接空闲的chunk结构体
typedef struct tcache_entry
{
    // next指向下一个具有相同大小的chunk
    // 与fast bin不同的是, chunk的fd指向的是下一个chunk的data部分
    struct tcache_entry *next;
    // 防止double free
    uintptr_t key;
} tcache_entry;

// 每个线程都会有一个tcache_perthread_struct用于管理tcache链表
// 这个结构体位于heap段的起始位置
typedef struct tcache_perthread_struct
{
    // counts记录了tcache_entry链上空闲chunk的数量
    // 每条tcache_entry链最多可以有7个chunk
    char counts[TCACHE_MAX_BINS];
    
    // 用单向链表的方式链接了相同大小的处于空闲状态的chunk
    tcache_entry *entries[TCACHE_MAX_BINS];
} tcache_perthread_struct;
```

1. 申请的内存块符合 fastbin 大小时并且在 fastbin 内找到可用的空闲块时，会把该 fastbin 链上的其他内存块放入 tcache 中。
2. 其次，申请的内存块符合 smallbin 大小时并且在 smallbin 内找到可用的空闲块时，会把该 smallbin 链上的其他内存块放入 tcache 中。
3. 当在 unsorted bin 链上循环处理时，当找到大小合适的链时，并不直接返回，而是先放到 tcache 中，继续处理。
4. tcache 取出：在内存申请的开始部分，首先会判断申请大小块，在 tcache 是否存在，如果存在就直接从 tcache 中摘取，否则再使用_int_malloc 分配。
5. 在循环处理 unsorted bin 内存块时，如果达到放入 unsorted bin 块最大数量，会立即返回。默认是 0，即不存在上限。
6. 在循环处理 unsorted bin 内存块后，如果之前曾放入过 tcache 块，则会取出一个并返回。

### top chunk

`prev_inuse`比特位始终为`1`

### last remainder

堆块切割后, 剩下的小于`MINSIZE`的部分

## 漏洞

### Chunk Extend and Overlapping

通过修改chunk的size和prev_size后通过释放和申请堆块，使得后面申请的堆块可以覆盖其他堆块

### unlink

```C
static void
unlink_chunk (mstate av, mchunkptr p)
{
    // 检查当前块的大小是否等于下一个块的 prev_size 字段
    if (chunksize (p) != prev_size (next_chunk (p)))
        malloc_printerr ("corrupted size vs. prev_size");

    // 获取当前块的前向指针和后向指针
    mchunkptr fd = p->fd;
    mchunkptr bk = p->bk;

    // 检查前向指针的后向指针是否指向当前块，以及后向指针的前向指针是否指向当前块
    if (__builtin_expect (fd->bk != p || bk->fd != p, 0))
        malloc_printerr ("corrupted double-linked list");

    // 从链表中移除，将前向指针的后向指针设置为后向指针，将后向指针的前向指针设置为前向指针
    fd->bk = bk;
    bk->fd = fd;
    // 如果当前块的大小不在 smallbin 的范围内，并且当前块的 fd_nextsize 字段不为 NULL
    // 那么需要处理 nextsize 链表
    if (!in_smallbin_range (chunksize_nomask (p)) && p->fd_nextsize != NULL)
    {
        // 检查 nextsize 链表的完整性
        if (p->fd_nextsize->bk_nextsize != p
              || p->bk_nextsize->fd_nextsize != p)
            malloc_printerr ("corrupted double-linked list (not small)");

        // 如果前向指针的 fd_nextsize 字段为 NULL
        if (fd->fd_nextsize == NULL)
        {
            // 如果当前块的 fd_nextsize 字段指向自己
            // 那么将前向指针的 fd_nextsize 和 bk_nextsize 字段都设置为前向指针自己
            if (p->fd_nextsize == p)
                fd->fd_nextsize = fd->bk_nextsize = fd;
            else
            {
                // 否则，将前向指针的 fd_nextsize 和 bk_nextsize 字段设置为当前块的 fd_nextsize 和 bk_nextsize 字段
                // 并将当前块的 fd_nextsize 和 bk_nextsize 字段的 bk_nextsize 和 fd_nextsize 字段设置为前向指针
                fd->fd_nextsize = p->fd_nextsize;
                fd->bk_nextsize = p->bk_nextsize;
                p->fd_nextsize->bk_nextsize = fd;
                p->bk_nextsize->fd_nextsize = fd;
            }
        }
        else
        {
            // 如果前向指针的 fd_nextsize 字段不为 NULL
            // 那么将当前块的 fd_nextsize 和 bk_nextsize 字段的 bk_nextsize 和 fd_nextsize 字段设置为前向指针的 fd_nextsize 字段
            p->fd_nextsize->bk_nextsize = p->bk_nextsize;
            p->bk_nextsize->fd_nextsize = p->fd_nextsize;
        }
    }
}
```

利用过程:

- 有一个指向上一个`fake chunk`的用户指针`ptr`
- 设置当前`chunk`的`p`标准位为`0`和`prev_size`
- 设置上一个`fake chunk`的`fd = ptr - 0x18`, `bk = ptr - 0x10`和`size`
- `free`当前`chunk`，即可使`ptr`指向`ptr - 0x18`

### Fastbin Attack

#### Fastbin Double Free

> 多次释放同一个`chunk`到`fastbin`，由于保护的存在，不能连续释放同一个`chunk`到`fastbin`，可以在之间隔一个`chunk`

比如:释放`chunk1`，释放`chunk2`，释放`chunk1`，那么此时fastbin如下:

- `main_arena`->`fastbinsY`→`chunk1`→`chunk2`→`chunk1`→`chunk2`→...

此时释放申请一个`chunk`后修改`chunk1`的`fd`指向`data`，然后再申请两次`chunk`后，第三次申请`chunk`即可获取`data`
__注意`data`的`size`必须满足当前`fastbin`的大小__
具体保护请见[fastbin的安全机制](#fastbin的安全机制)

#### House Of Spirit

House Of Spirit指在目标位置伪造chunk，释放后重新申请然后控制该区域，有点像`Chunk Extend and Overlapping`
伪造`fake chunk`时需要注意:

- `fake chunk` 的 `ISMMAP` 位不能为 `1`
- `fake chunk` 地址需要对齐
- `fake chunk` 的 `size` 大小需要满足对应的 `fastbin` 的需求
- `fake chunk` 的 `next chunk` 大小不能小于 `2 * SIZE_SZ`

#### Alloc to Stack和Arbitrary Alloc

劫持 `fastbin` 链表中 `chunk` 的 `fd` 指针，把 `fd` 指针指向我们想要分配的地方

### unsorted bin attack(在glibc-2.28及其以后变得难以利用)

```C
victim = unsorted_chunks (av)->bk;
bck = victim->bk;   //  bck = unsorted_chunks (av)->bk-bk
/* remove from unsorted list */
unsorted_chunks (av)->bk = bck;
bck->fd = unsorted_chunks (av);
```

如果我们可以控制释放后`chunk`的`bk`指针指向我们想要的修改的数据的地址，申请空间后即可将该数据的值设置为`main_arena`中的地址

### Large Bin Attack

glibc 从 2.26 版本开始引入了对 `large bin attack` 的防护

### tcache bin

#### tcache poisoning

修改 `tcache bin` 的 `next` 指针，使得 `malloc` 到任何地址
需要注意:

- 地址对齐
- `next`指针指向的是`mem`，而不是`chunk`, 可以使用`chunk2mem`进行转换
- 注意在`glibc 2.32`引入了对`next`指针的加密, 同[fastbin的安全机制](#fastbin的安全机制)
- `tcache bin`在取出`chunk`时会使用`count`检查对应`tcache bin`链上是否有`chunk`

如下:

```C
#include <stdio.h>
#include <stdlib.h>
// 加密
#define PROTECT_PTR(pos, ptr) \
  ((__typeof (ptr)) ((((size_t) pos) >> 12) ^ ((size_t) ptr)))
int main()
{
        size_t fake_chunk;
        size_t *a = malloc(0x80);   // 将a指针指向fake_chunk
        size_t *b = malloc(0x80);   // 用于tcache bin中count的计数
        free(b);                    // 先将b指针放入tcache bin中使得count计数为1
        free(a);
        *a = PROTECT_PTR(a, &fake_chunk); // 将fake_chunk的地址加密后存入a[0]中
        // tcache -> a -> fake_chunk
        printf("%p\n", &fake_chunk);
        printf("%p\n", malloc(0x80));   // 获取a
        printf("%p\n", malloc(0x80));   // 获取fake_chunk

        return 0;
}
```

#### tcache dup

可以通过double free申请两次或多次同一个堆块

## other

### 通过`main_arena`地址获取`glibc`基地址的偏移

通过`ida`找到`malloc_trim`函数，有一段`mstate ar_ptr = &main_arena;`可以获取`main_arena`地址

```C
int
__malloc_trim (size_t s)
{
    int result = 0;

    if (__malloc_initialized < 0)
        ptmalloc_init ();

    mstate ar_ptr = &main_arena;
    do
    {
        __libc_lock_lock (ar_ptr->mutex);
        result |= mtrim (ar_ptr, s);
        __libc_lock_unlock (ar_ptr->mutex);

        ar_ptr = ar_ptr->next;
    }
    while (ar_ptr != &main_arena);

    return result;
}
```

## struct malloc_state (glibc-2.35)

```C
# define INTERNAL_SIZE_T size_t
struct malloc_state
{
    // 用于序列化访问的互斥锁(64位下40字节，32位下24字节)
    __libc_lock_define (, mutex);

    // 标志位（以前在 max_fast 中）
    int flags;

    // 如果 fastbin 包含最近插入的空闲块，则设置此字段。注意，这是一个布尔值，但并非所有目标都支持对布尔值的原子操作。
    int have_fastchunks;

    // fast bins
    mfastbinptr fastbinsY[NFASTBINS];

    // top chunk
    mchunkptr top;

    // 最近一次小请求分割的剩余部分
    mchunkptr last_remainder;

    // bins
    mchunkptr bins[NBINS * 2 - 2];

    // bins 的位图
    unsigned int binmap[BINMAPSIZE];

    // 下一个malloc_state
    struct malloc_state *next;

    // 用于空闲 arenas 的链表。访问此字段的操作由 arena.c 中的 free_list_lock 进行序列化。
    struct malloc_state *next_free;

    // 附加到此 arena 的线程数。如果 arena 在空闲列表中，则为 0。访问此字段的操作由 arena.c 中的 free_list_lock 进行序列化。
    INTERNAL_SIZE_T attached_threads;

    // 在此 arena 中从系统分配的内存
    INTERNAL_SIZE_T system_mem;
    // 此 arena 中从系统分配的内存的最大值
    INTERNAL_SIZE_T max_system_mem;
};

typedef struct malloc_state *mstate;
```

## __libc_malloc (glibc-2.35)

```C
void *
__libc_malloc(size_t bytes)
{
    mstate ar_ptr;  // 存储当前 arena 的状态
    void *victim;   // 存储分配的内存块的指针

    _Static_assert(PTRDIFF_MAX <= SIZE_MAX / 2,
                   "PTRDIFF_MAX is not more than half of SIZE_MAX");

    // 初始化malloc
    if (!__malloc_initialized)
        ptmalloc_init();
#if USE_TCACHE
    // 如果启用了 tcache（线程缓存），那么尝试从 tcache 中分配内存
    size_t tbytes;
    // 将请求的字节数转换为实际需要分配的字节数
    if (!checked_request2size(bytes, &tbytes))
    {
        __set_errno(ENOMEM);
        return NULL;
    }
    // 计算 tbytes 对应的 tcache 索引
    size_t tc_idx = csize2tidx(tbytes);

    // 如果 tcache 还没有初始化，那么就初始化它
    MAYBE_INIT_TCACHE();

    DIAG_PUSH_NEEDS_COMMENT;
    // 检查 tcache 是否有足够的空间来满足这个请求
    if (tc_idx < mp_.tcache_bins && tcache && tcache->counts[tc_idx] > 0)
    {
        // 从 tcache 中获取一个内存块
        victim = tcache_get(tc_idx);
        // 返回这个内存块的指针
        return tag_new_usable(victim);
    }
    DIAG_POP_NEEDS_COMMENT;
#endif

    // 如果是单线程，那么直接从 main_arena 中分配内存
    if (SINGLE_THREAD_P)
    {
        victim = tag_new_usable(_int_malloc(&main_arena, bytes));
        assert(!victim || chunk_is_mmapped(mem2chunk(victim)) ||
               &main_arena == arena_for_chunk(mem2chunk(victim)));
        return victim;
    }

    // 获取一个 arena
    arena_get(ar_ptr, bytes);

    // 从获取的 arena 中分配内存
    victim = _int_malloc(ar_ptr, bytes);
    // 如果分配失败，并且我们找到了一个可用的 arena，那么尝试从其他 arena 中重新分配
    if (!victim && ar_ptr != NULL)
    {
        LIBC_PROBE(memory_malloc_retry, 1, bytes);
        ar_ptr = arena_get_retry(ar_ptr, bytes);
        victim = _int_malloc(ar_ptr, bytes);
    }

    // 解锁 arena 的互斥锁
    if (ar_ptr != NULL)
        __libc_lock_unlock(ar_ptr->mutex);

    // 返回分配的内存块的指针
    victim = tag_new_usable(victim);

    assert(!victim || chunk_is_mmapped(mem2chunk(victim)) ||
           ar_ptr == arena_for_chunk(mem2chunk(victim)));
    return victim;
}
```

## __libc_free (glibc-2.35)

```C
void __libc_free(void *mem)
{
    mstate ar_ptr;  // 存储当前 arena 的状态
    mchunkptr p;    // 存储对应于 mem 的 chunk

    // free的mem不能为NULL
    if (mem == 0)
        return;

    if (__glibc_unlikely(mtag_enabled))
        *(volatile char *)mem;

    // 保存当前的 errno
    int err = errno;

    // 将 mem 转换为对应的 chunk
    p = mem2chunk(mem);

    // 如果 chunk 是通过 mmap 分配的，那么释放这个 chunk
    if (chunk_is_mmapped(p))
    {
        // 检查是否需要调整动态 brk/mmap 阈值
        // 如果 chunk 的大小大于当前的 mmap 阈值，并且小于或等于最大的 mmap 阈值，那么就调整阈值
        if (!mp_.no_dyn_threshold && chunksize_nomask(p) > mp_.mmap_threshold && chunksize_nomask(p) <= DEFAULT_MMAP_THRESHOLD_MAX)
        {
            // 将 mmap 阈值设置为 chunk 的大小
            mp_.mmap_threshold = chunksize(p);
            // 将 trim 阈值设置为 mmap 阈值的两倍
            mp_.trim_threshold = 2 * mp_.mmap_threshold;
            // 发送一个 probe，记录这次调整阈值的操作
            LIBC_PROBE(memory_mallopt_free_dyn_thresholds, 2,
                       mp_.mmap_threshold, mp_.trim_threshold);
        }
        // 释放这个 chunk
        munmap_chunk(p);
    }
    else
    {
        // 如果 tcache 还没有初始化，那么就初始化它
        MAYBE_INIT_TCACHE();

        // 将 chunk 标记为属于库，而不是用户
        (void)tag_region(chunk2mem(p), memsize(p));

        // 获取 chunk 所在的 arena
        ar_ptr = arena_for_chunk(p);
        // 释放这个 chunk
        _int_free(ar_ptr, p, 0);
    }

    // 恢复 errno
    __set_errno(err);
}
```

## _int_malloc (glibc-2.35)
```C

```
