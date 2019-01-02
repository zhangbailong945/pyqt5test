'''
条件控制

'''

#if else

if True:
    print(1)
else:
    print(0)

a,b=1,1

if a<b:
    print(a)
elif a>b:
    print(b)
else:
    print('%d==%d'%(a,b))

#while 循环

maxNumber=100
sum=0
conunter=1
#计算0-100的和
while conunter<=maxNumber:
    sum+=conunter
    conunter+=1

print(sum)

var=1
#循环 while else
'''
while var<5:
    number=int(input("请输入一个数字:"))
    print('你输入的数字是%d'%number)
    var+=1
else:
    print('超过5遍了')

print('退出循环')
'''

#while (True):print('Welcome Python3!')

for x in range(5,9,2):
    pass