# 静读天下专业版 APK 逆向解剖 Writeup

**作者：位异号　日期：2026-11-07**

本次分析的目标不是"找 flag"，而是把一个真实发布形态的商业 APK 从容器到 native 完整拆开：
ZIP 结构、签名链、二进制清单、DEX 代码、资源表、assets、native 库，最后落到"这个包被谁动过、
动在哪一步"的结论上。全程不使用 apktool / jadx / IDA，只用 Python 手写二进制解析器，
因此每一步都能给出字节级的依据。

---

## 分析对象

| 项目 | 内容 |
| --- | --- |
| 文件名 | `静读天下专业版.apk`（Moon+ Reader Pro） |
| 大小 | 58,484,076 字节（55.78 MiB） |
| 包名 | `com.flyersoft.moonreaderp` |
| 版本 | versionName 10.6 / versionCode 1006000 |
| SDK | minSdk 21 / targetSdk 36 / compileSdk 36 |
| 签名方案 | v1（JAR）+ v2（0x7109871a）+ v3（0xf05368c0） |
| 证书主体 | `CN=rockz5555, OU=Droid Freedom Unit, O=Droid Freedom Inc, C=LK` |

## 环境与工具

宿主是一台没有 Java 环境的 Windows，没有任何标准逆向工具链：

| 工具 | 状态 | 处置 |
| --- | --- | --- |
| apktool / jadx / dex2jar / aapt | 均无 | 自己写解析器 |
| java | 无 | 不依赖 |
| python | 3.12.10（`C:\Users\魏征\AppData\Local\Programs\Python\Python312\python.exe`） | 主力 |
| unzip / openssl | git-bash 自带 | 辅助校验 |

自建工具（全部在 `1111\tools\`，纯标准库，无第三方依赖）：

| 脚本 | 作用 |
| --- | --- |
| `axml2.py` | AXML（二进制 AndroidManifest / res/xml）解析 |
| `dexlib.py` | DEX 头部、字符串池、类型、方法、类定义、指令解析 |
| `arsc2.py` | resources.arsc 资源表解析 |
| `verify_sig.py` | MANIFEST.MF 逐条 SHA1 校验 |
| `zipforensic.py` | EOCD / 中央目录 / 签名块布局 |
| `mfsum.py` | 清单结构化提取（组件、权限、queries） |

> 说明：`python3` 在本机是 WindowsApps 的转发存根，执行无输出。所有命令都显式使用上表的绝对路径。

---

## 全局目录

1. **[容器层](#1-容器层)** — [0x01 ZIP 结构取证](#0x01-zip-结构取证)、[0x02 字节布局与对齐](#0x02-字节布局与对齐)
2. **[签名层](#2-签名层)** — [0x03 v1 签名校验](#0x03-v1-签名校验)、[0x04 APK Signing Block](#0x04-apk-signing-block)
3. **[清单层](#3-清单层)** — [0x05 AXML 二进制解析](#0x05-axml-二进制解析)、[0x06 清单内容解读](#0x06-清单内容解读)
4. **[代码层](#4-代码层)** — [0x07 DEX 结构解析](#0x07-dex-结构解析)、[0x08 类分布统计](#0x08-类分布统计)
5. **[资源层](#5-资源层)** — [0x09 resources.arsc](#0x09-resourcesarsc)、[0x0A res 与 assets](#0x0a-res-与-assets)
6. **[Native 层](#6-native-层)** — [0x0B .so 与 JNI 符号](#0x0b-so-与-jni-符号)
7. **[归因](#7-归因)** — [0x0C 重打包痕迹](#0x0c-重打包痕迹)
8. **[复盘](#8-复盘)**

---

# 1. 容器层

## 0x01 ZIP 结构取证

### 目标信息

- 目标：确认这个 APK 是不是"原厂出的"，打包方式有没有异常
- 手段：`zipfile` + 手工读 EOCD

### 分析过程

先看最外层。`.apk` 就是 ZIP，`zipfile` 能直接读，但默认 API 会把很多取证信息藏起来——比如条目时间戳只有 `date_time` 元组（2 秒精度）、没有记录 EOCD 位置。所以第一件事是手工算 EOCD：

```python
data = open('静读天下专业版.apk','rb').read()
eocd = data.rfind(b'PK\x05\x06')
cd_off  = int.from_bytes(data[eocd+16:eocd+20], 'little')   # 中央目录起始偏移
cd_size = int.from_bytes(data[eocd+12:eocd+16], 'little')
print(len(data), eocd, cd_off, cd_size)
# 58484076 58484054 58298368 185686
```

三个数字立刻给出两条结论：

1. `cd_off + cd_size == 58484054 == eocd`：中央目录紧贴 EOCD，中间没有夹带数据；
2. `eocd + 22 == len(data)`：EOCD 固定 22 字节，**文件尾没有追加任何内容**（没有隐藏负荷、没有第二个 ZIP）。

条目统计：

```
条目总数     2167
压缩方式     1293 条 DEFLATE / 874 条 STORED
解压后总大小 85,188,967 字节 = 81.24 MiB
压缩比       68.6%
```

874 条 STORED 不是随机分布，而是集中在 `.so` 和部分 `res/` 大图上——`.so` 不压缩是为了安装期直接 `mmap`，
属于正常做法。

### 遇到的问题

用 `zipfile.ZipFile(p).infolist()` 统计修改时间，2167 个条目只有两个不同值：

```
(2026, 5, 12, 15, 1, 58)  →     6 条
(2026, 5, 12, 15, 2, 0)   → 2161 条
```

真实项目里，`res/` 下的图片可能横跨几个月，绝不可能全部落在 2 秒内。这不是"版本更新导致"，
而是**整包被重新写过一次 ZIP**（重新打包时所有条目时间戳会被统一刷成打包时刻）。

**而那 6 条恰好是全部"编译产物"**：

```
AndroidManifest.xml
classes.dex / classes2.dex / classes3.dex / classes4.dex / classes5.dex
```

这 6 个文件是 `aapt2 + d8` 的输出，时间戳比其余 2161 条（`res/`、`assets/`、`lib/`、`META-INF/`）早 2 秒。
两段时间戳对应两个打包阶段：先是编译产物落盘，再是把资源目录整体 zip 进去。
换句话说，**资源不是由构建系统按清单挑出来的，而是"把目录整个压进去"**——这和后面 0x0A 里
根目录散落文件的现象互相印证。

### 技术总结

ZIP 层的取证优先级：EOCD 位置 → 尾部追加 → 中央目录偏移 → 时间戳分布 → 压缩方式分布。
时间戳过于统一，本身就是"被重新打包"的强信号。

---

## 0x02 字节布局与对齐

### 目标信息

- 目标：画出从文件头到中央目录的完整区间图，定位签名块
- 手段：计算每个区间的起止

### 分析过程

```
[0, 58,294,272)              条目数据区（local file header + data，共 2167 条）
[58,294,272, 58,298,368)     APK Signing Block（4096 字节）
[58,298,368, 58,484,054)     中央目录（185,686 字节）
[58,484,054, 58,484,076)     EOCD（22 字节）
```

签名块正好 4096 字节（一页），这是 `apksigner` 的典型填充行为——它会把签名块补齐到 4096 的整数倍，
方便按页对齐读取。

再看 `.so` 的对齐：

```
lib/arm64-v8a/librdpdf.so       5,446,384 字节  STORED
header_offset % 4096 = 2773      （未对齐）
```

24 个 `.so` 全部 STORED 但全部不对齐 —— 说明没有启用"直读"模式（`extractNativeLibs=false` 会把
库压进 ZIP 且强制 4K 对齐），装包时系统会先把库解压到 `/data/app/.../lib/`。这解释了包体为什么这么大。

### 技术总结

`.so` 的"是否压缩 + 是否 4K 对齐"两个信号组合起来，可以直接推出 `extractNativeLibs` 的取值，
进而推断运行时是从 APK 里 mmap 还是从解压目录加载。

---

# 2. 签名层

## 0x03 v1 签名校验

### 目标信息

- 目标：确认 v1 签名是否"覆盖了当前全部内容"
- 手段：读 `META-INF/MANIFEST.MF`，逐条比对 SHA1

### 分析过程

`META-INF` 下三个文件：

```
META-INF/MANIFEST.MF    200,803 字节   2164 条 Name: 记录
META-INF/BALA.SF        200,911 字节
META-INF/BALA.RSA         1,299 字节   PKCS#7 签名块 + 证书
```

证书解析：

```
$ openssl pkcs7 -inform DER -in META-INF/BALA.RSA -print_certs -out v1.pem
$ openssl x509 -in v1.pem -noout -subject -issuer -dates -serial -fingerprint -sha256

