from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QStackedWidget,QListWidget,\
QLineEdit,QLabel,QRadioButton,QCheckBox,QHBoxLayout,QFormLayout,QVBoxLayout
from PyQt5.QtGui import QIcon
import sys



class StackedWidgetDemo(QWidget):

    def __init__(self,parent=None):
        super(StackedWidgetDemo,self).__init__(parent)
        self.initUI()
    

    def initUI(self):
        self.setGeometry(300,50,10,10)
        self.setWindowTitle("StackedWidget例子")
        self.leftMenu=QListWidget()
        self.leftMenu.insertItem(0,'联系方式')
        self.leftMenu.insertItem(1,'个人信息')
        self.leftMenu.insertItem(2,'教育程度')

        self.stack1=QWidget()
        self.stack2=QWidget()
        self.stack3=QWidget()

        self.stack1UI()
        self.stack2UI()
        self.stack3UI()

        self.stack=QStackedWidget(self)
        self.stack.addWidget(self.stack1)
        self.stack.addWidget(self.stack2)
        self.stack.addWidget(self.stack3)

        hbox=QHBoxLayout(self)
        hbox.addWidget(self.leftMenu)
        hbox.addWidget(self.stack)

        self.setLayout(hbox)
        self.leftMenu.currentRowChanged.connect(self.displayStack)
    

    def stack1UI(self):
        layout=QFormLayout()
        layout.addRow("姓名",QLineEdit())
        layout.addRow("地址",QLineEdit())
        self.stack1.setLayout(layout)
    
    def stack2UI(self):
        layout=QFormLayout()
        sex=QHBoxLayout()
        sex.addWidget(QRadioButton("男"))
        sex.addWidget(QRadioButton("女"))
        layout.addRow(QLabel("性别"),sex)
        layout.addRow("生日",QLineEdit())
        self.stack2.setLayout(layout)
    
    def stack3UI(self):
        layout=QHBoxLayout()
        layout.addWidget(QLabel("科目"))
        layout.addWidget(QCheckBox("物理"))
        layout.addWidget(QCheckBox("高数"))
        self.stack3.setLayout(layout)
    
    def displayStack(self,i):
        self.stack.setCurrentIndex(i)


if __name__=="__main__":
    app=QApplication(sys.argv)
    demo=StackedWidgetDemo()
    demo.show()
    sys.exit(app.exec_())

