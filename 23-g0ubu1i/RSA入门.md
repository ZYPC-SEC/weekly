# [RSA入门](https://github.com/ctf-wiki/ctf-wiki/blob/master/docs/zh/docs/crypto/asymmetric/rsa/rsa_theory.md#rsa-%E4%BB%8B%E7%BB%8D)

[TOC]



## 01.介绍：

RSA 加密算法是一种非对称加密算法。在公开密钥加密和电子商业中 RSA 被广泛使用。RSA 是 1977 年由罗纳德·李维斯特（Ron Rivest）、阿迪·萨莫尔（Adi Shamir）和伦纳德·阿德曼（Leonard Adleman）一起提出的。RSA 就是他们三人姓氏开头字母拼在一起组成的。

RSA 算法的可靠性由极大整数因数分解的难度决定。换言之，对一极大整数做因数分解愈困难，RSA 算法愈可靠。假如有人找到一种快速因数分解的算法的话，那么用 RSA 加密的信息的可靠性就肯定会极度下降。但找到这样的算法的可能性是非常小的。如今，只有短的 RSA 密钥才可能被强力方式解破。到 2017 年为止，还没有任何可靠的攻击 RSA 算法的方式。

## 02.RSA算法简介

### **公钥与私钥的产生：**

(1)进行加密之前，首先随机找出2个不同的大质数p和q,计算 $N = p \times q$

(2)根据欧拉函数,求得求得 $\varphi(N) = \varphi(p)\varphi(q) = (p - 1)(q - 1)$

(3)找出一个公钥e，e要满足: 1\<e\<φ(n) 的整数，且使e和φ(N)互质。

(4)根据e\*d除以φ(n)余数为1，找到私钥d。求得 $e$ 关于 $\varphi(N)$ 的模反元素，命名为 $d$(逆元) ，有 $ed \equiv 1(mod\varphi(N))$

\(5\) 将 $p$ 和 $q$ 的记录销毁

(6)所以,$(N,e)$ 是公钥，$(N,d)$ 是私钥。

### **消息加密:**

首先需要将消息以一个双方约定好的格式转化为一个小于 $\mathbf{N}$ ，且与 $\mathbf{N}$ 互质的整数 $\mathbf{m}_{\mathbf{\circ}}$ 如果消息太长，可以将消息分为几段，这也就是我们所说的块加密，后对于每一部分利用如下公式加密:

$$
m^{e} \equiv c\ \;(modN)
$$


### **消息解密:**

利用密钥 $d$ 进行解密。

$$
c^{d} \equiv m\ (modN)
$$

```
p 和 q ：大整数N的两个因子（factor）

N：大整数N，我们称之为模数（modulus

e 和 d：互为模反数的两个指数（exponent）

c 和 m：分别是密文和明文，这里一般指的是一个十进制的数
```

## 03.RSA算法原理

### 欧拉函数 $\varphi(N) $

定义：小于N的自然数中与N互质的数的个数

```
任何一个素数p的欧拉函数就是p-1

n的欧拉函数
phi = (p-1)(q-1)
```



### 欧拉定理

若n，a为正整数，且n，a互质，即 gcd ( n , a )=1 则：
$$
a^{\varphi(N)} \equiv 1\;(mod\;n)
$$

$$
即:a^{\varphi(N)}=1+kn \;\;\;(k为任意整数)
$$



### 费马小定理

费马小定理：

```
若p是质数，a与p互质，

a^p 
```

$$
a^p\equiv a\;(mod\;p)
$$

$$
即:a^p=a+kp
$$

$$
或:a^{\;p-1}\equiv1\;(mod\;p)
$$

$$
即:a^{p-1}=1+kp
$$

### 模运算

```
(a + b) % p = (a % p + b % p) % p
(a - b) % p = (a % p - b % p) % p
(a * b) % p = (a % p * b % p) % p
a ^ b % p = ((a % p) ^ b) % p
结合律
((a + b) % p + c) = (a + (b + c) % p) % p
((a * b) % p * c) = (a * (b * c) % p) % p
交换律
(a + b) % p = (b + a) % p
(a * b) % p = (b * a) % p
分配律
(a + b) % p = (a % p + b % p) % p
((a + b) % p * c) % p = ((a * c) % p + (b * c) % p
重要定理
若 a ≡ b (mod p)，则对于任意的 c，都有(a + c) ≡ (b + c) (mod p)
若 a ≡ b (mod p)，则对于任意的 c，都有(a * c) ≡ (b * c) (mod p)
若 a ≡ b (mod p)，c ≡ d (mod p)，则
(a + c) ≡ (b + d) (mod p)
(a - c) ≡ (b - d) (mod p)
(a * c) ≡ (b * d) (mod p)
(a / c) ≡ (b / d) (mod p) 
```