subject   = CN=rockz5555, OU=Droid Freedom Unit, O=Droid Freedom Inc, L=Unknown, S=Unknown, C=LK
issuer    = 同上（自签名）
notBefore = Dec  5 00:45:57 2014 GMT
notAfter  = Nov 27 00:45:57 2044 GMT
serial    = 638FBAD3  (十进制 1670363859)
SHA256    = 0C:FB:46:63:83:1A:0F:B8:D6:97:3A:AD:44:E2:21:A8:BA:78:F7:F6:84:BD:0B:17:D3:B4:4B:EC:82:31:64:84
```

`CN=rockz5555` + `O=Droid Freedom Inc` 是典型的第三方重打包者自签名证书（原厂 Moon+ 用的是自己的证书）。
2014 年生成，2044 年到期，标准的"一次生成用三十年"的野路子证书。

然后是关键一步：**v1 签名只对 MANIFEST 里的摘要负责，而 MANIFEST 里的摘要是否等于当前文件内容，必须自己验。**
`java -jar jarsigner -verify` 做不到（没有 JDK），所以手写：

```python
import hashlib, base64, zipfile

z  = zipfile.ZipFile('静读天下专业版.apk')
mf = z.read('META-INF/MANIFEST.MF').decode('utf-8')

# 1) 先把折行拼回逻辑行（Name 和 SHA1-Digest 都会折，续行以单空格开头）
lines = []
for line in mf.split('\r\n'):
    if line.startswith(' ') and lines:
        lines[-1] += line[1:]
    else:
        lines.append(line)              # 空行要保留，它是条目分隔符

# 2) 按空行切条目
entries, cur = [], {}
for line in lines:
    if not line:
        if cur: entries.append(cur); cur = {}
        continue
    if line.startswith('Name: '):            cur['name'] = line[6:]
    elif line.startswith('SHA1-Digest: '):   cur['digest'] = line[13:]
if cur: entries.append(cur)

# 3) 逐条比对
bad = 0
for e in entries:
    real = base64.b64encode(hashlib.sha1(z.read(e['name'])).digest()).decode()
    if real != e['digest']:
        bad += 1; print('MISMATCH', e['name'])
print('entries', len(entries), 'mismatch', bad)
# entries 2164  mismatch 0
```

**2164 条摘要全部匹配，0 处不符。**

这个结果的份量在于：它说明"当前 APK 里的每一个字节，都和签名时 MANIFEST 记录的一致"。
换句话说，重打包者不是"改完文件忘了更新签名"，而是**完整地重新签了一次 v1**。

### 遇到的问题

**坑一：折行。** JAR 清单的三个字段都会折行，规则是"每行不超过 72 字节，续行以一个空格开头"：

```
Name: META-INF/services/kotlinx.coroutines.internal.MainDispatcherFact
 ory
