'''
cookie的格式：
1.客户端发送cookie:
Cookie:key1=value1;key2=value2;key3=value3

2.服务器端保存cookie时:
Set-cookie:key1=value1;path=/;domain=xxx

cookie属性:
1.domain和path:定义cookie的作用域，当指定domain时，这个domain及其子域名都会包含这个cookie.
2.Expires:定义cookie的生命周期
3.HttpOnly:禁用脚本访问


'''