```
逆元
a mod p的逆元便是可以使 a * a' mod p = 1 的最小a'。
```

### RSA算法正确性的推导

```
式1：c=m^e%N
式2：m=c^d%N


将式1带入式2 得 m = (m ^ e % N ) ^ d % N

需要证明：m == ( m ^ e % N ) ^ d % N

(m^e%N)^d%N

=>  (m^e)^d%N #模运算 a ^ b % p = ((a % p) ^ b) % p

m^(e*d)%N #幂的乘方，底数不变，指数相乘
将 e * d ≡ 1 (mod φ(N)) 即 e * d = K * φ(N) + 1，K为任意正整数，代入得：



=> (m^(K*φ(N)+1))%N

=> (m^(K*φ(N)*m^1)%N # 同底数相乘，指数相加

=> (m^(K*φ(N)*m)%N

=> ((m^φ(N)^K%N*m)%N # 幂的乘方，底数不变，指数相乘

=> ((m^φ(N)^K%N*m%N)%N # (a * b) % p = (a % p * b % p) % p

=> ((m^φ(N)%N)^K%N*m%N)%N # a ^ b % p = ((a % p) ^ b) % p

=> (1^K%N*m%N)%N # 根据欧拉定理：a^φ(n)≡1 mod n 即 a^φ(n) mod n = 1

=> (m%N)%N # 1^K%N=1

=> (m%N)%N

=> (m%N)^1%N

=> (m^1)%N   # a ^ b % p = ((a % p) ^ b) % p

=> m%N

m  #因为 m < N 
```

## 04.随机生成flag

```python
import random
import hashlib
import string

#字符串列表
a=string.printable
#随机生成flag
for i in range(10):
    flag = ""
    for i in range(10):
        flag += a[random.randint(0, 99)]
    flag = hashlib.md5(flag.encode()).hexdigest()
    print("flag{" + flag + "}")


from uuid import uuid1
flag="flag{"+str(uuid1())+"}"
print(flag) 
```

