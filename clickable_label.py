from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt, pyqtSignal, QTimer
 
class ClickableLabel(QLabel):
    
    clicked = pyqtSignal()
    dblclicked = pyqtSignal()
    clickcount = 0
    
    def __init__(self, parent=None):
        super(ClickableLabel, self).__init__(parent)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.judgeClick)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clickcount += 1
            if self.clickcount >= 2:
                self.judgeClick()
            elif self.timer.isActive() != True:
                self.timer.start(200)
        return QLabel.mousePressEvent(self, event)
    
    def judgeClick(self):
        self.timer.stop()
        if self.clickcount >= 2:
            self.clickcount = 0
            self.dblclicked.emit()
        elif self.clickcount == 1:
            self.clickcount = 0
            self.clicked.emit()
