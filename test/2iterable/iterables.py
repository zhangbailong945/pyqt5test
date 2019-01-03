import sys
'''
生成器


'''
list1=[1,2,3,4,5,6,7,8]
it=iter(list1)
#print(next(it))
for x in it:
    print(x,end=" ")

#循环迭代
while True:
    try:
        print(next(it),end=",")
    except StopIteration:
        break


#创建迭代器
#1.把一个类作为迭代器使用需要实现两个方法，__iter__()和__next__()

class MyNumbers:

    def __iter__(self):
        self.a=1
        return self
    
    def __next__(self):
        if self.a<=20:
            x=self.a
            self.a+=1
            return x
        else:
            raise StopIteration

myclass=MyNumbers()
print(type(myclass))

myiter=iter(myclass)

for x in myiter:
    print(x)
    