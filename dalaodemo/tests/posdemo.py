import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QIcon,QFont,QCursor


class PosDemo(QWidget):

    def __init__(self,parent=None):
        super(PosDemo,self).__init__(parent)
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('posdemo')
        self.resize(400,300)
    
    def mousePressEvent(self,event):
        if event.button()==Qt.LeftButton:
            self.m_drag=True
            print('global=>x%s'%event.globalX())
            print('globaly=>%s'%event.globalY())
            print('x=>%s'%self.x())
            print('y=>%s'%self.y())
            print('gx-x=>%d'%int(event.globalX()-self.x()))
            print('gy-y=>%d'%int(event.globalY()-self.y()))
            self.m_DragPosition=event.globalPos()-self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.SizeAllCursor))
        
    def mouseReleaseEvent(self,event):
        if event.button()==Qt.LeftButton:
            self.m_drag=False
            print('global=>x%s'%event.globalX())
            print('globaly=>%s'%event.globalY())
            print('x=>%s'%self.x())
            print('y=>%s'%self.y())
            print('gx-x=>%d'%int(event.globalX()-self.x()))
            print('gy-y=>%d'%int(event.globalY()-self.y()))
            self.setCursor(QCursor(Qt.ArrowCursor))
    
    def mouseMoveEvent(self,event):
        if Qt.LeftButton and self.m_drag:
            self.move(event.globalPos()-self.m_DragPosition)
            event.accept()
    

if __name__=='__main__':
    app=QApplication(sys.argv)
    demo=PosDemo()
    demo.show()
    sys.exit(app.exec_())