SHA1-Digest: NZutgXM1VN70m5xDsTtKjrcsYuw=
```

第一版脚本只拼了 `SHA1-Digest` 的续行，没拼 `Name` 的续行，结果 2164 条里有 **45 条被误判成 MISSING**：

```
manifest digests=2164 ok=2119 bad=0 missing=45
```

因为被截断的名字（`...animation.xm`）在 ZIP 里找不到（实际是 `...animation.xml`）。
把 `Name` 的续行也拼回去之后才是真实结果：

```
manifest digests=2164 ok=2164 bad=0 missing=0
```

这条教训值得单独记：**"缺失 45 个文件"这种听起来像重大发现的结论，很可能只是解析器少拼了一次字符串。**
凡是出现"系统性缺失"，先怀疑自己的解析，再怀疑样本。

**坑二：空行。** 修折行的时候顺手把空行丢掉了（`if buf: lines.append(buf)`），结果条目之间没了分隔，
2164 条黏成 1 条。修法是保留空行：

```python
lines = []
for line in raw.split('\r\n'):
    if line.startswith(' ') and lines:
        lines[-1] += line[1:]
    else:
        lines.append(line)      # 空行是条目分隔符，不能丢
```

### 技术总结

v1 校验要分两层：`BALA.RSA` 用私钥签 `BALA.SF`，`BALA.SF` 里存 `MANIFEST.MF` 的摘要，
`MANIFEST.MF` 里存每个条目的摘要。**只有最内层能自证**（直接对文件算），外面两层需要公钥验签。
无 JDK 时，最内层已经足够回答"内容有没有被改过"。

最终的统计是：**2164 条摘要，2164 条匹配，0 处不符，0 处缺失。**

---

## 0x04 APK Signing Block

### 目标信息

- 目标：确认 v2/v3 签名是否存在、是否有效、证书是否与 v1 一致
- 手段：手工解析 signing block，并重算 v2 内容摘要

### 分析过程

这一步是本轮分析里唯一一次**结论被自己推翻**的地方，值得完整记录。

**第一轮（错）**：我写了个简单判断——在中央目录前 16 字节处比对 `APK Sig Block 42` 魔数，
然后在结论里写下"无 APK Signing Block（无 v2/v3），仅 v1"。

**发现异常**：写报告时为了引用中央目录偏移，顺手跑了一次
`data.find(b'APK Sig Block 42')`，返回 **58,298,352**，而中央目录在 58,298,368。
`58,298,368 − 58,298,352 = 16` —— 魔数正好占满中央目录前的 16 字节。

**魔数在**。也就是说签名块存在，是我的第一个判断逻辑写错了。

正确的结构（v2 规范）：

```
uint64  size_of_block               块总长 - 8
pairs[]                             id(4) | value_length(8, 含 id) | value
uint64  size_of_block               与开头相同
bytes   "APK Sig Block 42"          16 字节魔数
central directory
```

按此解析：

```python
eocd = data.rfind(b'PK\x05\x06')
cd   = int.from_bytes(data[eocd+16:eocd+20], 'little')
size2 = int.from_bytes(data[cd-24:cd-16], 'little')      # 尾部 size 字段
start = cd - 8 - size2                                    # 块起始
print(start, size2, data[cd-16:cd])                       # 58294272 4088 b'APK Sig Block 42'
```

块内成对项：

```
id=0x7109871a  v2   len=1511
id=0xf05368c0  v3   len=1503
（其余为 0x42726577 padding 对，用于把块补齐到 4096）
```

**v2 与 v3 都在。**

接着是最关键的一步：**v2 的摘要是否对得上当前内容**。v2 不是对整文件做一次哈希，而是分三段、按 1 MiB 分块：

```
chunk_digest = SHA256(0xA5 || uint32LE(chunk_len) || chunk_bytes)
content_digest = SHA256(0x5A || uint32LE(chunk_count) || concat(chunk_digest...))

section 1 = [0, block_start)              条目区
section 2 = [cd, eocd)                   中央目录
section 3 = EOCD，但把其中"中央目录偏移"字段改写为 block_start
```

实现：

```python
import hashlib

def agg(secs, CS=1 << 20):
    hs = []
    for s in secs:
        for i in range(0, len(s), CS):
            c = s[i:i+CS]
            hs.append(hashlib.sha256(b'\xa5' + len(c).to_bytes(4,'little') + c).digest())
    return hashlib.sha256(b'\x5a' + len(hs).to_bytes(4,'little') + b''.join(hs)).hexdigest()

