import sys

from PyQt5.QtWidgets import QApplication,QWidget
from Libraries.Views.Ui_StatusBarWidget import Ui_StatusBarWidget


class Call_StatusBarWidget(QWidget,Ui_StatusBarWidget):

    def __init__(self,*args,**kwargs):
        super(Call_StatusBarWidget,self).__init__(*args,**kwargs)
        self.setupUi(self)
        self.initUI()
    
    def initUI(self):
        self.setStyleSheet("background-color: rgb(192, 220, 239);")

