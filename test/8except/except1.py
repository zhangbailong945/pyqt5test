'''

#异常处理
try语句的工作方式
1.首先执行try字句（try和except之间的语句）
2.如果没有发生异常，忽悠except子句,try子句执行后结束。
3.如果在执行try子句的过程中发生了异常，那么try子句余下
的部分将被忽略。如果异常的类型和except之后的名称相符，那么对应
的except子句将被执行，最后执行try语句之后的代码。
4.如果一个异常没有与任何的except匹配，那么这个异常将会传递给上层的try中。

5.一个try语句可能包含多个except子句，分别处理不同的特定异常。
最多只有一个分支会被执行。

6.else 在try没有发生异常之后执行

7.raise 抛出异常，不处理异常

8.用户自定义异常,继承Exception类

9.定义清理行为 finally,定义了无论在任何情况下都会执行的清理行为。

10.预定义的清理行为with,关键字with语句就可以保证文件的对象在使用完之后，
一定会正确的执行他的清理方法


'''

class MyError(Exception):

    def __init__(self,value):
        self.value=value
    
    def __str__(self):
        return repr(self.value)


try:
    raise MyError(2*2)
except MyError as e:
    print('My exception occurred,value:',e.value)