e2 = bytearray(data[eocd:]); e2[16:20] = start.to_bytes(4,'little')
print(agg([data[:start], data[cd:eocd], bytes(e2)]))
# e41e53f34811a25ee596dd9288e7c42752615f1d55d418087409d87e0e15bd73
```

再从未经签名的面取期望值 —— 从 v2 的 signed data 里把摘要抠出来：

```
signed_data 结构：  digests(seq) | certificates(seq) | additional_attributes(seq)
digests 第一个条目： alg_id=0x0103（RSA-PKCS1v1.5 + SHA-256）, digest=32 字节
期望值 = e41e53f34811a25ee596dd9288e7c42752615f1d55d418087409d87e0e15bd73
```

**两者完全相等。** v2 签名有效，且签名块里的证书与 v1 是同一张：

```
v2 证书 DER 的 SHA256 = 0cfb4663831a0fb8d6973aad44e221a8ba78f7f684bd0b17d3b44bec82316484
v1 证书 DER 的 SHA256 = 0cfb4663831a0fb8d6973aad44e221a8ba78f7f684bd0b17d3b44bec82316484
```

### 遇到的问题

**坑一：先入为主。** 第一版判断"块是否存在"时，我用的是"中央目录前 16 字节不等于魔数则不存在"，
但那个位置在块内其实是魔数的**末尾**，而魔数起点在 `cd-16`，读偏了 16 字节，直接得出相反结论。
教训很直白：**这类判断必须打印十六进制，肉眼确认边界，不要靠"偏移量大概是……"**。

**坑二：摘要算了不算。** 第一次重算时我把三段分别算哈希，然后拿"sec1 的哈希"去和期望值比，
当然对不上。v2 的摘要不是三段并列，而是**三段的所有分块拼成一个大列表再整体哈希一次**。
分段是分块边界的问题，不是聚合层次的问题。

**坑三：EOCD 要打补丁。** 第三段必须把 EOCD 里的中央目录偏移改写成签名块起点，
因为签名时签名块还不存在，EOCD 记录的是"没有块时"的偏移。漏了这一步，第三段哈希必错。

### 技术总结

APK 的签名其实是三层递进：地址布局 → 内容摘要 → 公钥验签。
本轮把前两层做到了字节级自证（v1 逐条 SHA1、v2 内容摘要重算），第三层（RSA 验签）因为没 JDK 没做，
但证书一致性已经能把"是否同一签名者"钉死。

**结论修正：不是"仅 v1"，而是 v1 + v2 + v3 齐全且 v2 摘要有效。**
这反过来说明：重打包者用的不是"手工改 zip 再补 v1"的粗糙流程，而是跑过 `apksigner` 的完整重签流程。

---

# 3. 清单层

## 0x05 AXML 二进制解析

### 目标信息

- 目标：拿到可读的 `AndroidManifest.xml`（编译后是 AXML 二进制）
- 手段：手写 AXML 解析器

### 分析过程

`AndroidManifest.xml` 24,580 字节，开头是 `03 00 08 00` —— 典型的 AXML 头（类型 0x0003，头长 8）。
整体分四段：

```
XML header      8 字节
String Pool     字符串池（UTF-8 或 UTF-16，由 flags 决定）
Resource Map    资源 id 数组（属性名到 0x7f... 的映射）
Element 流      START_NAMESPACE / START_ELEMENT / END_ELEMENT / CDATA
```

元素节点的结构（`ResXMLTree_node`）：

```
uint16 type         0x0102=START_ELEMENT, 0x0103=END_ELEMENT
uint16 headerSize   通常 16
uint32 size
uint32 lineNumber
uint32 comment
--- 以下为 START_ELEMENT 扩展 ---
uint32 ns
uint32 name           指向字符串池
uint16 attributeStart 20
uint16 attributeSize  20      ← 单个 attribute 的固定步长
uint16 attributeCount
uint16 idIndex
uint16 classIndex
uint16 styleIndex
attribute[attributeCount]
```

单个 attribute 的布局（`ResXMLTree_attribute`，**共 20 字节**）：

```
uint32 ns        4
uint32 name      4
uint32 rawValue  4
uint16 valueSize 2   = 8
uint8  res0      1
uint8  dataType  1
uint32 data      4
```

解析代码的核心：

```python
ATTR_STRIDE = 20          # 关键：固定 20 字节，不是 8 + valueSize

def parse_attrs(pool, buf, off, count):
    out = {}
    for i in range(count):
        p = off + i * ATTR_STRIDE
        ns   = u32(buf, p)
        name = u32(buf, p + 4)
        raw  = u32(buf, p + 8)
        vsz  = u16(buf, p + 12)
        typ  = buf[p + 15]
        data = u32(buf, p + 16)

        key = pool[name]                       # 属性名必须取字符串池字面值
        if typ == 0x03:      val = pool[data]   # string
        elif typ == 0x01:    val = '@ref/0x%08x' % data   # reference
        elif typ == 0x12:    val = bool(data)   # boolean
        elif typ == 0x11:    val = hex(data)    # hex int
        elif typ == 0x10:    val = data         # dec int
        else:                val = 'type0x%02x:0x%x' % (typ, data)
        out[key] = val
    return out
