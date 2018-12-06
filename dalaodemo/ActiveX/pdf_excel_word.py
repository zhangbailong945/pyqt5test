import sys

from PyQt5.QtCore import Qt
from PyQt5.QAxContainer import QAxWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog,\
    QMessageBox

from PyQt5.QtGui import QIcon
'''
利用QAxWidget容器，打开相应的COM组件
'''


class AxWidget(QWidget):

    def __init__(self, *args, **kwargs):
        super(AxWidget, self).__init__(*args, **kwargs)
        self.resize(800, 600)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)
        self.axWidget = QAxWidget(self)
        layout.addWidget(self.axWidget)
        layout.addWidget(QPushButton('请选择pdf、excel、word文档',
                                     self, clicked=self.onOpenFile))

    #打开文件，根据文件类型，启动app显示
    def onOpenFile(self):
        path, _ = QFileDialog.getOpenFileName(
            self, '请选择文件', '', 'excel(*.xlsx *.xls);;word(*.docx *.doc);;pdf(*.pdf)')

        if not path:
            return
        if _.find('*.pdf'):
            return self.openOffice(path, 'Word.Application')
        if _.find('*.xls'):
            return self.openOffice(path, 'Excel.Application')
        if _.find('*.pdf'):
            return self.openPdf(path)

    #打开office app
    def openOffice(self, path, app):
        self.axWidget.clear()
        if not self.axWidget.setControl(app):
            return QMessageBox.critical(self, '错误', '没有安装 %s' % app)
        self.axWidget.dynamicCall(
            'SetVisible (bool Visible)', 'false'
        )
        self.axWidget.setProperty('DisplayAlerts', False)
        self.axWidget.setControl(path)

    #打开pdf app
    def openPdf(self, path):
        QMessageBox.critical(self, '错误', '没有安装 Adobe PDF Reader')
        self.axWidget.clear()
        if not self.axWidget.setControl('Adobe PDF Reader'):
            return QMessageBox.critical(self, '错误', '没有安装 Adobe PDF Reader')
        self.axWidget.dynamicCall('LoadFile(const QString&)', path)
    
    #关闭事件
    def closeEvent(self, event):
        self.axWidget.close()
        self.axWidget.clear()
        self.layout().removeWidget(self.axWidget)
        del self.axWidget
        super(AxWidget, self).closeEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = AxWidget()
    demo.show()
    sys.exit(app.exec_())
