'''

模块

把定义存放在问价那种，为一些脚本或者交互式的解释器实例使用，这个文件被称为模块。
模块是一个包含所有定义的函数和变量的文件，其后缀名是.py。模块可以被别的程序引入，以使用该模块中的函数等功能。
#1.import sys
#2.sys.argv  一个包含命令行参数的列表
#3.sys.path  包含一个python解释器自动查找所需模块的路径的列表

from modulefile import func1,func2,....

__name__ 属性
一个模块被另一个程序第一次引入时，其主程序将运行。
如果我们想在模块被引入时，模块中的某一个程序块不执行，我们可以用
__name__属性来使该程序块仅在该模块自身运行是执行。

每个模块都有一个__name__属性，当其值为__main__时，表明该模块在自身运行，否则是被引入。

#包是一个管理Python模块命名空间的形式，采用点模块名称
比如一个模块的名称是A.B,那么他表示一个包A中的子模块B。

'''

import sys,fibo

print(dir(sys))