```

### 遇到的问题

**这是全场最贵的一个 bug。** 第一版我写的是：

```python
p += a_vsize      # 错！a_vsize 是 Res_value 的长度=8，不是整个 attribute 的长度
```

结果读到第三个属性时指针就飞到了 79,147，直接越界崩溃；
更早的版本没崩，但属性错位，把 `android:exported="true"` 读成了 `android:targetActivity`，
整份清单看起来"有 30 多个属性但全是乱的"。

正确的做法是**用 `attributeSize` 字段（值恒为 20）作为步长**，而不是用 value 的长度。
AXML 的 attribute 是定长结构，就是为了让解析器能 O(1) 跳转。

第二个坑是属性名。AXML 里每个属性同时有：
- `name`：指向字符串池的下标（如 `"name"`）
- 以及资源映射表里的 `0x7f...` id

如果偷懒用资源 id 反查名字（拿 `public.xml` 或内置表猜），会得到 `android:name`、`app:name` 混淆的结果。
**必须用字符串池里的字面值**，它才是编译时真正写进去的那个。

### 技术总结

二进制 XML 的三个不变量：
1. 每个 chunk 都是 `type | headerSize | size` 开头，按 `size` 前进，永不按内容长度前进；
2. attribute 是定长 20 字节；
3. 所有字符串都在池里，索引是 u32。

记住这三条，AXML 基本不会写错。

---

## 0x06 清单内容解读

### 目标信息

- 目标：梳理应用面（权限 / 组件 / 外部依赖）
- 手段：`mfsum.py` 结构化输出

### 分析过程

```
package            com.flyersoft.moonreaderp
versionName        10.6
versionCode        1006000
minSdkVersion      21
targetSdkVersion   36
compileSdkVersion  36
application        androidx.multidex.MultiDexApplication
appComponentFactory androidx.core.app.CoreComponentFactory
allowBackup        true
requestLegacyExternalStorage  true
```

**权限（12 条）**：

```
android.permission.INTERNET
android.permission.ACCESS_NETWORK_STATE
android.permission.WRITE_EXTERNAL_STORAGE      maxSdkVersion=32
android.permission.READ_EXTERNAL_STORAGE       maxSdkVersion=32
android.permission.MANAGE_EXTERNAL_STORAGE     ← 全盘读写
android.permission.FOREGROUND_SERVICE
android.permission.FOREGROUND_SERVICE_MEDIA_PLAYBACK
android.permission.POST_NOTIFICATIONS
android.permission.USE_BIOMETRIC
android.permission.USE_FINGERPRINT
com.android.launcher.permission.INSTALL_SHORTCUT
com.flyersoft.moonreaderp.DYNAMIC_RECEIVER_NOT_EXPORTED_PERMISSION   （自定义）
```

`MANAGE_EXTERNAL_STORAGE` 是关键字：这是"所有文件访问权限"，上架 Google Play 需要专门申报理由。
对一个阅读器来说它是"扫全盘找书"的实现方式，但也意味着 App 进程可以读写任意用户文件。

**组件**：

```
activity 15 / service 4 / receiver 3 / provider 3
显式 exported="true" 7 个，另有通过 intent-filter 隐式导出的组件
```

导出的组件里值得注意的：

| 组件 | 类型 | 风险点 |
| --- | --- | --- |
| `ActivityMain` | Activity | 启动入口，接受外部 Intent |
| `MediaAct` | Activity | 媒体播放，接受外部 URI |
| `components.OpenFile_Receiver` | Receiver | 外部可广播触发文件打开 |
| `com.dropbox.core.android.AuthActivity` | Activity | 第三方 SDK 的 OAuth 回调 |
| `com.radaee.pdf.CaptureSignature` | Activity | PDF 手写签名界面 |
| `BookViewProvider` | Provider | 书籍数据 provider |

**`<queries>`（Android 11+ 的包可见性声明）**：

```
com.flyersoft.moonreader            （免费版包名，做互跳）
com.dropbox.android
intent: android.intent.action.TTS_SERVICE
intent: android.intent.action.SEARCH
intent: android.intent.action.SEND
intent: android.intent.action.PROCESS_TEXT
```

`TTS_SERVICE` 这条说明它把朗读交给系统 TTS 引擎，自己不实现合成。

### 技术总结

读清单时按"权限 → 导出组件 → queries"三遍扫：
第一遍看它能碰什么（MANAGE_EXTERNAL_STORAGE），第二遍看别人能碰它什么（7 个导出），
第三遍看它想和谁通信（queries 是最诚实的"功能清单"）。

---

# 4. 代码层

## 0x07 DEX 结构解析

### 目标信息

- 目标：不解包、不反编译，直接统计代码规模与结构完整性
- 手段：手写 DEX 解析器

### 分析过程

APK 里有 5 个 dex：

```
classes.dex    7,634,380   6,536 类
classes2.dex         548       1 类      ← 异常
classes3.dex   8,485,244   7,126 类
classes4.dex   6,828,304   7,412 类
classes5.dex   6,933,980   6,084 类
```

`classes2.dex` 只有 548 字节、1 个类，内容是：

```
Landroid/security/keystore/KeyPermanentlyInvalidatedException;
```

这是 minSdk 21 + multidex 的经典兼容垫片：API 23 才有这个异常类，为了在 21/22 上不 NoClassDefFoundError，
打包工具会生成一个只含该类的 dex 占位。属于正常现象，不是后门。

DEX 头部校验（`dexlib.py`）：

```
magic    dex\n035\0
checksum adler32(从 offset 12 到文件尾)   ← 全部自洽
signature SHA1(从 offset 32 到文件尾)     ← 全部自洽
file_size 与实际长度一致
```

统计结果：

```
类总数      27,159
方法总数   233,684
字段总数    99,037
字符串总数 196,169
```

解析链路（简化）：

```python
class Dex:
    def __init__(self, b):
        self.b = b
        self.string_ids_size, self.string_ids_off = u32(b,56), u32(b,60)
        self.type_ids_size,   self.type_ids_off   = u32(b,64), u32(b,68)
        self.proto_ids_size,  self.proto_ids_off  = u32(b,72), u32(b,76)
        self.field_ids_size,  self.field_ids_off  = u32(b,80), u32(b,84)
        self.method_ids_size, self.method_ids_off = u32(b,88), u32(b,92)
        self.class_defs_size, self.class_defs_off = u32(b,96), u32(b,100)

    def string(self, i):
        p = self.string_ids_off + i*4
        return self._mutf8(self.data_off(p))     # uleb128 长度 + MUTF-8
