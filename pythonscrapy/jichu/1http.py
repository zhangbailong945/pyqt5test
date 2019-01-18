'''
http协议是互联网里面最重要，最基础的协议之一
http请求报文介绍：
（1）、方法：GET/POST
GET获取远程服务器；/远程服务器的相对路径，这里是根目录
（2）、UUI：相对路径
（3）、HOST:目标主机
远程服务器的主机地址
（4）：Accept:可接受的媒体类型
客户端希望的连接处理方式;connection:希望连接继续保持，不要去关闭它
（5）：User-Agent:浏览器身份
（6）：gzip：表示我们可以接受这种亚索的媒体，压缩的媒体就可以建设
这个宽带的占用，可以提供传输的熟读
（7）：Accept-Language:接受的语言
Zh-CN

（8）：应答码
2xx :成功
200：ok
206：Partial content

3xx:重定向（客户端想要获取的资源，服务器告诉你，现在不在这了，你需要到另外的地方取
，301和303都表示要到另外的地方去取，会给你提供新的URL）
301 ：Moved Permanently
303 :See Other
304 :Not Modifide

4xx: 客户端错误（服务端会认为你客户端发的请求不对，比如说请求的格式不对，
或者参数不对之类的）
400：Not Found(你要请求的资源，在服务器上不存在)
500： 服务端错误
500：Interna Server Error
501:Not Implemented

2.Server:应答服务器
3.Content-Type:应答的数据类型
text/*
image/*
audio/*
Video/*
/
例如：Conent-Type:text/html;charset=utf-8


'''