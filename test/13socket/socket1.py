#Socket
'''
Socket套接字，应用程序通常通过套接字向网络发出请求或者应答网络请求，使主机
或者一台计算机上的进程可以通讯

'''

import socket

#socket.socket(family,type,proto)
#family:套接字家族 可以使用AF_UNIX或者AF_INET
#type:套接字类型可以根据是面向连接的还是非连接分为SOCK_STREAM或DGRAM
#protocol:一般不填默认为0

#socket对象的内建方法


'''
服务器端
1.bind() 绑定地址(host,port)到套接字
2.listen() 开始TCP监听，backlog指定在拒绝之前，操作系统可以挂起的最大数据量。
3.被动接受TCP客户端连接，（阻塞式）等待连接的到来

客户端
1.connect() 主动初始化TCP服务器连接，一般address的格式为元组(hostname,port),如果连接出错，返回socket.error错误。
2.connect_ex() 出错时返回错误码


#公共用途的函数
1.recv() 接受TCP数据，数据以字符串形式返回，busize指定要接受的最大数据量。
2.send() 发送TCP数据，将string红的数据发送到套接字，返回值是要发送的字节数量。
3.sendall() 完整发送TCP数据，将string中的数据饭打连接的套接字，但在返回之前
尝试发送所有数据。成功返回None,失败则抛出异常。

4.recvfrom() 接受UDP数据，返回值（data,address）
5.sendto() 发送udp数据，将数据放到套接字
6.close() 关闭套接字
7.getpeername() 返回套接字自己的地址
8.getsockopt(level,optname,value) 返回套接字选项的值
9.settimeout() 设置套接字的超时期
10.gettimeout() 返回当前超时期的值
11.setblocking(flag) 如果flag为0，则将套接字设置为非阻塞式
12.makefile() 创建一个与该套接字相关连的文件


'''

#创建服务的套接字
import sys
#创建套接字对象
serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#绑定主机和端口
host=socket.gethostname()
port=9999
serversocket.bind((host,port))

#设置最大连接数
serversocket.listen(5)

while True:
    #建立客户的连接
    clientsocket,addr=serversocket.accept()
    print('连接地址:%s'%str(addr))
    msg='欢迎光临!'+'\r\n'
    clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()





