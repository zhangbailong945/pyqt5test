# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Codes\PyQt5Projects\Ui_Pandas_1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MyWidget(object):
    def setupUi(self, MyWidget):
        MyWidget.setObjectName("MyWidget")
        MyWidget.resize(437, 485)
        self.horizontalLayout = QtWidgets.QHBoxLayout(MyWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pandastablewidget = DataTableWidget(MyWidget)
        self.pandastablewidget.setObjectName("pandastablewidget")
        self.horizontalLayout.addWidget(self.pandastablewidget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnInitData = QtWidgets.QPushButton(MyWidget)
        self.btnInitData.setObjectName("btnInitData")
        self.verticalLayout.addWidget(self.btnInitData)
        self.btnSaveData = QtWidgets.QPushButton(MyWidget)
        self.btnSaveData.setObjectName("btnSaveData")
        self.verticalLayout.addWidget(self.btnSaveData)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(MyWidget)
        QtCore.QMetaObject.connectSlotsByName(MyWidget)

    def retranslateUi(self, MyWidget):
        _translate = QtCore.QCoreApplication.translate
        MyWidget.setWindowTitle(_translate("MyWidget", "pandas_pyqt"))
        self.btnInitData.setText(_translate("MyWidget", "数据初始化"))
        self.btnSaveData.setText(_translate("MyWidget", "保存数据"))

from qtpandas.views.DataTableView import DataTableWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MyWidget = QtWidgets.QWidget()
    ui = Ui_MyWidget()
    ui.setupUi(MyWidget)
    MyWidget.show()
    sys.exit(app.exec_())

