import sys
from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout
from Libraries.Views.Ui_FramelessWindow import FramelessWindow



if __name__=='__main__':
    app=QApplication(sys.argv)
    w=FramelessWindow()
    w.resize(950,400)
    w.show()
    sys.exit(app.exec_())