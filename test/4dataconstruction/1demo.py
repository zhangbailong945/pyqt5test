'''
列表方法使得列表可以很方便的作为一个堆栈来使用。后进先出
append() 把一个元素添加到堆栈顶
pop() 把一个元素从堆栈顶释放出来
'''

stack=[1,2,3]
stack.append(4)
print(stack.pop())


#把列表当做队列来使用 (先进先出)
from collections import deque
queue=deque(['long','bai','zhang'])
queue.append('shi')
queue.append('shen')
print(queue)
print(queue.popleft())


#列表推导式
#提供了从序列创建列表的捷径
#每个列表推导式，都是在for之后跟一个表达式
list1=[x for x in range(1,11)]
print(list1)


#遍历技巧
#将序列以简直的形式打印出来
seq=['A','B','C']

for k,v in enumerate(seq):
    print('%d==%s'%(k,v))

#同时遍历两个或更多的序列
questions=['name','quest','favorite color']
answers=['lancelot','the holy grail','red']

for q,a in zip(questions,answers):
    print('what is your {0}? It is {1}.'.format(q,a))


#循环输出序列，要先对序列反序
seq11=[1,2,3,4,5,6,7]

for x in reversed(seq11):
    print(x)


#对序列继续排序

set11=set(seq11)
for x in set11:
    print(x)

print(set11)

for x in sorted(set(seq11)):
    print(x)