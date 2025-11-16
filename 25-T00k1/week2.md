# 完成事项</font>
+ Python基本内容学习
+ 完成了一些题目制作和脚本编写
+ 安装学习使用了lazyIDA,研究了一下IDA的各种功能
# 下周待做事项</font>
+ 继续做题,巩固代码分析编写能力
# 本周学习的知识分享</font>
## python学习的最后一条有点用的余温(目前)
+ for循环的再次理解
创建一个用于存储外星人的空列表。 
  aliens = [] 
 
 创建30个绿色的外星人。 
for alien_number in range(30): 
     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'} 
     aliens.append(new_alien) 
 
 显示前5个外星人。 
for alien in aliens[:5]: 
      print(alien) 
  print("...") 
按直接理解的意思是将1,2,3...赋给alien_number一轮一轮去工作了,但是alien_number后面再没有出现过
了

这可真是令人费解,经过我和deepseek的深入交流后才明白过来,for循环根本就不是一定要让它"对于"的东西去执行操作的,这里的alien_number纯粹就是一个计数器,就是说我有这个变量了,用不用就是另一回事了,这个代码是构史,应该这样把它用上

for alien_number in range(30):
    new_alien = {
        'color': 'green', 
        'points': 5, 
        'speed': 'slow',
        'id': alien_number  # 这里用到了它进行循环操作1,2,3,4.........
    }
    aliens.append(new_alien)

 现在每个外星人都有唯一的id了
## Reversing-x64Elf-100
+ 一道有点意思的题
```
{
  int i; // [rsp+14h] [rbp-24h]
  __int64 v3[4]; // [rsp+18h] [rbp-20h]

  v3[0] = (__int64)"Dufhbmf";
  v3[1] = (__int64)"pG`imos";
  v3[2] = (__int64)"ewUglpt";
  for ( i = 0; i <= 11; ++i )
  {
    if ( *(char *)(v3[i % 3] + 2 * (i / 3)) - *(char *)(i + a1) != 1 )
      return 1LL;
  }
  return 0LL;
}
```
+ 关键代码是这一部分,if ( *(char *)(v3[i % 3] + 2 * (i / 3)) - *(char *)(i + a1) != 1 )

写成入能看懂的形式

if{*(char*)(a[x+y]-*(char*)b[z+q]}

*(char*)是解包输出当前地址内字符串的意思
第一部分简单来写就是a[x+y]
放在原题中就是说取v3这个数组的第i%3,2*(i/3)作为第一部分

这里用%交替取值确实有点意思,我倒是第一次见,以后应该还能碰到,先记着吧
取用户输入的字符串的第i项与第一部分相减

然后后续和总体的代码大概就是说
如果不等于1就执行下面的事情,就是返回1LL
它不是零值,所以显示flag错误,那么正确的flag应当是等于1的
字符串相减要求等于一就用ASCII码值进行计算
那就只需要将我们找到的前半部分的ASCII-1就能得到需要输入的字符串
也就是flag

仔细观察这道题的特征,计算量小,确定值难,我感觉是手算比写程序要简单,不知道以后会不会还有这种题目,估计也很少了,姑且先有这么一个意识吧
## 666
+ 关键内容就两段
```
int __cdecl main(int argc, const char **argv, const char **envp)
{
  char s; // [rsp+0h] [rbp-1E0h]
  char v5; // [rsp+F0h] [rbp-F0h]

  memset(&s, 0, 0x1EuLL);
  printf("Please Input Key: ", 0LL);
  __isoc99_scanf("%s", &v5);
  encode(&v5, &s);
  if ( strlen(&v5) == key )
  {
    if ( !strcmp(&s, enflag) )
      puts("You are Right");
    else
      puts("flag{This_1s_f4cker_flag}");
  }
  return 0;
}
```
```
int __fastcall encode(const char *a1, __int64 a2)
{
  char v3[32]; // [rsp+10h] [rbp-70h]
  char v4[32]; // [rsp+30h] [rbp-50h]
  char v5[40]; // [rsp+50h] [rbp-30h]
  int v6; // [rsp+78h] [rbp-8h]
  int i; // [rsp+7Ch] [rbp-4h]

  i = 0;
  v6 = 0;
  if ( strlen(a1) != key )
    return puts("Your Length is Wrong");
  for ( i = 0; i < key; i += 3 )
  {
    v5[i] = key ^ (a1[i] + 6);
    v4[i + 1] = (a1[i + 1] - 6) ^ key;
    v3[i + 2] = a1[i + 2] ^ 6 ^ key;
    *(_BYTE *)(a2 + i) = v5[i];
    *(_BYTE *)(a2 + i + 1LL) = v4[i + 1];
    *(_BYTE *)(a2 + i + 2LL) = v3[i + 2];
  }
  return a2;
}
```
+ 大概意思就是说让你输入一个v5,与key比较,不等长就结束,等长就把v5编码储存在s中,然后用s去和key比较,相同你就对了,不同就会出言耍弄你
### memset
void *memset(void *ptr, int value, size_t num)
将ptr指向的内存块的前num个字节设置成value的变量
此题为空,因为s只做储存使用(明明只设置就好了却要做这样的伪装么,有点意思)
### strcmp
int strcmp(const char *str1, const char *str2)
按字典顺序比较两个null结尾的字符串

str1 小于 str2则返回值小于零

str1 等于 str2则返回值等于零(所以那里的if里才要有个!把0换成1执行命令)

str1 大于 str2则返回值大于零

+ 所以接下来就是找数据,enflag=izwhroz"“w"v.K”.Ni
+ 接下来写个python逆向还原
程序中是每三位进行三次异或运算,所以直接设置步长总体加和拼接(byd原来异或优先级低于加减啊)
```
def encode(data,key):
    result=[]
    for i in range(0,key,3):
        enc1=data[i]
        enc2=data[i+1]
        enc3=data[i+2]
        char1=(ord(enc1)^key)-6
        char2=(ord(enc2)^key)+6
        char3=(ord(enc3)^key)^6
        result.extend([char1,char2,char3])
    return bytes(result)
