from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class DateDialog(QDialog):

    signal_OneParameter=pyqtSignal(str)

    def __init__(self,parent=None):
        super(DateDialog,self).__init__(parent)
        self.setWindowTitle("子窗口发射信号")
        #布局
        layout=QVBoxLayout(self)
        self.label1=QLabel(self)
        self.label1.setText('前者发射内置信号\n后者发射自定义信号')
        
        self.datetime_inner=QDateTimeEdit(self)
        self.datetime_inner.setCalendarPopup(True)
        self.datetime_inner.setDateTime(QDateTime.currentDateTime())

        self.datetime_emit=QDateTimeEdit(self)
        self.datetime_emit.setCalendarPopup(True)
        self.datetime_emit.setDateTime(QDateTime.currentDateTime())

        layout.addWidget(self.label1)
        layout.addWidget(self.datetime_inner)
        layout.addWidget(self.datetime_emit)

        #两个按钮
        buttons=QDialogButtonBox(QDialogButtonBox.Ok|QDialogButtonBox.Cancel,Qt.Horizontal,self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)
        self.datetime_emit.dateTimeChanged.connect(self.emit_signal)
        self.setLayout(layout)

    def emit_signal(self):
        date_str=self.datetime_emit.dateTime().toString()
        self.signal_OneParameter.emit(date_str)
