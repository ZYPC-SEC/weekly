一、python

1、from Crypto.Util.number import*常用函数：

getPrime(bits, randfunc=None)：生成一个指定位数的随机素数。

参数 bits 指定了素数的位数。

参数 randfunc 是一个可选的随机数生成函数，默认为 Crypto.Random.get_random_bytes。

inverse(a, m)：计算 a 在模 m 下的模反元素。

要求 a 和 m 是互质的。

返回值是 a 在模 m 下的模反元素。

isPrime(n, k=10)：检测一个数是否为素数。

参数 n 是要检测的数。

参数 k 是进行 Miller-Rabin 素性测试的次数，默认为 10。

bytes_to_long(s)：将字节串转换为对应的长整数。

参数 s 是要转换的字节串。

返回值是转换后的长整数。

long_to_bytes(n)：将长整数转换为对应的字节串。

参数 n 是要转换的长整数。

返回值是转换后的字节串。

（模幂运算：给定三个整数a、b和n，计算a的b次方后对n取模的结果。表示为：c ≡ a^b (mod n)，其中c是a的b次方对n取模的结果。（应用：快速幂，在tip里面有用python实现快速幂的代码））

（模反元素：数论中的一个概念，也称为乘法逆元或倒数。给定一个整数 a 和一个模数 m，如果存在一个整数 b，使得 (a * b) % m = 1，则 b 称为 a 在模 m 下的模反元素。）

2、Bytes_to_long（将文字翻译为长整数）

3、以下是一些 gmpy2 常用函数：

整数函数：

gmpy2.add(x, y)：返回 x + y 的结果。

gmpy2.sub(x, y)：返回 x - y 的结果。

gmpy2.mul(x, y)：返回 x * y 的结果。

gmpy2.div(x, y)：返回 x // y 的结果，即整数除法。

gmpy2.pow(x, y)：返回 x ** y 的结果，即幂运算。

Gmpy2.pow(x,y,z):返回（x**y）%z的值。          （当然，我们可以直接调用pow()函数，但是通过gmpy库调用的pow函数计算精度更大一些）

特别地，它也可以计算模反元素，即：pow（x,-1,y）计算x在模数y下的模反元素。数学原理：扩展欧几里得算法。如果x，y不互质的话，会返回ValueError 异常

gmpy2.invert(x, y)：返回 x 在模数 y 下的模反元素。

gmpy2.gcd(x, y)：返回 x 和 y 的最大公约数。

gmpy2.is_prime(x)：判断 x 是否为素数。

浮点数函数：

gmpy2.mpfr(x)：将浮点数 x 转换为高精度浮点数对象。

gmpy2.add(x, y)：返回 x + y 的结果。

gmpy2.sub(x, y)：返回 x - y 的结果。

gmpy2.mul(x, y)：返回 x * y 的结果。

gmpy2.div(x, y)：返回 x / y 的结果。

gmpy2.iroot(n,t)：这个函数专门用来进行大数开根号，n就是大整数，t是你要开几次幂（用于计算两个素数很接近的情况）注意结果的形式：返回的是一个元组，第一个元素是开方结果，第二个元素是是否能整数开方即返回“true”or“false”，所以我们要是只要它的开放结果的话，需要这样的一个函数:temp=gmpy2.iroot(n,2)[0]

hashlib 是 Python 中用于进行哈希算法的标准库，提供了多种哈希算法的实现。下面是一些4、常用的 hashlib( Python 中用于进行哈希算法的标准库，提供了多种哈希算法的实现) 函数：

hashlib.md5(): 创建一个用于计算 MD5 哈希值的哈希对象。

hashlib.sha1(): 创建一个用于计算 SHA-1 哈希值的哈希对象。

hashlib.sha256(): 创建一个用于计算 SHA-256 哈希值的哈希对象。

hashlib.sha512(): 创建一个用于计算 SHA-512 哈希值的哈希对象。

hashlib.blake2b(): 创建一个用于计算 BLAKE2b 哈希值的哈希对象。

hashlib.blake2s(): 创建一个用于计算 BLAKE2s 哈希值的哈希对象。

这些函数返回的哈希对象可以用于对数据进行哈希计算。可以使用 update() 方法向哈希对象中添加数据，然后使用 hexdigest() 方法获取哈希值的十六进制表示。