enflag='izwhroz""w"v.K".Ni'
key=0x12
flag=encode(enflag,key)
print(flag) 
```
### ord(...)
将字符串转化为ascil码值
### chr(...)
将ascil码值转化为字符
## 好多水题
+ 为啥这些难度1的题难度会差这么多呢?
## reverse_re3
+ 搞了我最久的题目来了
+ 先看一眼main函数,短短几行,看着啥用都没有,只要一个被调取的函数在处理v4,进去看看
```
__int64 sub_940()
{
  int v0; // eax
  int v2; // [rsp+8h] [rbp-218h]
  int v3; // [rsp+Ch] [rbp-214h]
  char v4[520]; // [rsp+10h] [rbp-210h] BYREF
  unsigned __int64 v5; // [rsp+218h] [rbp-8h]

  v5 = __readfsqword(0x28u);
  v3 = 0;
  memset(v4, 0, 0x200uLL);
  _isoc99_scanf(&unk_1278, v4, v4);
  while ( 1 )
  {
    do
    {
      v2 = 0;
      sub_86C();
      v0 = v4[v3];
      if ( v0 == 100 )
      {
        v2 = sub_E23();
      }
      else if ( v0 > 100 )
      {
        if ( v0 == 115 )
        {
          v2 = sub_C5A();
        }
        else if ( v0 == 119 )
        {
          v2 = sub_A92();
        }
      }
      else
      {
        if ( v0 == 27 )
          return 0xFFFFFFFFLL;
        if ( v0 == 97 )
          v2 = sub_FEC();
      }
      ++v3;
    }
    while ( v2 != 1 );
    if ( dword_202AB0 == 2 )
      break;
    ++dword_202AB0;
  }
  puts("success! the flag is flag{md5(your input)}");
  return 1LL;
}
```
+ 怎么这么多条件判断?而且这代码怎么这么长,我能做?
+ 先问问ai大人怎么看吧
+ 好的,那么实际上这是一个迷宫类型的题目,识别出它的关键就在那很长的代码上,119,97,115,100其实就是wasd的ascil码值,这里就是个移动读取
+ 点击前面调取的函数
```
unsigned __int64 sub_86C()
{
  int i; // [rsp+0h] [rbp-10h]
  int j; // [rsp+4h] [rbp-Ch]
  unsigned __int64 v3; // [rsp+8h] [rbp-8h]

  v3 = __readfsqword(0x28u);
  for ( i = 0; i <= 14; ++i )
  {
    for ( j = 0; j <= 14; ++j )
    {
      if ( dword_202020[225 * dword_202AB0 + 15 * i + j] == 3 )
      {
        dword_202AB4 = i;
        dword_202AB8 = j;
        break;
      }
    }
  }
  return __readfsqword(0x28u) ^ v3;
}
```
+ 在这里找到了循环的边界,15次
+ 下面提到如果dword_202AB0[]中的某个值==3时循环结束，并将i，j的值分别赋给全局变量dword_202AB4，dword_202AB8
+ 好,那就去看看
+ 看集贸啊,不能是要我手打出来吧?没办法了,看看wp,不是哥们,你这怎么直接显示成这样啊?? 倒是解释一下怎么搞的啊
![alt text](3-1.png)
+ 看看其他人的吧
+ 不是你们怎么也是这种啊
+ 好,看来是时候让师傅发挥一下作用了!
+ "你不知道lazyIDA插件吗?"
## lazyIDA
https://blog.csdn.net/liKeQing1027520/article/details/137384900\
+ 哦吼?这么看来--确实挺不错的?
+ 看我也提取!!
+ 不是哥们你怎么装了没反应啊?😭
+ 只能去搜一下了
+ 于是我开始了长达一个半小时的修插件旅程
```
[notice] A new release of pip is available: 25.2 -> 25.3
[notice] To update, run: C:\Users\lTOOKI\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\python.exe -m pip install --upgrade pip
ERROR: Could not open requirements file: [Errno 2] No such file or directory: 'requirements.txt'
```
+ 按照教程一步步操作完还是没能解决
```
直接安装常用包（跳过requirements.txt）
bash
pip install requests numpy pandas
```
+ 嗯???难道说?
+ 什么?!我的pip居然差了一个版本?
+ 升级pip,一键安装,这下总没问题了吧
+ ...还是不对啊???
+ 手动去找一下那玩意吧
+ jm搜不到啊(bushi
```
4. 手动安装 LazyIDA 的依赖
根据 LazyIDA 的常见依赖，你可以手动安装：

