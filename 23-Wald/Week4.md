这周比较忙，只浅学了一下签名校验方面的知识

# 签名校验之java层:

自己的理解：

我们在对安卓应用修改后必须得重签名才能继续安装，而为了应用不被篡改，开发者们通常会添加一些签名校验来比较前后签名作为保护手段，使篡改者们即使篡改安装了应用也无法正常使用。

我见过的签名校验更多的是java层的签名校验

举个例子，这是我从 懂球帝 里面抠出来的签名校验部分

```java
public static boolean checkSignature(Context context, String str) {
        Signature[] appSignatures;
        Signature[] apkSignatures = getApkSignatures(context, str);
        if (apkSignatures == null || (appSignatures = getAppSignatures(context)) == null) {
            return true;
        }
        int length = appSignatures.length;
        for (int i = POS_0; i < length; i += POS_1) {
            Signature signature = appSignatures[i];
            int length2 = apkSignatures.length;
            for (int i2 = POS_0; i2 < length2; i2 += POS_1) {
                if (signature.equals(apkSignatures[i2])) {
                    return true;
                }
            }
        }
        return false;
    }

```

`getApkSignatures`：获取的是apk包含的签名，在安装的时候作为是否能够安装的依据

`getAppSignatures`：获取的是应用信息签名，也就是开发者提供的签名，是程序安装后生成的签名

上面的签名校验逻辑就是比较了APP签名和APK签名，不一样就返回false，当然，这是最最简单的签名校验了，安全性也是最低的







## 绕过手段:

手撕法：

1.反编译apk后找到函数调用处删掉调用那一行即可，一般看的时候都用jadx转java方便看，改的时候就要去smail里面改

2.用开源的signaturekiller的java文件直接添加到对应dex里，然后把包名和应用原签名填进去就可以了



工具法：MT,NP,lsp,eirv,Modex乱杀



还有一些是校验签名的MD5，也可以直接改if的判断行实现绕过









如果是dex CRC 校验呢？反编译apk，dex里面搜`>signatures`可以过滤一些系统的signatures代码，在搜索到的java文件中定位CRC，然后可以清楚的看见下方有原CRC，如果签名的crc和原crc不一样就是篡改，这直接改成自己签名的crc32就行了（具体的CRC可以在APKanalyzer里看见，MT也行）

# 签名校验之Native层：

如果把校验加到so，就很难删除绕过了，所以so校验是目前大多数应用的签名校验方式，也是大多数过签工具无法处理的情况，以下是一个简单例子

![img](C:\Users\Lenovo\Desktop\18192692-d00f17f858d81fbf.webp)

## 绕过手段：

我在一个帖子里面看到一个很妙的绕过手段

首先把应用包里的META-INF文件夹下的签名文件复制出来一份，等会用来

用HEX工具查有4D 45 54 41 2D 49 4E 46（META-INF）的so文件，然后把他改成自己想改的文件夹的名字，比如TEHX-INF

然后把刚才复制出来的那个文件夹名字改成TEHX-INF，然后重新签名apk，这样我们的签名就在META-INF里面，而他会去校验TEHX-INF里面正确的签名，这样也就实现了绕过





还有一种，是在程序入口处会直接System.Loadlibrary("...so"),一般这种也可能是有校验的，直接把他调用so那一行删了试试？如果闪退就另寻他法



最好用的方法：去开发者家严刑拷打拿到 `.jks` 文件和密码:joy_cat:







# 自己的思考:

我们如何确保自己的应用不被篡改，签名校验是一个很好的方式，只是看怎么去用。那如果让我去设计一个签名校验逻辑，我会去先让篡改的人难受一波，先和谐工具，让你去手撕。当工具都过不去的时候，大部分的人都已经准备放弃了，殊不知工具是死的，人是活的

以mt为例，我在代码中直接检测他过签包里的类bin.mt.signature.KillerApplication存不存在就可以防他过签名了，其他工具同理，一步一步把工具都和谐了，再加一点自己的保护思路，对那些篡改者是不是就很困难了呢？

