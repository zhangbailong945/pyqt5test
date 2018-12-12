import sys

from PyQt5.QtWidgets import QApplication,QWidget
from Libraries.Views.Ui_TitleBarWidget import Ui_TitleBarWidget


class Call_TitleBarWidget(QWidget,Ui_TitleBarWidget):

    def __init__(self,*args,**kwargs):
        super(Call_TitleBarWidget,self).__init__(*args,**kwargs)
        self.setupUi(self)
    
    def initUI(self):
        self.setStyleSheet("background-color: rgb(192, 220, 239);")


