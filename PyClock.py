#!/usr/bin/python
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6 import uic
from PyQt6.QtCore import QTimer, QTime, Qt
import sys

class AppClock(QWidget):
    def __init__(self):
        super().__init__()
        
        uic.loadUi('clock.ui', self)
        self.setFixedSize(540, 164)
        
       
        self.displayTime()


        # timer is a instance of QTimer
        timer = QTimer(self)
        timer.timeout.connect(self.displayTime)
        timer.start(1000) #1 second


    def displayTime(self):
        currentTime = QTime.currentTime()
        displayText = currentTime.toString('hh:mm:ss')
        self.label_clock.setText(displayText) #


app = QApplication(sys.argv)
window = AppClock()
window.show()
app.exec()