bash
pip install PyQt5
pip install keystone-engine
pip install capstone
```
+ 什么?难道说??
+ ...这不还是毛用没有吗???
+ ................................................................................
+ 最后发现是python版本问题,而这个玩意我早在自己解决的第二步就想到了,并且重装了python,但是您猜怎么着?没重启,不生效!哈哈
+ 那现在总能愉快地做题了吧?
+ ...结果就是convert之后给我报出来一堆16进制数字
+ 呵呵,到此为止了么?
+ 就在此时,我的misc之魂突然觉醒,不就是数据处理吗?你连这都不会了?
+ 我直接打开word,将0x0替换为空
![alt text](image.png)
终于得到了完整的字符!
+ 我满心欢喜地写了一个代码,按照15*15排列,哼哼,这道题,不还是非常....
![alt text](image-1.png)
+ 不是哥们,这啥啊?我怎么不认识你啊😭
+ 我代码写错了???不可能啊!
+ 反复确认之后我开始翻wp找线索
#### 特别注意，dword_202020是dword类型，所以每4个为一组，只有第一个值是有效值，后面3个都是填充为0的。
+ 我弯了两个小时的腰终于断了
+ 呵呵,果然,没有掌握lazyIDA最终奥义的我,是不配觊觎这样的题目的啊
+ 真的已经......穷途末路了吗?已经,没有任何办法了吗?我真的要输给,难度1的题了吗?!!不!!!!!
+ 银瓶乍破水浆迸,铁骑突出刀枪鸣!!一道灵光闪过脑海!那不过是我在写代码搞哈纳伏打时偶然看到的一个小小的信息!!
+ 却在此刻,犹如命运的指引一般站在了我的脑海之中!!!这就是命运的指引啊!!!!
```
data=[...]
for i in range(0,len(data),4):
    print(data[i], end=',')
    if (i/4 + 1) % 15 == 0:
        print()
    if (i/4 + 1) % 225 == 0:
        print("------------")
```
+ 游戏结束
![alt text](image-2.png)
(知其燃而不知其所以燃)
+ ok,结局就是最后我才知道可以直接按shift+e然后选中variable就能得到处理好的数,我就像个艾斯比一样自顾自地燃了半天实际上就是在浪费时间
+ 是同学直接告诉我这个数据提取方法的,事实上,其实我现在也不会直接把迷宫数据在IDA内改成那样,除了提取简单数据之外的功能我也不会,网上根本没有那样的使用教程,ai把我搞了半天一点用的没有,事实和它教的东西完全不同,对大佬来说分明就打几个字的功夫,我到现在也不明白啊,此致,我想说的其实是,对于这样的弯路,真的没必要再让后人走一遍了,或许在得到很多知识后再去想通这件事会发现其实主线很简单,但难就难在支线太过繁复,所以,让谜语停下来,关爱飞舞新手
# 本周学习总结</font>
+ 做了九道题,装了个插件
+ 暂时觉得搁下python内容
+ 逆向要用的各种函数确实还是和开发学习内容大相径庭,目前代码确实还需要ai大人的帮助,各种编码函数也在一一学习,也不知道这日子啥时候是个头
# 杂项</font>
+ 成功找到不被谷歌封号的办法,可以使用更强大的ai了woc
+ 终于发现不是麦课佬的CTF教学up主了woc