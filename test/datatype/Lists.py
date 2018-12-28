
'''

List(列表)是python中使用最频繁的数据类型
 1.列表中的元素可以不同
 2.支持嵌套
 3.列表[]之间，用逗号隔开元素
 4.列表截取返回新的列表
 5.列表中的元素可以改变

'''
word=['a','b','c','d','e','f']

word2=['j','k','l']

print(word[-3:-1])
print(word[1:3])

#访问列表中第一个元素
print(word[0])

#更新列表中第二个元素
word[1]=2
print(word)

#删除列表中的第三个元素
del word[2]
print(word)

#获取列表的长度
print(len(word))

#两个列表相加
print(word+word2)

#重复列表
print(word*2)

#检查元素是否在列表中
print(2 in word)

#迭代列表
for x in word:
    print(x)
    print(word.count(x))

#列表嵌套

l1=[[1,2,3],[4,5,6],[7,8,9]]
print(l1)
print(l1[0])
print(l1[0][2])

#列表中常用方法
#len(list)
#max(list)
#min(list)
#list(seq)

#内置方法
#append
word.append('5')
print(word)
seq=(0,9,8,)

#extend
word.extend(seq)
print(word)

#index
print(word.index('5'))

#insert
print(word.insert(5,5))
print(word)

#pop 
word.pop(5)
print(word)

#remove
word.remove(2)
print(word)

#reverse
word.reverse()
print(word)

#sort()
word.sort()
print(word)