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