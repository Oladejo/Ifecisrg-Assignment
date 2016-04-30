__author__ = 'azeez'

import sys
from PyQt4 import QtGui, QtCore

class Calculator(QtGui.QWidget):
    myData = []
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)

        self.setWindowTitle('Calculator')
        self.setGeometry(500, 500, 500, 500)
        self.myLayout()

    def myLayout(self):
        self.labelWelcome = QtGui.QLabel('Welcome to calculator', self)
        self.labelWelcome.move(150, 10)

        self.totalLabel = QtGui.QLabel('Total Values to compute', self)
        self.totalLabel.move(20, 50)

        self.totalText = QtGui.QLineEdit(self)
        self.totalText.move(20, 70)

        self.dataLabel = QtGui.QLabel('Data', self)
        self.dataLabel.move(20, 110)

        self.dataText = QtGui.QLineEdit(self)
        self.dataText.move(20, 130)

        self.nextBtn = QtGui.QPushButton('Next', self)
        self.nextBtn.move(150, 130)
        self.nextBtn.clicked.connect(self.nextData)

        self.sumLabel = QtGui.QLabel('Sum', self)
        self.sumLabel.move(20, 170)

        self.sumText = QtGui.QLineEdit(self)
        self.sumText.move(20, 190)

        self.averageLabel = QtGui.QLabel('Average', self)
        self.averageLabel.move(250, 170)

        self.averageText = QtGui.QLineEdit(self)
        self.averageText.move(250, 190)

        self.processBtn = QtGui.QPushButton('Process', self)
        self.processBtn.move(20, 250)
        self.processBtn.clicked.connect(self.processData)

        self.ResetBtn = QtGui.QPushButton('Reset', self)
        self.ResetBtn.move(130, 250)
        self.ResetBtn.clicked.connect(self.clearField)

        self.exitBtn = QtGui.QPushButton('Exit', self)
        self.exitBtn.move(250, 250)
        self.exitBtn.clicked.connect(QtCore.QCoreApplication.instance().quit)


        self.centerScreen()

    #accept data and click next button to save it
    def nextData(self):
        if len(self.dataText.text()) != 0:
            self.rawData = self.dataText.text()
            self.myData.append(self.rawData)
            self.dataText.clear()
            self.dataText.setFocus(True)
        else:
            QtGui.QMessageBox.information(self, "Information", "Box is empty, Please try to enter data and click next!!!", QtGui.QMessageBox.Cancel, QtGui.QMessageBox.NoButton)


    #process the data
    def processData(self):
        totalValue = int(self.totalText.text())
        if totalValue > len(self.myData):
            a = totalValue - len(self.myData)
            QtGui.QMessageBox.information(self, "Information", "Remain "+str(a)+" value to complete!!!", QtGui.QMessageBox.Cancel, QtGui.QMessageBox.NoButton)

        elif totalValue < len(self.myData):
            a = len(self.myData) - totalValue
            QtGui.QMessageBox.information(self, "Information", "Data exceed the total value we want by "+str(a)+" values!!!", QtGui.QMessageBox.Cancel, QtGui.QMessageBox.NoButton)

        else:
            i = 0
            mySum = 0
            while i < totalValue:
                mySum += int(self.myData[i])
                i += 1
            self.averageText.setText(str(mySum/totalValue))
            self.sumText.setText(str(mySum))
            self.myData.clear()

    #clear all filed
    def clearField(self):
        self.dataText.clear()
        self.averageText.clear()
        self.totalText.clear()
        self.dataText.clear()
        self.myData.clear()
        self.sumText.clear()


       #method to set GUI to center of the screen
    def centerScreen(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width())/2,
                  (screen.height() - size.height())/2)



def main():
    app = QtGui.QApplication(sys.argv)
    showCal = Calculator()
    showCal.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
