# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\PyQt5Projects\pyqt5test\Novel\StatusBarWidget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StatusBarWidget(object):
    def setupUi(self, StatusBarWidget):
        StatusBarWidget.setObjectName("StatusBarWidget")
        StatusBarWidget.resize(410, 30)
        StatusBarWidget.setMaximumSize(QtCore.QSize(16777215, 30))
        #StatusBarWidget.setAutoFillBackground(True)
        #StatusBarWidget.setStyleSheet("background-color:red;")
        #StatusBarWidget.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0.00568182, y1:0.051, x2:0, y2:0.563, stop:0 rgba(188, 217, 235, 255), stop:1 rgba(255, 255, 255, 255));background-color: rgb(192, 220, 239);")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(StatusBarWidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.novelname_label = QtWidgets.QLabel(StatusBarWidget)
        self.novelname_label.setObjectName("novelname_label")
        self.horizontalLayout_2.addWidget(self.novelname_label)
        self.novelversion_label = QtWidgets.QLabel(StatusBarWidget)
        self.novelversion_label.setObjectName("novelversion_label")
        self.horizontalLayout_2.addWidget(self.novelversion_label)
        self.checkupdate_label = QtWidgets.QLabel(StatusBarWidget)
        self.checkupdate_label.setObjectName("checkupdate_label")
        self.horizontalLayout_2.addWidget(self.checkupdate_label)
        self.suggest_label = QtWidgets.QLabel(StatusBarWidget)
        self.suggest_label.setObjectName("suggest_label")
        self.horizontalLayout_2.addWidget(self.suggest_label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.other_label = QtWidgets.QLabel(StatusBarWidget)
        self.other_label.setObjectName("other_label")
        self.horizontalLayout_2.addWidget(self.other_label)

        self.retranslateUi(StatusBarWidget)
        QtCore.QMetaObject.connectSlotsByName(StatusBarWidget)

    def retranslateUi(self, StatusBarWidget):
        _translate = QtCore.QCoreApplication.translate
        StatusBarWidget.setWindowTitle(_translate("StatusBarWidget", "Form"))
        self.novelname_label.setText(_translate("StatusBarWidget", "<html><head/><body><p><a href=\"http://www.zhangbailong.com/novel\" target=\"_blank\"><span style=\" text-decoration: underline; color:#0000ff;\">搜书神器</span></a></p></body></html>"))
        self.novelversion_label.setText(_translate("StatusBarWidget", "V1.0"))
        self.checkupdate_label.setText(_translate("StatusBarWidget", "<html><head/><body><p><a href=\"http://www.zhangbailong.com/novel/update\"><span style=\" text-decoration: underline; color:#0000ff;\">检查更新</span></a></p></body></html>"))
        self.suggest_label.setText(_translate("StatusBarWidget", "<html><head/><body><p><a href=\"http://www.zhangbailong.com/suggest\"><span style=\" text-decoration: underline; color:#0000ff;\">意见反馈</span></a></p></body></html>"))
        self.other_label.setText(_translate("StatusBarWidget", "<html><head/><body><p>其他</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StatusBarWidget = QtWidgets.QWidget()
    ui = Ui_StatusBarWidget()
    ui.setupUi(StatusBarWidget)
    StatusBarWidget.show()
    sys.exit(app.exec_())

