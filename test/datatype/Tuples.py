'''
1.元组和列表相似，元组的元素不能修改
2.元组用小括号，列表用方括号






'''
tuple1=(1,2,3,4,5)
tuple2="A","B","C","D","E"

print(type(tuple1))
print(type(tuple2))

#访问 下标
print(tuple1[0:2])
print(tuple2[-3:-1])

#修改元组，元组的元素不能被修改，但是可以连接两个元组
tuple3=tuple1+tuple2
print(tuple3)

#删除元组，元组的元素是不能删除的，但是可以使用del删除真个元组
#del tuple3
#print(tuple3)

#元组运算符
print(len(tuple3))
#连接
print(tuple1+tuple2)
#复制
print(tuple3*4)
#是否存在
print('A' in tuple2)
#迭代
for x in tuple3:
    print(x)


#元组截取
tuple4=("Tmall","Taobao","Jingdong")
print(tuple4[2])
print(tuple4[-2])
print(tuple4[1:])
