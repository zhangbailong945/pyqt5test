'''
命令模式 Command
将一个请求封装为一个对象，
从而使你可用不同的请求对客户进行参数化；
对请求排队或者记录日志，以及支持可撤销的操作。

行为请求者与行为实现者通常呈现一种耦合。
比如要对细微记录、撤销/重做、事务等处理。这种无法抵御变化的紧耦合是
不合适的。
命令模式角色：
Command:
定义命令的接口，声明执行的方法，可以理解为一个基类。
ConcreteCommand:
命令接口实现对象，通常会持有接受者，并调用接受者的功能来完成命令要执行的操作。
Receiver:
接受者，真正执行命令的对象，任何类都可能成为一个接受者，只要它能够实现命令要求
实现的相应功能。
Invoker:
要求命令对象执行请求，通常会持有命令对象，可以持有很多的命令对象，相当于使用命令
对象的入口。
Client:
创建具体的命令对象，组装命令对象和及守着，或者把这个client称谓装配者会更好理解，
因为真正使用命令的客户端从Invoker来触发执行。

'''


class Command:

    '''声明命令模式接口'''
    def __init__(self,obj):
        self.obj=obj
    
    def execute(self):
        pass

class ConcreteCommand(Command):
    '''实现命令模式接口'''
    def execute(self):
        self.obj.run()
    
class Invoker:
    '''接受命令并执行命令的接口'''
    def __init__(self):
        self._commands=[]
    
    def add_command(self,cmd):
        self._commands.append(cmd)
    
    def remove_command(self,cmd):
        self._commands.remove(cmd)
    
    def run_command(self):
        for cmd in self._commands:
            cmd.execute()


class Receiver:
    '''具体动作'''
    def __init__(self,word):
        self.word=word
    
    def run(self):
        print(self.word)


def client():
    '''装配者'''
    test=Invoker()
    cmd1=ConcreteCommand(Receiver('命令一'))
    test.add_command(cmd1)
    cmd2=ConcreteCommand(Receiver('命令二'))
    test.add_command(cmd2)
    cmd3=ConcreteCommand(Receiver('命令三'))
    test.add_command(cmd3)
    test.run_command()

if __name__ == "__main__":
    client()