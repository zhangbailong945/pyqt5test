from PyQt5.QtCore import QTimer,Qt,QDateTime,QUrl
from PyQt5.QtWidgets import QApplication,QWidget,QGridLayout,QListWidget,QLabel,\
QVBoxLayout,QHBoxLayout,QPushButton
from PyQt5.QtWebEngineWidgets import *
import sys

#嵌入javascript ,pyqt5与javascript交互


class TimerDemo(QWidget):

    def __init__(self,parent=None):
        super(TimerDemo,self).__init__(parent)
        self.initUI()
    
    def initUI(self):
        layout=QVBoxLayout()
        self.browser=QWebEngineView()
        html="""
        <html>
        <head>
        <title>PyQt5嵌入html5</title>
        <script type="text/javascript">
        function completeAndReturnName(){
            var fname=document.getElementById('fname').value;
            var lname=document.getElementById('lname').value;
            var full=fname+' '+lname;
            document.getElementById('fullname').value=full;
            document.getElementById('submit-btn').style.display='block';
            return full;

        }
        </script>
        </head>
        <body>
        <h1>Hello PyQt5!</h1>
        <form>
        <label for='fname'>Frist Name</label>
        <input type='text' name='fname' id='fname' />
        <label for='lname'>Last Name</label>
        <input type='text' name='lname' id='lname' />
        <label for='fullname'>Full Name</label>
        <input type='text' name='fullname' id='fullname' />
        <input type='submit' style='display:none;' id='submit-btn' />
        </form>
        </body>
        </html>
        """
        self.browser.setHtml(html)

        #按钮用于挑用js代码
        self.btnJs=QPushButton('设置全名')
        def js_callback(result):
            print(result)
        
        def complete_name():
            self.browser.page().runJavaScript('completeAndReturnName();',js_callback)
        
        #按钮连接'complete_name'槽函数
        self.btnJs.clicked.connect(complete_name)
        

        layout.addWidget(self.browser)
        layout.addWidget(self.btnJs)
        self.setLayout(layout)


if __name__=='__main__':
    app=QApplication(sys.argv)
    demo=TimerDemo()
    demo.show()
    sys.exit(app.exec_())