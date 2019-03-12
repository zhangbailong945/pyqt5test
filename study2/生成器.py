#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   生成器.py
@Time    :   2019/03/11 22:20:20
@Author  :   loach
@Version :   1.0
@Contact :   1207549344@qq.com
@License :   (C)Copyright 2019-2010 loachblog.com
@Desc    :   None
'''

# here put the import lib
#生成器
#在python中一边循环一边计算的机制，成为生成器generator
#把一个列表的生成式的[]改为()，就是创建了一个generator
L=[x * x for x in range(5)]
print(L)

G=(x * x for x in range(5))
print(next(G))
print(next(G))
print(next(G))
print(next(G))
print(next(G))

while(True):
    try:
        x=next(G)
        print('G:',x)
    except StopIteration as e:
        print('Generator return value:',e.value)
        break