import sys
from PyQt5.QtWidgets import QWidget, QLabel, QSizePolicy, QGridLayout, QPushButton, QHBoxLayout
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt, QTimer
#from mdl_timer import Timer
import datetime

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.resize(1024,600)
        self.setWindowTitle('PyQt5 sample GUI')
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor('#080808'))
        self.setPalette(p)
        
        style1 = "background-color: black; color: #EEEEEE; font-size: 220px"
        style2 = "background-color: white; color: black; font-size: 220px"
        
        #label1 = QLabel(self)
        self.button1 = QPushButton(self)
        self.button1.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        #self.button1.setText('15:00:00')
        self.button1.setStyleSheet(style1)
        #label1.setAlignment(Qt.AlignCenter)
        self.button1.clicked.connect(self.switchTimer)
        #self.button1.clicked.connect(lambda: self.UpdateLabel('100'))
        
        #label2 = QLabel(self)
        #label2.setText('hogehoge')
        #label2.setStyleSheet("background-color: green")
        #label2.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        
        
        
        self.labelMinute = QLabel(self)
        self.labelMinute.setText('15')
        self.labelMinute.setAlignment(Qt.AlignCenter)
        #self.labelMinute.resize(200, 500)
        #self.labelMinute.setGeometry(0, 0, 200, 500)
        self.labelMinute.setStyleSheet(style1)
 
        self.labelColon1 = QLabel(self)
        self.labelColon1.setText(':')
        self.labelColon1.setAlignment(Qt.AlignCenter)
        #self.labelColon1.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.labelColon1.setStyleSheet(style1)
        
        self.labelSecond = QLabel(self)
        self.labelSecond.setText('00')
        self.labelSecond.setAlignment(Qt.AlignCenter)
        #self.labelSecond.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        #self.labelSecond.resize(200, 500)
        #self.labelSecond.setGeometry(200, 0, 200, 500)
        self.labelSecond.setStyleSheet(style1)
        
        self.labelColon2 = QLabel(self)
        self.labelColon2.setText(':')
        self.labelColon2.setAlignment(Qt.AlignCenter)
        #self.labelColon2.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.labelColon2.setStyleSheet(style1)
        
        self.labelMilliSecond = QLabel(self)
        self.labelMilliSecond.setText('00')
        self.labelMilliSecond.setAlignment(Qt.AlignCenter)
        #self.labelMilliSecond.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        #self.labelMilliSecond.resize(200, 500)
        self.labelMilliSecond.setStyleSheet(style1)
        
        hLayout = QHBoxLayout()
        hLayout.addWidget(self.labelMinute, 1)
        hLayout.addWidget(self.labelColon1)
        hLayout.addWidget(self.labelSecond, 1)
        hLayout.addWidget(self.labelColon2)
        hLayout.addWidget(self.labelMilliSecond, 1)
        self.button1.setLayout(hLayout)

        grid1 = QGridLayout()
        grid1.setSpacing(100)
        grid1.addWidget(self.button1, 0, 0)
        grid1.setContentsMargins(50,50,50,50)
        #grid1.addWidget(label2, 1, 1)
        self.setLayout(grid1)
        
        #self.TIME_INIT = 15 * 60 * 100
        #self.time = self.TIME_INIT
        self.td_timeSpan = datetime.timedelta(minutes=1)
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateLabel)
        
    def switchTimer(self):
        if self.timer.isActive():
            self.stopTimer()
        else:
            self.startTimer()
    
    def startTimer(self):
        self.dt_endTime = datetime.datetime.now() + self.td_timeSpan
        self.timer.start(10)
        
    def stopTimer(self):
        self.timer.stop()
        
    def updateLabel(self):
        #timeLeft = self.endTime - datetime.datetime.now()
        td_timeLeft = self.dt_endTime - datetime.datetime.now()
        if td_timeLeft.days >= 0:
            #minute = self.time // (60 * 100)
            #tmp = self.time % (60 * 100)
            #second = tmp // 100
            #milliSecond = tmp % 100
            m, s, tms = self.get_m_s_tms(td_timeLeft)
            self.labelMinute.setText(f"{m:02d}")
            self.labelSecond.setText(f"{s:02d}")
            self.labelMilliSecond.setText(f"{tms:02d}")
            self.update()
        else:
            self.stopTimer()
    
    def get_m_s_tms(self, td):
        tms = td.microseconds // 10000
        m, s = divmod(td.seconds, 60)
        return m, s, tms
