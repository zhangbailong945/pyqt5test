import socket,sys

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host=socket.gethostname()

port=9999

#连接到主机
s.connect((host,port))

#接受数据
msg=s.recv(1024)

s.close()
print(msg.decode('utf-8'))