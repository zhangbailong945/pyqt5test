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

