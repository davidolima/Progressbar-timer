from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import time

class UI_MAIN(object):
    def setupUI(self, MAIN):
        MAIN.setObjectName("MAIN")
        MAIN.setMinimumSize(520,50)
        MAIN.setWindowTitle("Temporizador")
        MAIN.setMaximumWidth(520)
        MAIN.setMaximumHeight(50)

        self.progressbar = QtWidgets.QProgressBar(MAIN)
        self.progressbar.setGeometry(5,10,510,25)

        self.label = QtWidgets.QLabel(MAIN)
        self.label.setGeometry(20,10,250,25)
        self.label.setText("Coloque o horário de encerramento:")

        self.timer = QTimer(MAIN)
        self.timer.timeout.connect(self.timerEvent)

        self.hourBox = QComboBox(MAIN)
        hours = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23']
        self.hourBox.addItems(hours)
        self.hourBox.move(210, 12)

        self.minBox = QComboBox(MAIN)
        minutes = []
        for i in range(60):
            minutes.append(str(i))

        self.minBox.addItems(minutes)
        self.minBox.move(250, 12)

        self.goButton = QPushButton(MAIN)
        self.goButton.setText("Ok")
        self.goButton.setGeometry(300,10,170,25)
        self.goButton.clicked.connect(self.Okayclicked)
        

        QtCore.QMetaObject.connectSlotsByName(MAIN)

    def Okayclicked(self):
        self.timer.start(1000)
        self.final = QTime(int(self.hourBox.currentText()),int(self.minBox.currentText()),0)
        self.minBox.hide()
        self.hourBox.hide()
        self.goButton.hide()
    
    def timerEvent(self):
        now = QTime.currentTime()

        dif = now.secsTo(self.final)
        difTime = QTime(0,0,0)
        secToNow = difTime.secsTo(now)
        secToFinal = difTime.secsTo(self.final)
        difTime = difTime.addSecs(dif)

        print(self.final, now, dif, difTime)
        if now >= self.final:
            self.timer.stop()
            self.progressbar.setValue(self.progressbar.maximum())
            self.label.setText("O Temporizador Acabou!")
            tempoacabou = QMessageBox()
            tempoacabou.setWindowTitle("Temporizador")
            tempoacabou.setText("O Temporizador Acabou!")
            tempoacabou.setIcon(QMessageBox.Warning)
            tempoacabou.exec_()
            
        else:
            self.progressbar.setMaximum(secToFinal)
            self.progressbar.setValue(secToNow)
            self.label.setText(str(difTime.toString()))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MAIN = QtWidgets.QWidget()
    ui = UI_MAIN()
    ui.setupUI(MAIN)
    MAIN.show()
    sys.exit(app.exec_())
