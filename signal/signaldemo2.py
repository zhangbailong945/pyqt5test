from PyQt5.QtCore import QTimer,Qt,QDateTime,pyqtSignal,QObject
from PyQt5.QtWidgets import QApplication,QWidget,QGridLayout,\
QListWidget,QLabel,QMessageBox,QPushButton
import sys

#自定义信号和槽

#信号对象
class QTypeSignal(QObject):

    #定义信号
    sendMsg=pyqtSignal(object)

    def __init__(self):
        super(QTypeSignal,self).__init__()
    
    def run(self):
        self.sendMsg.emit("Hello PyQt5!")

#槽对象
class QTypeSlot(QObject):

    def __init__(self):
        super(QTypeSlot,self).__init__()
    
    def get(self,msg):
        print('QSlot get msg: '+msg)




if __name__=='__main__':
    send=QTypeSignal()
    slot=QTypeSlot()

    send.sendMsg.connect(slot.get)
    send.run()

    send.sendMsg.disconnect(slot.get)
    send.run()