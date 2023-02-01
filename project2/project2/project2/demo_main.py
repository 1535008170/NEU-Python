from ctypes.wintypes import HPALETTE
from PyQt5.Qt import *
import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget
from Ui_untitled1 import Ui_Project2_20203578  #导入写的界面类
from Ui_untitled import Ui_MainWindow  #导入写的界面类 
from PyQt5 import QtCore
import logging #写日志


class MyMainWindow(QMainWindow,Ui_Project2_20203578): 
    
    #定义信号
    _signal = QtCore.pyqtSignal(str)

    def __init__(self,parent =None):
        super(MyMainWindow,self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Project2_20203578_陆晓晓")  #设置窗口标题
        #初始化子界面
        #ChildWin=SecondPage()
        #super(ChildWin, self).__init__()
        self.SecondPage=SecondPage()
        #self.pushButton.clicked.connect(self.slot1)
        #self.pushButton.clicked.connect(SecondPage.getData)
        #self.setStyleSheet("background-color:blue;")

        #设置背景
        palette = QPalette()
        pix=QPixmap("project2/city.jpg")

        pix = pix.scaled(self.width(),self.height())

        palette.setBrush(QPalette.Background,QBrush(pix))
        self.setPalette(palette)


    def slot1(self):
        data_str = self.lineEdit.text()
        #print(data_str) 信号发送没问题
        #发送信号
        self._signal.emit(data_str)

class SecondPage(QMainWindow,Ui_MainWindow): #这里
    def __init__(self,parent =None):
        super(SecondPage,self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("二手房详细信息")  #设置窗口标题

'''
    def onClicked(self): #没有用
        #连接信号
        self.MainPage._signal.connect(self.getData)
        print("connect")

    def getData(self, parameter):
        self.lineEdit.setText(parameter)
'''

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()

    #初始化第二个界面
    myWinSecond = SecondPage()
    #myWinSecond.show() 初始化第二个界面时候不能show，要触发了才可以

    #主界面的信号连接副界面的槽函数
    myWin.pushButton.clicked.connect(myWinSecond.show)

    #str=Ui_Project2_20203578.get_str()
    #print(str)

    #写日志文件部分
    logger = logging.getLogger(__name__)
    logger.setLevel(level = logging.INFO)
    handler = logging.FileHandler("log.txt")
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
 
    logger.info("Start print log")
    logger.debug("Do something")
    logger.info("project2_Information of Second hand house")
    logger.error("ERROR message!")
    logger.warning("abc")
    logger.info("Finish your work!Good job!")

    sys.exit(app.exec_())    