例子：

import hashlib

data = b'Hello, world!'      （为什么加前缀b，详见tip）

hash_object = hashlib.sha256(data)

hex_digest = hash_object.hexdigest()

print(hex_digest)

5、SymPy是一个用于符号计算的Python库，它提供了许多功能和工具，用于处理符号表达式、代数运算、解析几何、微积分、方程求解、线性代数等方面的问题。以下是SymPy模块的一些主要功能和用途：

符号表达式：SymPy允许你创建符号变量，并使用这些符号变量进行符号计算。你可以定义代数表达式、多项式、有理函数等，并进行各种代数运算，如加法、减法、乘法、除法、幂运算等。

方程求解：SymPy提供了用于求解方程和方程组的函数。你可以使用sp.solve函数来解析代数方程和方程组，得到变量的解。SymPy还支持求解微分方程、差分方程和常微分方程等。

在使用 SymPy 求解符号方程组时，sp.solve() 函数无法直接处理包含非符号变量的方程组。对于这种情况，我们可以使用 sp.solvers.solve() 函数来解决。

Eg：sol = sp.solve((eq1, eq2), (p, q))（即：求解eq1=p，eq2=q两个方程联立起来的结果）

微积分：SymPy可以进行符号微积分运算，如求导、积分、极限、级数展开等。你可以使用sp.diff函数计算函数的导数，使用sp.integrate函数计算函数的积分。

线性代数：SymPy提供了用于处理线性代数问题的函数和工具。你可以进行矩阵运算、求解线性方程组、计算矩阵的特征值和特征向量、计算矩阵的逆等。

解析几何：SymPy支持解析几何计算，如点、直线、平面、曲线、圆、球等的表示和计算。你可以进行点的坐标计算、直线和平面的方程计算、曲线的参数化表示等。

绘图：SymPy可以生成数学表达式的图形，包括函数图像、曲线图、散点图等。你可以使用sp.plot函数绘制函数的图像，使用sp.plot_parametric函数绘制参数化曲线的图像。

符号化简：SymPy提供了符号化简的功能，可以对表达式进行代数化简、三角化简、指数化简等。你可以使用sp.simplify函数对表达式进行简化。

数值计算：虽然SymPy主要是一个符号计算库，但它也提供了一些数值计算的功能。你可以使用sp.N函数将符号表达式转换为数值，使用sp.evalf函数计算表达式的数值近似。

next_prime()：寻找比括号里数大的下一个质数

php 的内置函数 

数学相关函数

abs();  //求绝对值

ceil(); //向上取整 

floor(); // 向下取整

round() ;  //四舍五入

round(1.45) ;  默认只有一个参数时，返回的是整数，第二个参数表示保留小数点的位数

max() ;  // 返回最大值

min();   //返回最小值

rand() ;  // 生成随机数  0 - rand-max

rand(10,20) ;  //生成10-20之间的随机数

字符串相关函数

explode: 将字符串转成数组 

$arr = explode(" ",$str);

implode: 将数组转成字符串

lcfirst() : // 字符串首字母转成小写

ucfirst(): // 字符串首字母转成大写

strtolower();    // 字符串转成小写

strtoupper(); // 字符串转成大写

strlen() ; //字符串的长度

trim(); //去字符串首尾空格

查找字符串

strpos() -查找字符串在另一字符串中第一次出现的位置（区分大小写）

strripos() -查找字符串在另一字符串中最后一次出现的位置（不区分大小写）

strrpos() -查找字符串在另一字符串中最后一次出现的位置（区分大小写）

转换字符串

strtr(字符串,查询字符,转换的字符)

替换字符串

str_replace(查询字符,替换的字符, 字符串);

日期相关函数

time();  // 获取时间戳

date();  // 格式化时间 , date(format, timestamp) ; 

strtotime(); //字符串转成时间戳

数组相关的函数

array_keys()  // 获取数组的所有的键名

array_merge(); //数组的合并

array_pop(); //删除数组的最后一个元素

array_push(); //添加一个或多个在数组的最后

array_shift(); //删除数组的首个元素，并返回删除的元素

array_unique();  //删除数组中重复的值

count();  // 获取数组的长度

in_array(); //检查数组是否存在指定的值, 存在返回1

extract() ;  // 从数组中将变量导入到当前的符号表