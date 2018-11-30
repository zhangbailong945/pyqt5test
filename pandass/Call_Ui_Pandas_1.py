from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
import sys,time
from Ui_Pandas_1 import Ui_MyWidget
from qtpandas.models.DataFrameModel import DataFrameModel
import pandas as pd 

##QSS的UI美化

class WinForm(QWidget,Ui_MyWidget):

    def __init__(self,parent=None):
        super(WinForm,self).__init__(parent)
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        widget=self.pandastablewidget
        widget.resize(600,500)

        self.model=DataFrameModel()
        widget.setViewModel(self.model)
        self.df=pd.read_excel(r'D:/PyQt5Projects/pyqt5test/data/fund_data.xlsx',encoding='gbk')
        self.df_original=self.df.copy() #备份原始数据
        self.model.setDataFrame(self.df)
    
    @pyqtSlot()
    def on_btnInitData_clicked(self):
        print('initdata')
        self.model.setDataFrame(self.df_original)
    
    @pyqtSlot()
    def on_btnSaveData_clicked(self):
        print('savadata')
        self.df.to_excel(r'D:/PyQt5Projects/pyqt5test/data/fund_data_copy.xlsx')



if __name__=="__main__":
    app=QApplication(sys.argv)
    demo=WinForm()
    demo.show()
    sys.exit(app.exec_())