![img](https://i0.hdslb.com/bfs/article/6bb7113e6f3e65e1f762f2565539c32563b340c1.png@902w_209h_progressive.webp)

## 05.一般出题脚本

```python
import libnum

from Crypto.Util.number import *
#生成随机素数
getPrime()

p=libnum.generate_prime(1024)
q=libnum.generate_prime(1024)
e=65537
m="flag{20d6e2da95dcc1fa5f5432a436c4be18}"
#字符串转数字
m=libnum.s2n(m)
m=bytes_to_long(m)

n=p*q
phi_n=(p-1)*(q-1)
#求逆元
d=libnum.invmod(e,phi_n)
d=inverse()
c=pow(m,e,n)


print("p=",p)
print("q=",q)
print ("n=",n)
print("d=",d)
print ("e=",e)
print ("c=",c) 
```



## 06.题型总结

### 已知n,d,e,c求m

```python
import libnum

n= 14685532699024100754723222996385121368294636639693750794149020559314539676501066491415844320990799035552463714403031072164829458702780715523923962246149328887690893262271480633736651143634392056066729487305166335857950659680699210683976952113003674104898343893168719508462975991580551696824510044412974267585312807460664570245139015568859112921920860421973308538800641652781742897528769692264955229878206911313791989518088100099218315995549914435278654377368771668058107642713121127495780090852489015591581414806590111818355121157794129813430710822697558144598815860067978324469091074823400715400666808772858128261149
d= 10655677501818714057545408290692306276248758047017058020876274084213258239416744966450976471246402284779991562186357882946337721435118045765127426899173581894141706933500094886492805160951008521020815528782559085235105783294876017603112074153984218299742602608478449101819428678878037976091306073545785820932796422483686522431260926680891531210950251782422010888047909274618007401655588566411972291526501884077240225819170340160706732901152519829956055255218835518533347875405883278225018714890042991619568316304958478955576005445279807142753050999269866987221510643119355301877102904394259290548609330522059178100989
e= 65537
c= 7937297427288435728721973474925856865675225171317301007619581716746999628275946964127516634203401830643076435690247635478297903236185011960902817030042080567027165802992734580344202744697251074454156026031417427325660809453340428989949816426637434868049018580855865080715251672252410696685286047485204432648545886024276695749435709592994477514818763551176789963387889424072650811645828675090859926233585219662579177051353763021116106877502871331756544361402971459889233069752657661921397258845893293005099736406362733668960163109452223071514272504206470939914043855546880424121530822318600645513435826636440478681928

m=pow(c, d, n)
print(libnum.n2s(m).decode()
```

### 已知p,q,e,c求m

```python
import libnum

p= 178974110759313878895493455207516672882434662571655460770401953730906926302476821805659378622536968418528094957044346203494793341636459433763427491907849563922785749794854266865548657682445692416895365631610849027415100889893466490767087266542637440212533807985124840688092762928583845838066174446047886496977
q= 93610871651220602641323046206103959524660743045950590135111801621145944725719667412027010040112514078098465817329474817485502356054795293086881519931215167856745860801666777619204160653243683622930567962804914581845602027547589056026105213437044768786486688576038889017989891165091320977401144724582916902269
e= 65537
c= 10505609204533893330224001468185225454647695615253006709365840521320011117703729471412769493857753605106376689659952882885215696765275778768339621441610719177208351696489476567331875339672513868473669863672226315682278831184868041476134806131989809014422520472566202048041013413698358733781909446846787304422628166599338803127610040714545537436536348608012176828441837378861024372912755344397449657260043057239911064546424582314518819235470388313710641962070846850292694572345451390561142917224092435026246696084949470913298543523893386679712766629009873176804118782436042080621119334193337953451160118095182279971122

n=p*q
phi_n=(p-1)*(q-1)

#求逆元
d=libnum.invmod(e,phi_n)

m=pow(c,d,n)
print(m)
#数字转字节，转字符串
print(libnum.n2s(int(m)).decode()
```

### 基于N分解的RSA题目

#### 1.在线查询分解网站

http://www.factordb.com/index.php

#### 2.使用yafu工具分解

下载地址：https://sourceforge.net/projects/yafu/



```
#以分解49为例
yafu-x64.exe factor(49)

#导入文件进行分解，主要注意文本结尾要换行！！！不然要报错
yafu-x64.exe "factor(@)" -batchfile 1.txt
```

#### 3.使用费马分解

网上找的脚本，p和q太接近



```python
def isqrt(n):
  x = n
  y = (x + n // x) // 2
  while y < x:
    x = y
    y = (x + n // x) // 2
  return x

def fermat(n, verbose=True):
    a = isqrt(n) # int(ceil(n**0.5))
    b2 = a*a - n
    b = isqrt(n) # int(b2**0.5)
    count = 0
    while b*b != b2:
        # if verbose:
        #     print('Trying: a=%s b2=%s b=%s' % (a, b2, b))
        a = a + 1
        b2 = a*a - n
        b = isqrt(b2) # int(b2**0.5)
        count += 1
    p=a+b
    q=a-b
    assert n == p * q
    # print('a=',a)
    # print('b=',b)
    # print('p=',p)
    # print('q=',q)
    # print('pq=',p*q)
    return p, q
fermat(n)
```

#### 4.分解出来后，用脚本解密即可

```
import gmpy2
import libnum

p=
q=
e=
c=

n=p*q
phi_n=(p-1)*(q-1)

#求逆元
#d=libnum.invmod(e,phi_n)
d=gmpy2.invert(e,phi_n)

m=pow(c,d,n)
print(m)
print(libnum.n2s(int(m)).decode())
```

#### 出题脚本

```
p,q接近，很快就能分解
import libnum
import gmpy2

p=libnum.generate_prime(1024)
#下一个素数
q=gmpy2.next_prime(p)
print(p)
print(q)
print(gmpy2.is_prime(q))
e=65537
m="flag{20d6e2da95dcc1fa5f5432a436c4be18}"
m=libnum.s2n(m)
n=p*q
phi_n=(p-1)*(q-1)
d=libnum.invmod(e,phi_n)
c=pow(m,e,n)

print("n=",n)
print ("e=",e)
print ("c=",c) 
```

#### 解题脚本

```python
import  gmpy2
import libnum

def isqrt(n):
  x = n
  y = (x + n // x) // 2
  while y < x:
    x = y
    y = (x + n // x) // 2
  return x

def fermat(n, verbose=True):
    a = isqrt(n) # int(ceil(n**0.5))
    b2 = a*a - n
    b = isqrt(n) # int(b2**0.5)
    count = 0
    while b*b != b2:
        # if verbose:
        #     print('Trying: a=%s b2=%s b=%s' % (a, b2, b))
        a = a + 1
        b2 = a*a - n
        b = isqrt(b2) # int(b2**0.5)
        count += 1
    p=a+b
    q=a-b
    assert n == p * q
    # print('a=',a)
    # print('b=',b)
    print('p=',p)
    print('q=',q)
    # print('pq=',p*q)
    return p, q
n= 11236396438945464079176717143196471087880430124798640194523124584883161483744355761881720924798661332027501424643154414538029585287580122761405974427818841257794157497994556608202723391478027760181705924317533420305444809223444128034654367210331137068958693840582892819495487826045956577156074156668942232139402108462349340352898572481115406698318121299787982873916502591396884489682255184448165523604671743400422220149772905676655777228607948091675612455989601008858361759327370403306760674195506394280387024357322586732298060169962426894360775981877169895632927906390632063530920611197753716095903307467004289983267
e= 65537
c= 4260482466101011731957430920901406417434306478040387371588613512063428441001754753741853444857207349755032658064826592770143368278573527632514794087007140974732031358793249329430363014561312271335226315065519570861993052432656879088776144909638480994662696119431870831156129142403063675855781198930583825083362703887688501680905266707624440432914989795886392952354713859444836529227033324455920455610359249535012999943891644938239837207994673190694512955995798836266797112432609992164908679997257920566918693544746179908166741635316261624634351348613130319346356388546672516037747806222134853885202448682842353199133
pq=fermat(n)
p=pq[0]
q=pq[1]
phi_n=(p-1)*(q-1)
#求逆元
#d=libnum.invmod(e,phi_n)
d=gmpy2.invert(e,phi_n)
m=pow(c,d,n)
print(m)
print(libnum.n2s(int(m)).decode()) 
```

### RSA密钥生成与读取

**安装pycryptodome模块**

#### 公钥生成

```python
from Crypto.PublicKey import RSA

p= 787228223375328491232514653709
q= 814212346998672554509751911073
n= 640970939378021470187479083920100737340912672709639557619757
d= 590103645243332826117029128695341159496883001869370080307201
e= 65537


rsa_components = (n, e)
keypair = RSA.construct(rsa_components)
with open('pubckey.pem', 'wb') as f :
    f.write(keypair.exportKey())
```

#### 私钥生成

```python
from Crypto.PublicKey import RSA

p= 787228223375328491232514653709
q= 814212346998672554509751911073
n= 640970939378021470187479083920100737340912672709639557619757
d= 590103645243332826117029128695341159496883001869370080307201
e= 65537


rsa_components = (n,e,d,p,q)
keypair = RSA.construct(rsa_components)
with open('private1.pem', 'wb') as f :
    f.write(keypair.exportKey())
```

#### 公钥读取

```python
from Crypto.PublicKey import RSA
with open("pubckey.pem","rb") as f:
    key = RSA.import_key(f.read())
    print('n = %d' % key.n)
    print('e = %d' % key.e)
```

#### 私钥读取

```python
from Crypto.PublicKey import RSA
with open("private1.pem","rb") as f:
    key = RSA.import_key(f.read())
    print('n = %d' % key.n)
    print('e = %d' % key.e)
    print('d = %d' % key.d)
    print('p = %d' % key.p)
    print('q = %d' % key.q)
```

#### 出题脚本 -基于N分解的题目

```python
import libnum
import gmpy2
from Crypto.PublicKey import RSA

p=libnum.generate_prime(1024)
#下一个素数
q=int(gmpy2.next_prime(p))
e=65537
m="flag{a272722c1db834353ea3ce1d9c71feca}"
m=libnum.s2n(m)
n=p*q
c=pow(m,e,n)
flag_c=libnum.n2s(c)
rsa_components = (n, e)
keypair = RSA.construct(rsa_components)
with open('pubckey1.pem', 'wb') as f :
    f.write(keypair.exportKey())
with open("flag.txt","wb") as f:
    f.write(flag_c) 
```

#### 解题脚本

```python
import libnum
import gmpy2
from Crypto.PublicKey import RSA


def isqrt(n):
  x = n
  y = (x + n // x) // 2
  while y < x:
    x = y
    y = (x + n // x) // 2
  return x

def fermat(n, verbose=True):
    a = isqrt(n) # int(ceil(n**0.5))
    b2 = a*a - n
    b = isqrt(n) # int(b2**0.5)
    count = 0
    while b*b != b2:
        # if verbose:
        #     print('Trying: a=%s b2=%s b=%s' % (a, b2, b))
        a = a + 1
        b2 = a*a - n
        b = isqrt(b2) # int(b2**0.5)
        count += 1
    p=a+b
    q=a-b
    assert n == p * q
    # print('a=',a)
    # print('b=',b)
    # print('p=',p)
    # print('q=',q)
    # print('pq=',p*q)
    return p, q


with open("pubckey1.pem","rb") as f:
    key = RSA.import_key(f.read())
    n=key.n
    e=key.e

with open("flag.txt","rb") as f:
    c=f.read()
    c=libnum.s2n(c)

#费马分解,
n1=fermat(n)
p=n1[0]
q=n1[1]
phi_n=(p-1)*(q-1)
#求逆元
d=libnum.invmod(e,phi_n)
m=pow(c,d,n)
print(m)
print(libnum.n2s(int(m)).decode()) 
```

#### 进阶——自动生成密钥及加解密

```python
from Crypto.Cipher import PKCS1_v1_5
from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


random_generator = Random.new().read
rsa = RSA.generate(2048, random_generator)
# 生成私钥
private_key = rsa.exportKey()
# print(private_key.decode('utf-8'))
with open('rsa_private_key.pem', 'wb')as f:
    f.write(private_key)
# 生成公钥
public_key = rsa.publickey().exportKey()
# print(public_key.decode('utf-8'))
with open('rsa_public_key.pem', 'wb')as f:
    f.write(public_key)


#测试用密钥加密
public_key = RSA.importKey(public_key)
msg='flag'
pk = PKCS1_v1_5.new(public_key)
encrypt_text = pk.encrypt(msg.encode())
print(encrypt_text)

#测试密钥解密
private_key = RSA.importKey(private_key)
pk = PKCS1_v1_5.new(private_key)
msg = pk.decrypt(encrypt_text,0)
print(msg)


#两种标准
rsa_components = (n, e, int(d), p, q)
arsa = RSA.construct(rsa_components)
rsakey = RSA.importKey(arsa.exportKey())
rsakey = PKCS1_OAEP.new(rsakey)
decrypted = rsakey.decrypt(c)
print(decrypted) 
```

### 共享素数

解题脚本

```python
from Crypto.Util.number import *
from gmpy2 import *

n1 = ···
n2 = ···
e = 65537
c = ···

p = gmpy2.gcd(n1,n2)
q1 = n1 // p
q2 = n2 // p
phi1 = (p-1)*(q1-1)
phi2 = (p-1)*(q2-1)
d1 = gmpy2.invert(e,phi1)
d2 = gmpy2.invert(e,phi2)
m = pow(c,d2,n2)
m = pow(m,d1,n1)
print(long_to_bytes(m))
```

### 共模攻击

#### e1与e2互质

解题脚本

```python
from Crypto.Util.number import *
from gmpy2 import *

n1 = ```
e1 = ```

n2 = ```
e2 = ```

c1=```
c2=```

s,s1,s2 = gmpy2.gcdext(e1,e2)

m=(pow(c1,s1,n1)*pow(c2,s2,n1))%n1

print(long_to_bytes(m))
```

#### e1与e2不互质

解题脚本 

```python
from Crypto.Util.number import *
from gmpy2 import *
n= ……
c1= ……
c2= ……
e1=55
e2=200

g,x,y=gmpy2.gcdext(e1,e2)
m1=pow(c1,x,n)*pow(c2,y,n)%n
x = gmpy2.gcd(e1,e2)
k = 0
while 1:
    m11 = m1 + k*n
    m,s = gmpy2.iroot(m11,x)
    if s:
        print(long_to_bytes(m))
        break
    k += 1
```



### 低加密指数

解题脚本

```python
from gmpy2 import*
from Crypto.Util.number import*
from libnum import*

e=9

def CRT(a,n):
    sum = 0
    N = reduce(lambda x,y:x*y,n)   # ni 的乘积,N=n1*n2*n3

    for n_i, a_i in zip(n,a):    # zip()将对象打包成元组
        N_i = N // n_i           #Mi=M/ni
        sum += a_i*N_i*gmpy2.invert(N_i,n_i)   #sum=C1M1y1+C2M2y2+C3M3y3
    return sum % N 

n = [···]
c = [···]
x = CRT(c,n)

m = gmpy2.iroot(x,e)[0]
print(n2s(int(m)))
```

### 低解密指数

当e非常大时，d会很小，维纳攻击，涉及数论的勒让德定理https://www.cnblogs.com/yuanzhimengbian/p/15876619.html

```python
def RSA_wiener (n,e,c):
    #连分数逼近，并列出逼近过程中的分子与分母
    def lian_fen(x,y):
        res = []
        while y:
            res.append(x//y)
            x,y = y,x%y
        resu = []
        for j in range(len(res)):
            a,b = 1,0
            for i in res[j::-1]:
                b,a = a,a*i+b
            resu.append((a,b))
        if resu[0] == (0,1):
            resu.remove((0,1))
        return resu[:-1]
    lianfen = lian_fen(e,n)
    def get_pq(a,b,c):
        par = isqrt((n-phi+1)**2-4*n)
        x1,x2 = (-b + par) // (2 * a), (-b - par) // (2 * a)
        return x1,x2
    for (k,d) in lianfen:
        phi = (e*d-1)//k
        p,q = get_pq(1,n-phi+1,n)
        if p*q == n:
            p,q = abs(int(p)),abs(int(q))
            d = invert(e,(p-1)*(q-1))
            break
    return long_to_bytes(pow(c,d,n))
```



### 小明文

```python

```

### dp泄露

出题脚本



解题脚本

```python
import gmpy2 as gp

e = 
n = 
dp = 
c = 

for x in range(1, e):
	if(e*dp%x==1):
		p=(e*dp-1)//x+1
		if(n%p!=0):
			continue
		q=n//p
		phin=(p-1)*(q-1)
		d=gp.invert(e, phin)
		m=gp.powmod(c, d, n)
		if(len(hex(m)[2:])%2==1):
			continue
		print('--------------')
		print(m)
		print(hex(m)[2:])
		print(bytes.fromhex(hex(m)[2:]))
```

### 二次剩余

```python
from Crypto.Util.number import *
n = ...
r = ...
a = ...
c = ...
e = 65537
""" R.<x> = PolynomialRing(Zmod(r))
f = (x^2) -a
ans = f.roots()
p,s = ans[0]
print(p) """
p = ...
q = n //p
phi = (p-1)*(q-1)
d = inverse(e,phi)
m = pow(c,d,n)
print(long_to_bytes(m))
```

### P高位泄露

```python
from Crypto.Util.number import *
P = ...
n = ...
kbits = 340
p_fake = P << kbits
pbits = p_fake.nbits()
pbar = p_fake & (2^pbits-2^kbits)
print ("upper %d bits (of %d bits) is given" % (pbits-kbits, pbits))

PR.<x> = PolynomialRing(Zmod(n))
f = x + pbar
x0 = f.small_roots(X=2^kbits, beta=0.4)[0]  # find root < 2^kbits with factor >= n^0.3
p = x0 + pbar
print(p)
```

### e与phi不互素

解题脚本

```python
from Crypto.Util.number import *
from gmpy2 import *
p= 86053582917386343422567174764040471033234388106968488834872953625339458483149
q= 72031998384560188060716696553519973198388628004850270102102972862328770104493
c= 3939634105073614197573473825268995321781553470182462454724181094897309933627076266632153551522332244941496491385911139566998817961371516587764621395810123
e = 74
phi = (p-1)*(q-1)
g = GCD(e,phi)
d = inverse(e//g,phi)
m = pow(c,d,p*q)
m = gmpy2.iroot(m,g)[0]
print(long_to_bytes(m))
```

