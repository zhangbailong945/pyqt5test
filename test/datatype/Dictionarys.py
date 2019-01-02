'''

#字典

'''

#1.字典是另一种可变容器模型，且可存储任意类型对象
#2.字典的每个键值对用冒号分割，整个字典包括在花括号中。
#3.键必须是唯一的，但值则不必
#4.值可以取任意数据类型，但键必须是不可变的。
#5.键不能重复，如有重复只会记录最后一个

dict1={"A":1,"C":2,"D":3,"B":4}
print(type(dict1))

#访问 字典里面的值
print(dict1['A'])

#修改 字典
dict1['A']=6
print(dict1)

# 删除字典的元素
del dict1['A']
print(dict1)

# 清空字典
#dict1.clear()
#print(dict1)

#删除字典 
#del dict1
#print(dict1 is None)

print(str(dict1))

#内置方法
#1.dict.fromkeys(seq),把seq序列作为字典的键，val为值
seq1=(1,2,3,4)
dict=dict.fromkeys(seq1,1)
print(dict)
#{1: 1, 2: 1, 3: 1, 4: 1}

#2.dict.get(key),通过键返回值
print(dict1.get('B'))


print('B' in dict1)
#4 返回可迭代的数组dict.items()
for k,v in dict1.items():
    print('%s===%d'%(k,v))

#5.返回迭代器
itera=dict1.keys()
list1=list(itera)
print(type(list1))
print(list1)

#6.通过键找值，如果值不存在，就用默认的
print(dict1.setdefault('F',444))
print(dict1)

#{'C': 2, 'D': 3, 'B': 4, 'F': 444}

dict2={"name":'zhangsan',"age":12,"sex":'male'}

#7.dict.update(dict2),将dict2更新到dict中
dict1.update(dict2)
print(dict1)

#8.dict.values(),返回值的迭代器
for x in dict1.values():
    print(x)

#9.删除字典指定key的值，值必须有，否则返回默认
print(dict1.pop('D',5))
print(dict1)

#10.随机删除字典中的一对键值对，一般删除末尾对
print(dict1.popitem())
print(dict1)