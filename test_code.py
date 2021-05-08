import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.resize(400, 300)
        self.move(400, 300)
        self.setWindowTitle('PyQt5 sample GUI')
        label = QLabel(self)
        label.move(20, 20)
        label.setText('Hello GUI app with PyQt5')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
