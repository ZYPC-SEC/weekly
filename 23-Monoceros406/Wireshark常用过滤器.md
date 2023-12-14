---
title: Wireshark常用过滤器
date: 2023-11-28 13:33:13
tags: Wireshark
mathjax: true
---

# Wireshark常用过滤器

## http

```bash
 http
 http.request.method == "GET"
 http.request.method == "POST"
 http.host matches "www.baidu.com|baidu.cn" #可以多个
 http.host contains "www.baidu.com" #只能一个
 http contains "GET" #可以为"Host:" "User-Agent:" "Content-Type:" "HTTP/1.1 200 OK"等
```

## tcp

```bash
tcp
tcp.steam eq 0
tcp.port == 80
tcp.port >= 80
tcp.dstport == 80
tcp.srcport == 80
```

## udp

```bash
udp
udp.port == 80
```

## ip

```bash
ip.addr=192.168.1.1 #只显示源/目的IP为192.168.1.1的数据包
not ip.src=1.1.1.1 #不显示源IP为1.1.1.1的数据包
ip.src==1.1.1.1 or ip.dst==1.1.1.2 #只显示源IP为1.1.1.1或目的IP为1.1.1.2的数据包
```

## eth

```bash
eth.dst == A0:00:00:04:C5:84
eth.src == A0:00:00:04:C5:84
eth.addr == A0:00:00:04:C5:84 #源MAC和目标MAC都等于
```

