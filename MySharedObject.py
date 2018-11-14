from PyQt5.QtCore import QObject,pyqtProperty
from PyQt5.QtWidgets import QWidget,QMessageBox

class MySharedObject(QWidget):

    def __init__(self):
        super(MySharedObject,self).__init__()
    
    def _getStrValue(self):
        return "100"
    
    def _setStrValue(self,str):
        print('页面参数:%s'%str)
        QMessageBox.information(self,'信息','获取页面参数:%s'%str)
    
    #对外部发布的方法
    strValue=pyqtProperty(str,fget=_getStrValue,fset=_setStrValue)