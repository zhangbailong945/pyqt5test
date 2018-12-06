import sys,json,chardet

from PyQt5.QtCore import Qt,QRegExp,QSortFilterProxyModel
from PyQt5.QtWidgets import QApplication,QWidget,QHBoxLayout,QComboBox,\
QLabel,QSpacerItem,QSizePolicy
from PyQt5.QtGui import QIcon,QStandardItem,QStandardItemModel

class SortFilterProxyModel(QSortFilterProxyModel):

    def __init__(self,*args,**kwargs):
        super(SortFilterProxyModel,self).__init__(*args,**kwargs)
        #根据Qt.ToolTipRole角色过滤
        self.setFilterRole(Qt.ToolTipRole)
        self._model=QStandardItemModel(self)
        self.setSourceModel(self._model)
    
    def appendRow(self,item):
        self._model.appendRow(item)
    
    def setFilter(self, _):
        #过滤
        #self.sender() #发送者
        #获取上一个下拉框中的item_code
        item_code=self.sender().currentData(Qt.ToolTipRole)
        if not item_code:
            return
        if item_code.endswith("0000"):# 过滤城市
            self.setFilterRegExp(QRegExp(item_code[:-4]+"\d\d00"))
        elif item_code.endswith("00"): #过滤城市一下
            self.setFilterRegExp(QRegExp(item_code[:-2]+"\d\d"))



class Demo(QWidget):

    def __init__(self,parent=None):
        super(Demo,self).__init__(parent)
        self.initUI()
    
    def initUI(self):
        layout=QHBoxLayout()
        #市级以上
        self.comboBox_Province=QComboBox(self,minimumWidth=200)
        #城市
        self.comboBox_City=QComboBox(self,minimumWidth=200)
        #市级以下
        self.comboBox_County=QComboBox(self,minimumWidth=200)
        layout.addWidget(QLabel('省/直辖市/特别行政区',self))
        layout.addWidget(self.comboBox_Province)
        layout.addItem(QSpacerItem(20,20,QSizePolicy.Expanding,QSizePolicy.Minimum))
        layout.addWidget(QLabel("市",self))
        layout.addWidget(self.comboBox_City)
        layout.addItem(QSpacerItem(20,20,QSizePolicy.Expanding,QSizePolicy.Minimum))
        layout.addWidget(QLabel('区/县/镇',self))
        layout.addWidget(self.comboBox_County)
        self.setLayout(layout)
        self.initModel()
        self.initSignal()
        self.initData()
    
    def initSignal(self):
        #初始化信号槽
        self.comboBox_Province.currentIndexChanged.connect(self.city_model.setFilter)
        self.comboBox_City.currentIndexChanged.connect(self.county_model.setFilter)
    
    def initModel(self):
        #初始化模型
        self.province_model=SortFilterProxyModel(self)
        self.city_model=SortFilterProxyModel(self)
        self.county_model=SortFilterProxyModel(self)
        #设置模型
        self.comboBox_Province.setModel(self.province_model)
        self.comboBox_City.setModel(self.city_model)
        self.comboBox_County.setModel(self.county_model)
    
    def initData(self):
        #初始化数据
        datas=open('D:/PyQt5Projects/pyqt5test/dalaodemo/citydata/data.json','rb').read()
        encoding=chardet.detect(datas) or {}
        datas=datas.decode(encoding.get("encoding",'utf-8'))
        datas=json.loads(datas)
        #解析数据
        for data in datas:
            item_code=data.get("item_code")
            item_name=data.get("item_name")
            item=QStandardItem(item_name)
            item.setData(item_code,Qt.ToolTipRole)
            if item_code.endswith("0000"):
                self.province_model.appendRow(item)
            elif item_code.endswith("00"):
                self.city_model.appendRow(item)
            else:
                self.county_model.appendRow(item)


if __name__=="__main__":
    app=QApplication(sys.argv)
    demo=Demo()
    demo.show()
    sys.exit(app.exec_())