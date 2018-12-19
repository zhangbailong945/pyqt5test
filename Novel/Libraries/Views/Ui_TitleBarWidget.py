# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\PyQt5Projects\pyqt5test\Novel\TitleBarWidget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from images import images

class Ui_TitleBarWidget(object):
    def setupUi(self, TitleBarWidget):
        TitleBarWidget.setObjectName("TitleBarWidget")
        TitleBarWidget.resize(642, 70)
        TitleBarWidget.setMinimumSize(QtCore.QSize(0, 70))
        TitleBarWidget.setMaximumSize(QtCore.QSize(16777215, 70))
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(TitleBarWidget)
        self.horizontalLayout_2.setContentsMargins(-1, 0, 0, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.header_img_label = QtWidgets.QLabel(TitleBarWidget)
        self.header_img_label.setMinimumSize(QtCore.QSize(60, 60))
        self.header_img_label.setMaximumSize(QtCore.QSize(60, 60))
        self.header_img_label.setText("")
        self.header_img_label.setPixmap(QtGui.QPixmap(":/images/logo.png"))
        self.header_img_label.setScaledContents(True)
        self.header_img_label.setAlignment(QtCore.Qt.AlignCenter)
        self.header_img_label.setWordWrap(False)
        self.header_img_label.setObjectName("header_img_label")
        self.horizontalLayout_2.addWidget(self.header_img_label)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.login_label = QtWidgets.QLabel(TitleBarWidget)
        self.login_label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.login_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.login_label.setAlignment(QtCore.Qt.AlignCenter)
        self.login_label.setObjectName("login_label")
        self.verticalLayout.addWidget(self.login_label)
        self.login_info_label = QtWidgets.QLabel(TitleBarWidget)
        self.login_info_label.setObjectName("login_info_label")
        self.verticalLayout.addWidget(self.login_info_label)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.online_btn = QtWidgets.QPushButton(TitleBarWidget)
        self.online_btn.setMinimumSize(QtCore.QSize(70, 0))
        self.online_btn.setMaximumSize(QtCore.QSize(70, 70))
        self.online_btn.setStyleSheet("border:0px;\n"
"")
        self.online_btn.setObjectName("online_btn")
        self.horizontalLayout_3.addWidget(self.online_btn)
        self.bookstack_btn = QtWidgets.QPushButton(TitleBarWidget)
        self.bookstack_btn.setMinimumSize(QtCore.QSize(70, 0))
        self.bookstack_btn.setMaximumSize(QtCore.QSize(70, 70))
        self.bookstack_btn.setStyleSheet("border:0px;\n"
"")
        self.bookstack_btn.setObjectName("bookstack_btn")
        self.horizontalLayout_3.addWidget(self.bookstack_btn)
        self.history_btn = QtWidgets.QPushButton(TitleBarWidget)
        self.history_btn.setMinimumSize(QtCore.QSize(70, 0))
        self.history_btn.setMaximumSize(QtCore.QSize(70, 70))
        self.history_btn.setAutoFillBackground(False)
        self.history_btn.setStyleSheet("border:0px;\n"
"")
        self.history_btn.setCheckable(False)
        self.history_btn.setObjectName("history_btn")
        self.horizontalLayout_3.addWidget(self.history_btn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_5.setContentsMargins(-1, -1, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.line_label1 = QtWidgets.QLabel(TitleBarWidget)
        self.line_label1.setMinimumSize(QtCore.QSize(0, 0))
        self.line_label1.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.line_label1.setAutoFillBackground(False)
        self.line_label1.setStyleSheet("border:1px solid red;\n"
"border-left:none;\n"
"border-top:none;\n"
"border-bottom:none;\n"
"border-right-color:rgb(87, 104, 136);")
        self.line_label1.setText("")
        self.line_label1.setTextFormat(QtCore.Qt.PlainText)
        self.line_label1.setScaledContents(False)
        self.line_label1.setWordWrap(False)
        self.line_label1.setObjectName("line_label1")
        self.horizontalLayout_5.addWidget(self.line_label1)
        self.feedback_btn = QtWidgets.QPushButton(TitleBarWidget)
        self.feedback_btn.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.feedback_btn.sizePolicy().hasHeightForWidth())
        self.feedback_btn.setSizePolicy(sizePolicy)
        self.feedback_btn.setMinimumSize(QtCore.QSize(40, 24))
        self.feedback_btn.setMaximumSize(QtCore.QSize(40, 70))
        self.feedback_btn.setToolTip("")
        self.feedback_btn.setStyleSheet("border:0px;\n"
"")
        self.feedback_btn.setFlat(False)
        self.feedback_btn.setObjectName("feedback_btn")
        self.horizontalLayout_5.addWidget(self.feedback_btn)
        self.line_label2 = QtWidgets.QLabel(TitleBarWidget)
        self.line_label2.setStyleSheet("border:1px solid red;\n"
"border-left:none;\n"
"border-top:none;\n"
"border-bottom:none;\n"
"border-right-color:rgb(87, 104, 136);")
        self.line_label2.setText("")
        self.line_label2.setObjectName("line_label2")
        self.horizontalLayout_5.addWidget(self.line_label2)
        self.setting_toolButton = QtWidgets.QToolButton(TitleBarWidget)
        self.setting_toolButton.setMinimumSize(QtCore.QSize(40, 24))
        self.setting_toolButton.setStyleSheet("border:0px;")
        self.setting_toolButton.setText("")
        self.setting_toolButton.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.setting_toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.setting_toolButton.setAutoRaise(False)
        self.setting_toolButton.setArrowType(QtCore.Qt.DownArrow)
        self.setting_toolButton.setObjectName("setting_toolButton")
        self.horizontalLayout_5.addWidget(self.setting_toolButton)
        self.line_label3 = QtWidgets.QLabel(TitleBarWidget)
        self.line_label3.setStyleSheet("border:1px solid red;\n"
"border-left:none;\n"
"border-top:none;\n"
"border-bottom:none;\n"
"border-right-color:rgb(87, 104, 136);")
        self.line_label3.setLineWidth(1)
        self.line_label3.setText("")
        self.line_label3.setObjectName("line_label3")
        self.horizontalLayout_5.addWidget(self.line_label3)
        self.min_btn = QtWidgets.QPushButton(TitleBarWidget)
        self.min_btn.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.min_btn.sizePolicy().hasHeightForWidth())
        self.min_btn.setSizePolicy(sizePolicy)
        self.min_btn.setMinimumSize(QtCore.QSize(40, 24))
        self.min_btn.setMaximumSize(QtCore.QSize(40, 70))
        self.min_btn.setStyleSheet("border:0px;")
        self.min_btn.setFlat(False)
        self.min_btn.setObjectName("min_btn")
        self.horizontalLayout_5.addWidget(self.min_btn)
        self.line_label4 = QtWidgets.QLabel(TitleBarWidget)
        self.line_label4.setStyleSheet("border:1px solid red;\n"
"border-left:none;\n"
"border-top:none;\n"
"border-bottom:none;\n"
"border-right-color:rgb(87, 104, 136);")
        self.line_label4.setText("")
        self.line_label4.setObjectName("line_label4")
        self.horizontalLayout_5.addWidget(self.line_label4)
        self.max_btn = QtWidgets.QPushButton(TitleBarWidget)
        self.max_btn.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.max_btn.sizePolicy().hasHeightForWidth())
        self.max_btn.setSizePolicy(sizePolicy)
        self.max_btn.setMinimumSize(QtCore.QSize(40, 24))
        self.max_btn.setMaximumSize(QtCore.QSize(40, 70))
        self.max_btn.setStyleSheet("border:0px;")
        self.max_btn.setFlat(False)
        self.max_btn.setObjectName("max_btn")
        self.horizontalLayout_5.addWidget(self.max_btn)
        self.line_label5 = QtWidgets.QLabel(TitleBarWidget)
        self.line_label5.setStyleSheet("border:1px solid red;\n"
"border-left:none;\n"
"border-top:none;\n"
"border-bottom:none;\n"
"border-right-color:rgb(87, 104, 136);")
        self.line_label5.setText("")
        self.line_label5.setObjectName("line_label5")
        self.horizontalLayout_5.addWidget(self.line_label5)
        self.close_btn = QtWidgets.QPushButton(TitleBarWidget)
        self.close_btn.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.close_btn.sizePolicy().hasHeightForWidth())
        self.close_btn.setSizePolicy(sizePolicy)
        self.close_btn.setMinimumSize(QtCore.QSize(40, 24))
        self.close_btn.setMaximumSize(QtCore.QSize(40, 70))
        self.close_btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.close_btn.setAutoFillBackground(False)
        self.close_btn.setStyleSheet("border:0px;")
        self.close_btn.setAutoRepeat(False)
        self.close_btn.setAutoExclusive(False)
        self.close_btn.setAutoDefault(False)
        self.close_btn.setDefault(False)
        self.close_btn.setFlat(False)
        self.close_btn.setObjectName("close_btn")
        self.horizontalLayout_5.addWidget(self.close_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.bookname_comboBox = QtWidgets.QComboBox(TitleBarWidget)
        self.bookname_comboBox.setObjectName("bookname_comboBox")
        self.bookname_comboBox.addItem("")
        self.bookname_comboBox.addItem("")
        self.horizontalLayout_4.addWidget(self.bookname_comboBox)
        self.bookname_lineEdit = QtWidgets.QLineEdit(TitleBarWidget)
        self.bookname_lineEdit.setStyleSheet("")
        self.bookname_lineEdit.setObjectName("bookname_lineEdit")
        self.horizontalLayout_4.addWidget(self.bookname_lineEdit)
        self.search_btn = QtWidgets.QPushButton(TitleBarWidget)
        self.search_btn.setObjectName("search_btn")
        self.horizontalLayout_4.addWidget(self.search_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.retranslateUi(TitleBarWidget)
        QtCore.QMetaObject.connectSlotsByName(TitleBarWidget)

    def retranslateUi(self, TitleBarWidget):
        _translate = QtCore.QCoreApplication.translate
        TitleBarWidget.setWindowTitle(_translate("TitleBarWidget", "TitleBarWidget"))
        self.login_label.setText(_translate("TitleBarWidget", "点击登录"))
        self.login_info_label.setText(_translate("TitleBarWidget", "登录可同步书架\n"
"和阅读记录"))
        self.online_btn.setText(_translate("TitleBarWidget", "在线\n"
"书城"))
        self.bookstack_btn.setText(_translate("TitleBarWidget", "我的\n"
"书架"))
        self.history_btn.setText(_translate("TitleBarWidget", "阅读\n"
"记录"))
        self.feedback_btn.setText(_translate("TitleBarWidget", "反馈"))
        self.min_btn.setText(_translate("TitleBarWidget", "_"))
        self.max_btn.setText(_translate("TitleBarWidget", "口"))
        self.close_btn.setText(_translate("TitleBarWidget", "×"))
        self.bookname_comboBox.setItemText(0, _translate("TitleBarWidget", "书名"))
        self.bookname_comboBox.setItemText(1, _translate("TitleBarWidget", "作者"))
        self.search_btn.setText(_translate("TitleBarWidget", "查"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TitleBarWidget = QtWidgets.QWidget()
    ui = Ui_TitleBarWidget()
    ui.setupUi(TitleBarWidget)
    TitleBarWidget.show()
    sys.exit(app.exec_())

