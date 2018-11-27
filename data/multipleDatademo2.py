from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class DateDialog(QDialog):

    def __init__(self,parent=None):
        super(DateDialog,self).__init__(parent)
        self.setWindowTitle('DateDialog')

        layout=QVBoxLayout(self)
        self.datetime=QDateEdit(self)
        self.datetime.setCalendarPopup(True)
        self.datetime.setDateTime(QDateTime.currentDateTime())
        layout.addWidget(self.datetime)

        #使用两个按钮（ok和cancel）
        buttons=QDialogButtonBox(
            QDialogButtonBox.Ok|QDialogButtonBox.Cancel,
            Qt.Horizontal,self
        )
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)
    
    def dateTime(self):
        return self.datetime.dateTime()
    
    #使用静态函数创建对话框 并返回
    @staticmethod
    def getDateTime(parent=None):
        dialog=DateDialog(parent)
        result=dialog.exec_()
        date=dialog.dateTime()
        return (date.date(),date.time(),result==QDialog.accepted)
    