```

`class_def_item` 是 32 字节定长：

```
uint32 class_idx        → type_ids → 类描述符
uint32 access_flags
uint32 superclass_idx
uint32 interfaces_off
uint32 source_file_idx  ← 关键
uint32 annotations_off
uint32 class_data_off   → uleb128 编码的字段/方法表
uint32 static_values_off
```

**重要发现：27,159 个类的 `source_file_idx` 全部是 -1（0xFFFFFFFF）。**

正常的 Android 构建，即使是 release 包，`source_file_idx` 也会指向 `"MainActivity.java"` 这样的名字
（ProGuard/R8 默认保留 `SourceFile` 属性）。全 -1 说明**额外做了一步源文件名剥离**，
这是商业软件防逆向的常规操作，也让"通过异常堆栈定位源码类名"这条路彻底断掉。

`class_data_item` 用 uleb128 变长编码：

```
uleb128 static_fields_size | instance_fields_size | direct_methods_size | virtual_methods_size
encoded_field[]   field_idx_diff(uleb128) + access_flags(uleb128)
encoded_method[]  method_idx_diff + access_flags + code_off(uleb128)
```

跳到 `code_off` 就是 `code_item`：`registers_size | ins_size | outs_size | tries_size | debug_info_off | insns_size | insns[]`。

### 遇到的问题

MUTF-8 不是 UTF-8：`0xC0 0x80` 表示 `\0`，超过 BMP 的字符用**代理对**分别编码成 3 字节。
用 `bytes.decode('utf-8')` 会在遇到 `\0` 或代理对时报错。必须自己解：

```python
def _mutf8(self, p):
    n = self.uleb128_at(p); p += self._leb_len(p)
    out = []
    while n:
        c = self.b[p]
        if c < 0x80:            out.append(chr(c)); p += 1; n -= 1
        elif c & 0xE0 == 0xC0:  out.append(chr(((c & 0x1F) << 6) | (self.b[p+1] & 0x3F))); p += 2; n -= 2
        elif c & 0xF0 == 0xE0:  out.append(chr(((c & 0x0F) << 12) | ((self.b[p+1] & 0x3F) << 6) | (self.b[p+2] & 0x3F))); p += 3; n -= 3
        else:                   out.append('?'); p += 1; n -= 1
    return ''.join(out)
```

### 技术总结

DEX 是"索引 + 偏移"的典型结构：所有真实数据都在 `data` 段，头部只是一张索引表。
抓住 `string_ids → type_ids → proto/field/method → class_defs → class_data → code_item` 这条链，
就能在没有反编译器的情况下统计出全部代码规模。

---

## 0x08 类分布统计

### 目标信息

- 目标：看清代码构成——哪些是自己的，哪些是第三方
- 手段：按包前缀聚合 `class_defs`

### 分析过程

按顶级包聚合（前五）：

```
Lcom/dropbox/core/v2              5,079 类
Lio/reactivex/rxjava3/internal    1,560 类
Lcom/google/android/gms           1,541 类
Lcom/google/common/collect        1,115 类
Lcom/google/android/material      1,025 类
```

自有代码：

```
Lcom/flyersoft                    2,279 类
  ├ components/cloud                177
  ├ components/androidsvg           146
  ├ books/chmlib                     48
  └ ...
Lcom/flyersoft/moonreaderp           53 类（顶层）
  ActivityMain, ActivityTxt, MediaAct, BookTtsService, BookViewProvider,
  BookView*, PrefXxx ×40 ...
```

两个比例值得注意：

1. **Dropbox SDK 是最大单一包**（5,079 类，占全部类的 18.7%），比应用自身代码还多一倍多。
   Dropbox 的 Java SDK 是出了名的"重"，一个云同步功能拖进来半个网络栈。
2. **自有代码只占 8.4%**（2,279 / 27,159）。这在大厂商业 App 里是常态：
   UI 框架、图片库、网络库、云 SDK 占大头，真正"这是 Moon+ Reader"的部分不到十分之一。

### 技术总结

类分布统计是"低成本高收益"的一步：不用反编译，就能判断技术栈、判断哪些是自研、
判断依赖里有没有已知高危库（比如老的 OkHttp、老的 GMS）。

---

# 5. 资源层

## 0x09 resources.arsc

### 目标信息

- 目标：读出资源表的完整结构
- 手段：手写 ARSC 解析器

### 分析过程

`resources.arsc` 3,395,628 字节，单包结构：

```
RES_TABLE_TYPE (0x0002)
  header
  RES_STRING_POOL_TYPE (0x0001)       全局字符串池
  RES_TABLE_PACKAGE_TYPE (0x0200) ×1  包 id = 0x7f
    RES_TABLE_TYPE_SPEC_TYPE (0x0202)  每个类型一份（条目数/配置标志）
    RES_TABLE_TYPE_TYPE (0x0201)       每个类型 × 每种配置一份（真正的条目）
```

解析逻辑：

```python
def walk(buf, start, end):
    p = start
    while p < end:
        ctype = u16(buf, p)
        hsize = u16(buf, p + 2)
        size  = u32(buf, p + 4)
        if ctype == 0x0200:                      # package
            pkg_id = u32(buf, p + 8)
            type_strings_off = u32(buf, p + 268)
            key_strings_off  = u32(buf, p + 276)
            walk(buf, p + hsize, p + size)
        elif ctype == 0x0202:                    # type spec：只记"有几个条目"
            type_id = buf[p + 8]
            counts[type_id] = (size - hsize) // 4
        elif ctype == 0x0201:                    # type：真正的条目
            type_id = buf[p + 8]
            cfg_size = u32(buf, p + 20)
            entries_start = u32(buf, p + 24)
            n = (entries_start - hsize) // 4
            for i in range(n):
                eo = u32(buf, p + hsize + i*4)
                if eo == 0xFFFFFFFF: continue     # 该配置下无此条目
                ep = p + entries_start + eo
                if u16(buf, ep) == 0x0008:        # RES_TABLE_ENTRY（紧凑）
                    ...
        p += size
```

统计结果：

```
包数量            1（id = 0x7f）
类型数量          20
key 数量          7,965
TYPE 块（0x0201）290 个
配置数量          125 种
条目总数          135,689
```

按类型分布（前九）：

```
string     83,072
style      18,848
dimen      11,600
drawable   11,144
color       3,640
layout      2,136
id          1,824
array       1,680
attr        1,314
```

83,072 条字符串——这个数字解释了为什么这个包有 196,169 条 DEX 字符串：
多语言（`assets/readme` 有 22 个语言目录）+ 大量文案资源。

### 遇到的问题

**`0x0201` 与 `0x0202` 搞反。** 第一版我写的是：

```python
if ctype == 0x0201:  # 我以为是 TYPE_SPEC
    counts[type] = ...
