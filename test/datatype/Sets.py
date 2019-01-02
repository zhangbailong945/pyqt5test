'''
#集合set
是一个无序的不重复的序列
可以使用大括号或者set()函数创建集合，但是空集合必须用set()而不是{}。

'''

#创建
set1={'1','2',3,5.33}
print(type(set1))
print(set1)

set2={1,2,3,4,5}
set3={3,5,6,7,8}

print(set2.difference(set3))

#集合1相对于集合2的差集
print(set2-set3)

#并集
print(set2|set3)

#交集
print(set2&set3)

#对称差集
print(set2^set3)

#集合添加元素
set4=set()
set4.add('A')
set4.add('B')
set4.add('C')
set4.add('D')
set4.add('E')
print(set4)

#update()
set4.update('F','G','H')
print(set4)
#remove(x),如果x元素不存在，会发生错误
set4.remove('F')
print(set4)

#discard(x),删除x元素，不存在不发生错误
set4.discard('F')
print(set4)

#pop(),随机删除集合中的一个元素
set4.pop()
print(set4)

#清空集合
set4.clear()
print(set4)

a,b=0,1
while b<1000:
    print(b,end=",")
    a,b=b,a+b
