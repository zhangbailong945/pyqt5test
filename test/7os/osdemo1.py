'''

os模块提供了非常丰富的方法用来处理文件和目录



'''

#1.检验权限模式os.access(path,mode)
#path 检查的路径
#mode 测试类型，F_OK是否存在，R_OK是否可读，W_OK是否可写，X_OK是否可执行。
import os



ret=os.access('./test/6file/python.txt',os.F_OK)
print('F_OK-返回值为:%s'% ret)


ret=os.access('./test/6file/python.txt',os.R_OK)
print('R_OK-返回值为:%s'% ret)

ret=os.access('./test/6file/python.txt',os.W_OK)
print('W_OK-返回值为:%s'% ret)

ret=os.access('./test/6file/python.txt',os.X_OK)
print('X_OK-返回值为:%s'% ret)


#2.os.chdir(path) 用于改变当前工作目录到指定的路径
#path 要切换到的新路径

import sys

path='D:/PyQt5Projects'
#查看当前目录
retval=os.getcwd()
print('当前工作目录%s'% retval)

#修改当前工作目录
os.chdir(path)

#修改后的当前目录
retval=os.getcwd()
print('目录修改后的%s'% retval)

#3.os.chflags(path,flags) 方法用于设置路径的标记为数字标记。只支持在linux使用
#path 路径
#flags可以是一下值
#stat.UF_NODUMP: 非转储文件
#stat.UF_IMMUTABLE 文件是只读的
#stat.UF_APPEND 文件只能追加
#stat.UF_NOUNLINK:文件不可删除
#stat.UF_OPAQUE:目录不透明，需要通过联合堆栈查看
#stat.SF_ARCHIVED:可存档文件（超级用用户）
#stat.SF_IMMUTABLE:文件只读（超级用户）
#stat.SF_APPEND:文件只能追加(超级用户)
#stat.SF_NOUNLINK:文件不可删除（超级用户）
#stat.SF_SNAPSHOT:快照文件（超级用户可社）


#4.os.chmod(path,mode)用于改变文件或目录的权限
#path 文件路径或者目录路径
#mode
#stat.S_IXOTH:其他用户有执行权
#stat.S_IWOTH:其他用户有写权限
#stat.S_IROTH:其他用户有读权限
#stat.S_IRWXO:其他用户有全部权限
#stat.S_IXGRP:组用户有执行权限
#stat.S_IWGRP:组用户有写权限
#stat.S_IRGRP:组用户有读权限
#stat.S_IRWXG:组用户有全部权限
#stat.S_IXUSR:拥有者有执行权限
#stat.S_IWUSR:拥有者有写权限
#stat.S_IRUSR:拥有者有读权限
#stat.S_IRWXU:拥有者拥有全部权限
#stat.S_ISVTX:目录文件目录只有拥有者才可删除
#stat.S_ISGID:执行此文件其进程有效组为文件所在组
#stat.S_ISUID:执行此文件进程有效用户为拥有者
#stat.S_IREAD:window下设只读
#stat.S_IWRITE:windows下取消只读

#5.os.chown(path,uid,gid)
#paht 设置权限的文件路径
#uid 所属用户id
#gid 所属用户组

#5.os.chroot(path) 用于更改当前进程的根目录
#path要设置为根目录的目录


#6.os.close(fd)  用于关闭指定的文件描述符
#fd 文件描述符

#7.os.closerange() 用于关闭所有文件描述符fd,从fd_low到fd_high,错误会忽略
#os.closerange(fd_low,fd_high)


#os.listdir(path)
print(os.listdir('D:\PyQt5Projects'))

#os.mkdir(path) 创建目录

#os.remove(path) 删除路径为path的文件

#os.removedirs(paht) 递归删除目录

#os.rmdir(path) 删除一个空目录，非空报错

import os.path

#os.path模块 主要用于获取文件的属性


#1.返回文件的绝对路径
path="d:\\PyQt5Projects\\pyqt5test\\test\\7os\\osdemo1.py"
path2="d:\\PyQt5Projects\\pyqt5test\sss\ff"
path3="d:\\PyQt5Projects\\pyqt5test\ss\ww\tt"
list1=[]
list1.append(path)
list1.append(path2)
list1.append(path3)

print(os.path.abspath(path))

#2.返回文件名
print(os.path.basename(path))

#3.返回list中多个路径，所有path共有的最长的路径
print(os.path.commonprefix(list1))


#4.返回文件路径
print(os.path.dirname(path))

#5.路径是否存在
print(os.path.exists(path))

#6.文件最近访问时间
print(os.path.getatime(path))

#7.文件最近修改时间
print(os.path.getmtime(path))

#8.返回文件的创建时间
print(os.path.getctime(path))


#9.返回文件的大小
print(os.path.getsize(path))

#10.判断是否为绝对路径
print(os.path.isabs(path))

#11.判断是否问文件
print(os.path.isfile(path))

#12.判断是否为目录
print(os.path.isdir(path))

#13.判断是否为链接
print(os.path.islink(path))

#14.判断是否为挂载点
print(os.path.ismount(path))

#15.把目录和文件名合成一个路径
print(os.path.join(path,path2))

#16.转换path的大小写和斜杠
print(os.path.normcase(path))

#17.规范化path字符串形式
print(os.path.normpath(path))

#18.规划化path的真实路径
print(os.path.realpath(path))

#19.判断文件或目录是相同
#print(os.path.samefile(path,path2))

#20.判断f1和f2是否指向同一文件
#print(os.path.sameopenfile(path,path2))

#21.把路径分隔dirname和basename，返回一个元组
print(os.path.split(path))

#22.一般在windows下，返回驱动器名或路径组成的元组
print(os.path.splitdrive(path))

#23,分隔路径，返回路径名和文件扩展名的元组
print(os.path.splitext(path))