```

结果每种类型的条目数全是 0，因为 `TYPE_SPEC` 只有 8 字节的头 + 一个 `unit` 数组，而我按 `TYPE` 去读
`entries_start`，读到的全是 0。

这两个 chunk 的正确含义：

- `0x0202 RES_TABLE_TYPE_SPEC_TYPE`：**声明**某类型在本包里有几个条目（全局），数量少；
- `0x0201 RES_TABLE_TYPE_TYPE`：**具体的**某一配置下该类型的条目偏移表，数量多（类型 × 配置）。

所以"290 个 0x0201 vs 20 个 0x0202"是正常的，不是我算错。

第二个坑是累计方式：

```python
counts[type] = 0          # 错：每个 chunk 进来都清零
counts[type] = counts.get(type, 0) + n   # 对
```

### 技术总结

ARSC 是"三层索引"：包 → 类型 → 配置。任何一层用错，统计结果都会静默变成 0 或重复计数——
**不报错**，这是它最阴的地方。判断方法：拿 `string` 类型的条目数去和 DEX 的字符串数比，
数量级对不上就说明解析层级错了。

---

## 0x0A res/ 与 assets/

### 目标信息

- 目标：摸清资源文件构成，找异常
- 手段：按目录聚合 `ZipInfo`

### 分析过程

`res/` 共 1,857 个条目，目录分布（前九）：

```
res/drawable                458
res/layout                  355
res/drawable-hdpi           310
res/color                   178
res/drawable-xhdpi          126
res/drawable-xxhdpi         114
res/layout-v22               95
res/anim                     60
res/animator                 33
```

`assets/` 共 122 个文件、约 6.6 MB：

```
assets/background      33
assets/hyphenation     22   （断词词典，按语言分）
assets/readme          22   （22 种语言的说明）
assets/book            13   （示例书）
assets/themes          12
assets/network          6   （在线书源配置）
assets/fonts            4
```

`hyphenation` + `readme` 的多语言分布，是"这是一个面向全球市场的成熟产品"的直接证据。

**根目录下的异常条目**（这是本轮最有意思的发现）：

```
credentials.json      364
simp.txt          104,508
trad.txt          104,508
simplified.txt     12,702
traditional.txt    64,761
unknown.txt         3,148
pinyin.txt              0
polyphone.txt           0
```

再加上几个**本该在 assets 下、却躺在 APK 根目录**的目录：

```
com/google/api/client/googleapis/google.jks    71,764   ← 签名库！
com/google/api/client/googleapis/google.p12    76,476
org/apache/commons/codec/language/bm/*.txt      130 个（语音编码数据）
kotlin/*.kotlin_builtins                          7 个
mozilla/public-suffix-list.txt                    1 个
```

`credentials.json` 内容是标准 Google OAuth 客户端配置：

```json
{ "installed": { "client_id": "237912218931-dgqu52ni...", ...
```

`google.jks` / `google.p12` 是 Google API 客户端库自带的**默认密钥库**（公共测试用途，不含秘密），
但它们出现在 APK 根目录而不是 assets，同样说明打包时文件被"拍平"过。

### 遇到的问题

一开始我以为根目录这些文件是"作者放的彩蛋"。查过之后不是：

- `simp.txt` / `trad.txt` 各 104,508 字节，字节数完全一致 —— 是简繁对照表；
- `simplified.txt` / `traditional.txt` / `unknown.txt` / `pinyin.txt` / `polyphone.txt` 是多音字处理数据。

这些在 Moon+ 里是"简繁转换 + 拼音注音"的运行时数据，正常位置是 `assets/`。
它们在 APK 根目录，说明**重打包时用了"把整个工作目录 zip 进去"的粗暴方式**，
而不是走 `aapt2` 的标准资源合并流程。

### 技术总结

"文件位置异常"比"文件内容异常"更容易被发现，也更难辩解。
判断标准很简单：**Android 只认几个固定位置**（`res/`、`assets/`、`lib/`、`META-INF/`、根目录的几个文件），
其余一切出现在根目录的东西，都是打包流程失控的痕迹。

---

# 6. Native 层

## 0x0B .so 与 JNI 符号

### 目标信息

- 目标：确认 native 部分的功能与攻击面
- 手段：ELF 动态符号表扫描 + 字符串搜索

### 分析过程

24 个 `.so` = 4 个 ABI × 6 个库：

| 库（arm64-v8a） | 大小 | JNI 符号 |
| --- | --- | --- |
| `librdpdf.so` | 5,446,384 | 505 个 `Java_com_radaee_pdf_*` |
| `libmydjvu.so` | 1,967,952 | 31 个 |
| `libmloader.so` | 253,392 | 6 个 `Java_com_dozof_app_MLoader_*` |
| `libnative-imagetranscoder.so` | 585,376 | 0（JNI_OnLoad 动态注册） |
| `libnative-filters.so` | 23,712 | 0（同上） |
| `libimagepipeline.so` | 8,760 | 0（同上） |

四条 ABI 说明这个包在 2026 年还在支持 32 位 —— 对应大量老旧国产阅读设备。

`librdpdf.so` 是 **Radaee PDF SDK**，505 个导出 JNI 函数覆盖了 PDF 渲染、注释、表单、签名、加密。
`libmydjvu.so` 是 DjVu 格式支持。`libmloader.so`（`com.dozof.app`）是 MOBI/AZW3 解析器。
后三个是 Facebook Fresco 图片管线，统一用 `JNI_OnLoad` 动态注册，所以静态符号表是空的。

验证方式（不反汇编，只读 `.dynsym` 的字符串）：

```python
def jni_symbols(so_bytes):
    out = []
    for m in re.finditer(rb'Java_[A-Za-z0-9_]{3,120}', so_bytes):
        s = m.group().decode('ascii', 'ignore')
        if s not in out: out.append(s)
    return out
```

### 技术总结

对阅读器类 App，native 层就是**文件解析器**：PDF、DjVu、MOBI。
这一层是历史漏洞的重灾区（PDF 解析器几乎年年有 CVE），
所以库版本比库功能更值得追：`librdpdf.so` 的版本号通常能从内部字符串里读出来。

---

# 7. 归因

## 0x0C 重打包痕迹

### 目标信息

- 目标：回答"这个包是谁打的、怎么打的"
- 手段：把前面所有线索串起来

### 分析过程

把六条证据摆在一起：

| 证据 | 指向 |
| --- | --- |
| 证书 `CN=rockz5555 / O=Droid Freedom Inc` | 非原厂签名 |
| 2167 条目时间戳集中在 2 秒内 | 整包被重写过一次 |
| 根目录散落 `simp.txt`、`google.jks`、`kotlin/` 等 | 打包时工作目录被整体 zip |
| v1 摘要 2164 条全部匹配 | 改完之后重新签了 v1 |
| v2 摘要重算后完全一致 | 不是手工补签，是跑过 `apksigner` |
| `credentials.json` 带 OAuth client_id | 保留了原作者的开发期配置 |

结论：**这是一次"解包 → 改 → 用标准工具重签"的完整重打包**，不是简单的字节补丁。
重签流程完整到 v2/v3 都对，说明操作者熟悉 Android 签名工具链。

至于改了什么：`MANIFEST.MF` 与内容一致只证明"自洽"，不能证明"和原版一致"。
要回答这个必须拿官方原版做二进制 diff —— 本轮没有原版，所以这一条**留白**，不做推测。

### 技术总结

APK 归因的三条硬指标：
1. 证书主体（谁签的）；
2. 时间戳分布（什么时候重写的）；
3. 打包布局异常（用什么工具打的）。

三条互相独立，只要有一条异常，就足以证明"这不是原厂包"。

---

# 8. 复盘

## 方法层面

这轮最有价值的不是结论，而是**在没有工具链的情况下把"不可能"拆成了"可以"**：

1. **先定边界，再挖细节。** 顺序是 ZIP → 签名 → 清单 → 代码 → 资源 → native。
   每一步的输出都是下一步的输入（比如中央目录偏移是解析签名块的前提）。
2. **每个结论都要有字节级的出处。** "无 v2 签名"这个错误结论，就是因为只看了 16 字节的错位位置。
   凡涉及偏移的判断，必须 hexdump 确认。
3. **不报错 ≠ 正确。** ARSC 把 type/spec 搞反时条目数静默变 0；AXML 步长错误时属性名静默错位。
   所以要设置"外部一致性校验"：ARSC 的 string 条目数 vs DEX 的字符串数，量级必须对得上。
4. **自证优先于信任工具。** 没有 `apksigner`，就手算 v2 摘要。手算出来的结论比"工具说 OK"更硬，
   因为你能说清它为什么 OK。

## 工程层面

四个坑，每个都值得记：

| 坑 | 表现 | 根因 |
| --- | --- | --- |
| AXML 属性步长 | 指针飞到 79,147 越界 | 用 `valueSize`(=8) 当步长，实际是固定 `attributeSize`(=20) |
| ARSC chunk 类型 | 所有条目数 = 0 | `0x0201`(TYPE) 与 `0x0202`(TYPE_SPEC) 搞反 |
| ARSC 累计 | 数字重复 | `counts[k] = 0` 覆盖了之前的累加 |
| 签名块判断 | 结论完全相反 | 魔数在 `cd-16`，却去 `cd-16` 之外的位置比对 |

## 结论

- 容器：2167 条目、81.24 MiB、无尾部追加、`.so` 未压缩未对齐（`extractNativeLibs=true`）
- 签名：v1 + v2 + v3 齐全，v2 内容摘要重算通过，证书 `CN=rockz5555`（自签，2014 年签发）
- 清单：targetSdk 36、`MANAGE_EXTERNAL_STORAGE`、7 个显式导出组件
- 代码：27,159 类 / 233,684 方法，自有代码 8.4%，`source_file_idx` 全 -1（源文件名已剥离）
- 资源：135,689 条目、83,072 字符串、22 种语言 readme
- Native：4 ABI × 6 库，Radaee PDF / DjVu / MOBI 三套解析器
- 归因：完整重打包，重签流程规范；具体改动内容需要原版 diff 才能定论

---

## 附：复现清单

```bash
# 0. 环境
PY="C:/Users/魏征/AppData/Local/Programs/Python/Python312/python.exe"

# 1. 容器层
$PY -c "import zipfile;z=zipfile.ZipFile('静读天下专业版.apk');print(len(z.infolist()))"

# 2. v1 逐条校验
$PY tools/verify_sig.py 静读天下专业版.apk

# 3. 签名块
$PY -c "d=open('静读天下专业版.apk','rb').read();print(d.find(b'APK Sig Block 42'))"

# 4. 清单
$PY tools/mfsum.py 静读天下专业版.apk > manifest.txt

# 5. DEX 统计
$PY tools/listclasses.py 静读天下专业版.apk > out_classes.txt

# 6. 资源表
$PY tools/arsc2.py 静读天下专业版.apk > arsc_report.txt

# 7. native 符号
$PY tools/scanstrings.py 静读天下专业版.apk > so_symbols.txt

# 8. 证书
unzip -o 静读天下专业版.apk META-INF/BALA.RSA
openssl pkcs7 -inform DER -in META-INF/BALA.RSA -print_certs | openssl x509 -noout -subject -dates
```

产物与本文件同目录：`APK解剖报告.md`、`index.csv`、`manifest.txt`、`arsc_report.txt`、`out_classes_classes*.dex.txt`。
