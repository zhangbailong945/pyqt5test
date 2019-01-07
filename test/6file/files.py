'''
#方法 python
1.open()方法，用于打开一个文件，并返回文件对象。
2.在堆文件进行处理过程都要使用到这个函数。如果文件无法打开，会抛出OSError
3.使用open()方法一定要保证关闭文件对象，即调用close()方法。

open(file,mode='r',buffering=-1,encoding=None,errors=None,newlineNone,closefd=True,opener=None)




'''

#打开文件
fo=open("python.txt","r+",encoding="utf8")
print('文件名:',fo.name)

#清楚缓冲区
#fo.flush()

#返回一个整型的文件描述符
fid=fo.fileno()
print('文件描述符:',fid)

#如果连接到一个终端设备返回True

ret=fo.isatty()
print('是否连接到终端设备：',ret)

#next()该方法返回文件的下一行
'''
for x in range(5):
    line=next(fo)
    print('第%d行,内容是:%s'%(x,line))
'''
#read(szie) 方法用于从文件读取指定的字节数，如果为给定或负责读取所有

#size 从文件中读取的字节数

#line=fo.read(10)

#读取整行，包括\n

'''
line=fo.readline()
print('内容是：',line)
line2=fo.readline(2)
print('内容2是：',line2)

'''

#readlines() 读取所有行，并返回列表
'''
for line in fo.readlines():
    line=line.strip()
    print("内容：",line)
'''

#seek(offset[,whence]),用于移动文件读取指针到指定位置
# 0表示开头，1表示当前，2表示末尾
line=fo.readline()
print('内容',line) 
'''
fo.seek(0,0)
line2=fo.readline()
print('内容2',line2)

fo.seek(1,0)
line3=fo.readline()
print('内容3',line3)
'''

#tell()返回当前的位置
fposition=fo.tell()
print('当前位置',fposition)

fo.truncate()
line=fo.readlines()
print('取行',line)


#在末尾写入新的一行
fo.seek(0,2)
fo.write('第六行')

#wirtelines() 用于写入一序列的字符串
seq=['第七行\n','第八行\n','第九行']
fo.seek(0,2)
fo.writelines(seq)

#关闭文件
fo.close()