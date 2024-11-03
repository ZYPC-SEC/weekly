# 上周总结
- 把ssti注入的方法了解了并试着把基础题做了
- 收集了flask session伪造的脚本并尝试做题
- 收集了PIN码计算脚本并学习了其使用方法和原理同时完成了个基础题
- 搭建了Ubuntu虚拟机
- 尝试在服务器搭建gzctf平台失败，选择的系统版本不太方便操作
# 本周任务
## js原型链污染
### hgame-webvpn
查看主源码
```json
const express = require("express");
const axios = require("axios");
const bodyParser = require("body-parser");
const path = require("path");
const fs = require("fs");
const { v4: uuidv4 } = require("uuid");
const session = require("express-session");

const app = express();
const port = 3000;
const session_name = "my-webvpn-session-id-" + uuidv4().toString();

app.set("view engine", "pug");
app.set("trust proxy", false);
app.use(express.static(path.join(__dirname, "public")));
app.use(
session({
  name: session_name,
  secret: uuidv4().toString(),
  secure: false,
  resave: false,
  saveUninitialized: true,
})
);
app.use(bodyParser.json());
var userStorage = {
  username: {
    password: "password",
    info: {
    age: 18,
  },
  strategy: {
    "baidu.com": true,
    "google.com": false,
  },
  },
};

function update(dst, src) {
  for (key in src) {
  if (key.indexOf("__") != -1) {
  continue;
}
if (typeof src[key] == "object" && dst[key] !== undefined) {
  update(dst[key], src[key]);
  continue;
}
dst[key] = src[key];
}
}

app.use("/proxy", async (req, res) => {
  const { username } = req.session;
if (!username) {
  res.sendStatus(403);
}

let url = (() => {
  try {
  return new URL(req.query.url);
} catch {
  res.status(400);
  res.end("invalid url.");
  return undefined;
}
})();

if (!url) return;

if (!userStorage[username].strategy[url.hostname]) {
  res.status(400);
  res.end("your url is not allowed.");
}

try {
  const headers = req.headers;
  headers.host = url.host;
  headers.cookie = headers.cookie.split(";").forEach((cookie) => {
  var filtered_cookie = "";
  const [key, value] = cookie.split("=", 1);
  if (key.trim() !== session_name) {
  filtered_cookie += `${key}=${value};`;
}
return filtered_cookie;
});
const remote_res = await (() => {
  if (req.method == "POST") {
  return axios.post(url, req.body, {
  headers: headers,
});
} else if (req.method == "GET") {
  return axios.get(url, {
  headers: headers,
});
} else {
  res.status(405);
  res.end("method not allowed.");
  return;
}
})();
res.status(remote_res.status);
res.header(remote_res.headers);
res.write(remote_res.data);
} catch (e) {
  res.status(500);
  res.end("unreachable url.");
}
});

app.post("/user/login", (req, res) => {
  const { username, password } = req.body;
if (
typeof username != "string" ||
typeof password != "string" ||
!username ||
!password
) {
  res.status(400);
  res.end("invalid username or password");
  return;
}
if (!userStorage[username]) {
  res.status(403);
  res.end("invalid username or password");
  return;
}
if (userStorage[username].password !== password) {
    res.status(403);
    res.end("invalid username or password");
    return;
  }
  req.session.username = username;
  res.send("login success");
});

// under development
app.post("/user/info", (req, res) => {
  if (!req.session.username) {
    res.sendStatus(403);
  }
  update(userStorage[req.session.username].info, req.body);
  res.sendStatus(200);
});

app.get("/home", (req, res) => {
  if (!req.session.username) {
    res.sendStatus(403);
    return;
  }
  res.render("home", {
    username: req.session.username,
    strategy: ((list)=>{
      var result = [];
      for (var key in list) {
        result.push({host: key, allow: list[key]});
      }
      return result;
    })(userStorage[req.session.username].strategy),
  });
});

// demo service behind webvpn
app.get("/flag", (req, res) => {
  if (
    req.headers.host != "127.0.0.1:3000" ||
    req.hostname != "127.0.0.1" ||
    req.ip != "127.0.0.1" 
  ) {
    res.sendStatus(400);
    return;
  }
  const data = fs.readFileSync("/flag");
  res.send(data);
});

app.listen(port, '0.0.0.0', () => {
  console.log(`app listen on ${port}`);
});

```
```javascript
// under development
app.post("/user/info", (req, res) => {
  if (!req.session.username) {
    res.sendStatus(403);
  }
  update(userStorage[req.session.username].info, req.body);
  res.sendStatus(200);
});
```
在/user/info这个路由中，有可控制点，这句
`update(userStorage[req.session.username].info, req.body);`
接收req.body（请求数据） → userStorage.username.info
```json
app.use(bodyParser.json());
var userStorage = {
  username: {
    password: "password",
    info: {
      age: 18,
    },
    strategy: {
      "baidu.com": true,
      "google.com": false,
    },
  },
};
```
将数据就要污染到这个strategy中
> 对象.__proto__=构造函数.prototype
> js中的类是通过函数实现的(伪类)

