#解释器
'''
意图：
给定一个语言，定义它的文法的一种表示，并定义这个解释器，这个解释器
使用该表示来解释语言中的句子。
适用性：
当一个语言需要解释执行时，并且你可将该语言中的句子表示为一个抽象语法树时，
可使用解释器模式。
场景1：
该文法简单对于复杂的文法，文法的类层次变得庞大而无法管理。此时语法分析程序生成器
这样的工具是更好的选择。他们无需构造抽象语法树即可解释表达，这样可以节省空间而且还
可能节省时间。
效率不是一个关键问题最高效的解释器通常不是通过直接解释器语法分析树来实现的，而是首先
将他们转换成另一种形式。例如，正则表达式通常被转换成状态机。但即使在这种情况下，转换器
仍用解释器模式实现。
解释器模式实现两个核心角色：
终结符表达式：实现与文法中的元素相关联的解释操作。通常一个解释器模式中只有一个
终结符表达式，但有多个实例，对应不同的终结符。终结符一半的文法中的运算单元，比如有一个
简单的公式R=R1+R2,在里面R1好R2就是终结符，对应的解析R1和R2的解释器就是终结符表达式。

非终结符表达式：文法中的每条规则对于一个非终结符表达式，非终结符表达式一般是文法中的
运算符或者其他关键字。比如公式R=R1+R2中，+就是非终结符，解析+的解释器就是一个非终结符表达式。
非终结符表达式。非终结符表达式根据逻辑的复杂程度而增加，原则上一个文法规则都对应一个非终结符表达式。

'''

import time
import datetime

'''实现中文编程'''

class Code:
    '''自定义语言'''
    def __init__(self,text=None):
        self.text=text


class InterpreterBase:

    '''自定义解释器基类'''
    def run(self,code):
        pass


class Interpreter(InterpreterBase):

    '''实现解释器方法，实现终结符表达式字典'''
    def run(self,code):
        code=code.text
        code_dict={'获取当前时间戳':time.time(),"获取当前日期":datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        print(code_dict.get(code))


if __name__ == "__main__":
    test=Code()
    test.text='获取当前时间戳'
    Interpreter().run(test)
    test.text='获取当前日期'
    Interpreter().run(test)