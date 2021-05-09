import sys
import datetime
from PyQt5.QtWidgets import QWidget, QLabel, QSizePolicy, QGridLayout, QPushButton, QHBoxLayout, QFrame
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt, QTimer

from clickable_label import *

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.resize(1024,600)
        self.setWindowTitle('PyQt5 sample GUI')
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor('#000000'))
        self.setPalette(p)
        
        self.setCursor(Qt.BlankCursor)
        
        self.style1 = "background-color: black; color: #EEEEEE; font-size: 220px"
        self.style2 = "background-color: white; color: black; font-size: 220px"
        self.stylebutton1 = "background-color: black; color: #000000; font-size: 220px"
        self.stylebutton2 = "background-color: white; color: #FFFFFF; font-size: 220px"
        
        #self.cLabel1 = QPushButton(self)
        self.cLabel1 = ClickableLabel(self)
        self.cLabel1.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.cLabel1.setStyleSheet(self.stylebutton1)
        self.cLabel1.setFrameStyle(QFrame.Box)
        self.cLabel1.clicked.connect(self.switchTimer)
        
        self.labelMinute = QLabel(self)
        self.labelMinute.setText('')
        self.labelMinute.setAlignment(Qt.AlignCenter)
        self.labelMinute.setStyleSheet(self.style1)
 
        self.labelColon1 = QLabel(self)
        self.labelColon1.setText('')
        self.labelColon1.setAlignment(Qt.AlignCenter)
        self.labelColon1.setStyleSheet(self.style1)
        
        self.labelSecond = QLabel(self)
        self.labelSecond.setText('')
        self.labelSecond.setAlignment(Qt.AlignCenter)
        self.labelSecond.setStyleSheet(self.style1)
        
        self.labelColon2 = QLabel(self)
        self.labelColon2.setText('')
        self.labelColon2.setAlignment(Qt.AlignCenter)
        self.labelColon2.setStyleSheet(self.style1)
        
        self.labelMilliSecond = QLabel(self)
        self.labelMilliSecond.setText('')
        self.labelMilliSecond.setAlignment(Qt.AlignCenter)
        self.labelMilliSecond.setStyleSheet(self.style1)
        
        hLayout = QHBoxLayout()
        hLayout.addWidget(self.labelMinute, 1)
        hLayout.addWidget(self.labelColon1)
        hLayout.addWidget(self.labelSecond, 1)
        hLayout.addWidget(self.labelColon2)
        hLayout.addWidget(self.labelMilliSecond, 1)
        self.cLabel1.setLayout(hLayout)

        grid1 = QGridLayout()
        grid1.setSpacing(100)
        grid1.addWidget(self.cLabel1, 0, 0)
        grid1.setContentsMargins(50,50,50,50)
        self.setLayout(grid1)

        self.td_timeSpan = datetime.timedelta(minutes=15, seconds=0)
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateLabel)
        self.colorChanger = QTimer(self)
        self.colorChanger.timeout.connect(self.changeColor)
        self.colorMode = 0
        
    def switchTimer(self):
        if self.timer.isActive() or self.colorChanger.isActive():
            self.stopTimer()
        else:
            self.startTimer()
    
    def startTimer(self):
        self.labelColon1.setText(':')
        self.labelColon2.setText(':')
        self.dt_endTime = datetime.datetime.now() + self.td_timeSpan
        self.timer.start(10)
        
    def stopTimer(self):
        self.timer.stop()
        self.colorChanger.stop()
        self.colorMode = 1
        self.changeColor()
        
    def updateLabel(self):
        td_timeLeft = self.dt_endTime - datetime.datetime.now()
        if td_timeLeft.days >= 0:
            m, s, tms = self.get_m_s_tms(td_timeLeft)
            self.labelMinute.setText(f"{m:02d}")
            self.labelSecond.setText(f"{s:02d}")
            self.labelMilliSecond.setText(f"{tms:02d}")
            self.update()
        else:
            self.timer.stop()
            self.labelMinute.setText("")
            self.labelColon1.setText("")
            self.labelSecond.setText("")
            self.labelColon2.setText("")
            self.labelMilliSecond.setText("")
            self.changeColor()
            self.colorChanger.start(500)
    
    def get_m_s_tms(self, td):
        tms = td.microseconds // 10000
        m, s = divmod(td.seconds, 60)
        return m, s, tms
    
    def changeColor(self):
        if self.colorMode == 0:
            self.colorMode = 1
            p = self.palette()
            p.setColor(self.backgroundRole(), QColor('#FFFFFF'))
            self.setPalette(p)
            self.cLabel1.setStyleSheet(self.stylebutton2)
            self.labelMinute.setStyleSheet(self.style2)
            self.labelColon1.setStyleSheet(self.style2)
            self.labelSecond.setStyleSheet(self.style2)
            self.labelColon2.setStyleSheet(self.style2)
            self.labelMilliSecond.setStyleSheet(self.style2)
            self.update()
        else:
            self.colorMode = 0
            p = self.palette()
            p.setColor(self.backgroundRole(), QColor('#000000'))
            self.setPalette(p)
            self.cLabel1.setStyleSheet(self.stylebutton1)
            self.labelMinute.setStyleSheet(self.style1)
            self.labelColon1.setStyleSheet(self.style1)
            self.labelSecond.setStyleSheet(self.style1)
            self.labelColon2.setStyleSheet(self.style1)
            self.labelMilliSecond.setStyleSheet(self.style1)
            self.update()