```json
function update(dst, src) {
  for (key in src) {
    if (key.indexOf("__") != -1) {
      continue;
    }
    if (typeof src[key] == "object" && dst[key] !== undefined) {
      update(dst[key], src[key]);
      continue;
    }
    dst[key] = src[key];
  }
}
```
> 对象.__proton__—>构造方法(constructor).prototype—>构造函数的原型上层

本题的构造方法(constructor)为userStorage
而上述代码中的这句
`if (key.indexOf("__") != -1) {`
把___过滤了，相当于把__proto__过滤了
```javascript
app.get("/home", (req, res) => {
  if (!req.session.username) {
    res.sendStatus(403);
    return;
  }
  res.render("home", {
    username: req.session.username,
    strategy: ((list)=>{
      var result = [];
      for (var key in list) {
        result.push({host: key, allow: list[key]});
      }
      return result;
    })(userStorage[req.session.username].strategy),
  });
});
```
userStorage.username.info.constructor.prototype=object  
要把127.0.0.1污染到strategy中
通过constructor->prototype的方法调用它的object，污染strategy
所以exp如下
```json
{
    "constructor":{
        "prototype":{
            "127.0.0.1":true       
        }
    }
}
```
```javascript
// demo service behind webvpn
app.get("/flag", (req, res) => {
  if (
    req.headers.host != "127.0.0.1:3000" ||
    req.hostname != "127.0.0.1" ||
    req.ip != "127.0.0.1" 
  ) {
    res.sendStatus(400);
    return;
  }
  const data = fs.readFileSync("/flag");
  res.send(data);
});

app.listen(port, '0.0.0.0', () => {
  console.log(`app listen on ${port}`);
});
```
最后是web服务在3000端口读flag
### VCTF-hackjs
```javascript
const express = require('express')
const fs = require('fs')
var bodyParser = require('body-parser');
const app = express()
app.use(bodyParser.urlencoded({
    extended: true
}));
app.use(bodyParser.json());

app.post('/plz', (req, res) => {

    venom = req.body.venom

    if (Object.keys(venom).length < 3 && venom.welcome == 159753) {
        try {
            if(venom.hasOwnProperty("text")){
                res.send(venom.text)
            }else{
                res.send("no text detected")
            }
        } catch {
            if (venom.text=="flag") {
                let flag=fs.readFileSync("/flag");
                res.send("Congratulations:"+flag);
            } else {
                res.end("Nothing here!")
            }
        }
    } else {
        res.end("happy game");
    }
})



app.get('/',
function(req, res, next) {
    res.send('<title>oldjs</title><a>Hack me plz</a><br><form action="/plz" method="POST">text:<input type="text" name="venom[text]" value="ezjs"><input type="submit" value="Hack"></form>  ');
});

app.listen(80, () => {
  console.log(`listening at port 80`)
})
```
主要部分
```json
app.post('/plz', (req, res) => {

    venom = req.body.venom

    if (Object.keys(venom).length < 3 && venom.welcome == 159753) {
        try {
            if(venom.hasOwnProperty("text")){
                res.send(venom.text)
            }else{
                res.send("no text detected")
            }
        } catch {
            if (venom.text=="flag") {
                let flag=fs.readFileSync("/flag");
                res.send("Congratulations:"+flag);
            } else {
                res.end("Nothing here!")
            }
        }
    } else {
        res.end("happy game");
    }
})
```
对/plz这个路由
`venom = req.body.venom`
提取请求中的venom的body
```json
if (Object.keys(venom).length < 3 && venom.welcome == 159753) {
  
} else {
        res.end("happy game");
    }
```
然后检查venom的数量是否小于3个并且venom的welcome属性的值为159753不是就输出happy game
![bf5769564f02aca0e5769cbcec9099e5.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1710593675256-35a4f49e-81c0-40d5-bb68-fec882f9e69b.png#averageHue=%23faf9f9&clientId=u1761cc94-bd76-4&from=paste&height=234&id=uff384156&originHeight=292&originWidth=631&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=12327&status=done&style=none&taskId=udd45cbcf-f070-4a00-9f26-9c0ea3bbf70&title=&width=504.8)
![e8ab6512991c6fe3ff20eb9f1ad1ad27.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1710593695373-7b25eeec-6d44-4881-a9b1-3551c9e94f20.png#averageHue=%23fbfaf9&clientId=u1761cc94-bd76-4&from=paste&height=233&id=uf9fffe46&originHeight=291&originWidth=641&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=11991&status=done&style=none&taskId=u31adb242-07d8-4082-abb2-6be55ada70b&title=&width=512.8)
![070126fcac3b8e0a5a8b2f1e69cda873.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1710593707525-54028f43-6775-4717-8e4f-2ee6e5f0ed9f.png#averageHue=%23fbfaf9&clientId=u1761cc94-bd76-4&from=paste&height=253&id=u86220084&originHeight=316&originWidth=698&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=13173&status=done&style=none&taskId=u00951ab2-b848-4df1-852a-de6f9fcdb65&title=&width=558.4)
```json
if(venom.hasOwnProperty("text")){
                res.send(venom.text)
            }else{
                res.send("no text detected")
            }
```
检查venom有没有text属性，没有则输出no text detected
![e8fcdbce1b4d82139bee248b9bd1124d.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1710593716731-a90e0340-9da3-48ca-87a1-c92ef179c04b.png#averageHue=%23fbfaf9&clientId=u1761cc94-bd76-4&from=paste&height=246&id=uc94eb39d&originHeight=307&originWidth=711&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=13389&status=done&style=none&taskId=u3ef4d65b-0b86-4b49-9a6b-8d6d084aa16&title=&width=568.8)
```json
if (venom.text=="flag") {
                let flag=fs.readFileSync("/flag");
                res.send("Congratulations:"+flag);
            } else {
                res.end("Nothing here!")
            }
```
检查venom的text属性的值是否为flag，是则让flag变成/flag文件的内容输出Congratulations:"+flag否则输出Nothing here!
上述两段代码又由try catch连接
当try中的语句错误时才会执行catch的语句
思路到上面为止
后来群里出题人给了原型漏洞
[https://github.com/n8tz/CVE-2022-24999](https://github.com/n8tz/CVE-2022-24999)
```json
venom[__proto__][welcome]=159753&venom[hasOwnProperty]=Jay17&venom[text]=flag
```
> 解释一下：
> venom[__proto__][welcome]=159753：这一部分试图修改venom对象的原型（即venom对象的__proto__属性指向的对象）上的welcome属性。在JavaScript中，所有的对象默认继承自Object.prototype，除非明确地改变了对象的原型链。通过设置venom[__proto__][welcome]=159753，它实际上是在所有对象的原型上设置了welcome属性的值为159753，因为__proto__是指向对象原型的引用。
> venom[hasOwnProperty]=Jay17：这部分将venom对象的hasOwnProperty属性设置为字符串"flag"。正常情况下，hasOwnProperty是一个继承自Object.prototype的方法，用于检查对象是否拥有特定的自有属性。通过将它设置为一个字符串，venom.hasOwnProperty("text")的调用将会失败，因为hasOwnProperty已不再是一个函数。所以进入catch块
> venom[text]=flag：这部分设置venom对象的text属性为字符串"flag"。
> 现在，让我们回到原始的服务器端代码逻辑，看看为什么这个传参能够导致输出flag：
> 服务器期望venom对象有一个welcome属性，其值为159753，而这已经通过原型污染在所有对象上设置了。
> 服务器代码检查venom.hasOwnProperty("text")，这个调用会失败（抛出异常）因为hasOwnProperty已被覆盖为一个非函数值，这使得执行流进入到catch块。
> 在catch块中，代码检查venom.text=="flag"，这个条件为真，因为venom的text属性已经被设置为"flag"。
> 因此，满足了输出flag的条件。


