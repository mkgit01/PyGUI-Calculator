from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(361, 588)
        MainWindow.setWindowIcon(QtGui.QIcon('logo.ico'))
        MainWindow.setStyleSheet("background-color: rgb(30, 30, 30);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.outputLabel = QtWidgets.QLabel(self.centralwidget)
        self.outputLabel.setGeometry(QtCore.QRect(10, 10, 341, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.outputLabel.setFont(font)
        self.outputLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.outputLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.outputLabel.setLineWidth(2)
        self.outputLabel.setStyleSheet("background-color: rgb(179, 179, 179);")
        self.outputLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.outputLabel.setObjectName("outputLabel")

        self.percentButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("%"))
        self.percentButton.setGeometry(QtCore.QRect(100, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.percentButton.setFont(font)
        self.percentButton.setStyleSheet("color: rgb(223, 223, 223);\n"
"background-color: rgb(255, 116, 16);")
        self.percentButton.setObjectName("percentButton")
        
        self.cButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("C"))
        self.cButton.setGeometry(QtCore.QRect(10, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.cButton.setFont(font)
        self.cButton.setStyleSheet("color: rgb(223, 223, 223);\n"
"background-color: rgb(255, 0, 0);")
        self.cButton.setObjectName("cButton")
        self.arrowButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.remove_it())
        self.arrowButton.setGeometry(QtCore.QRect(190, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.arrowButton.setFont(font)
        self.arrowButton.setStyleSheet("color: rgb(223, 223, 223);\n"
"background-color: rgb(255, 116, 16);")
        self.arrowButton.setObjectName("arrowButton")
        self.divideButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("/"))
        self.divideButton.setGeometry(QtCore.QRect(275, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.divideButton.setFont(font)
        self.divideButton.setStyleSheet("color: rgb(223, 223, 223);\n"
"background-color: rgb(255, 116, 16);")
        self.divideButton.setObjectName("divideButton")
        self.multiplyButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("*"))
        self.multiplyButton.setGeometry(QtCore.QRect(275, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.multiplyButton.setFont(font)
        self.multiplyButton.setStyleSheet("color: rgb(223, 223, 223);\n"
"background-color: rgb(255, 116, 16);")
        self.multiplyButton.setObjectName("multiplyButton")
        self.nineButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("9"))
        self.nineButton.setGeometry(QtCore.QRect(190, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.nineButton.setFont(font)
        self.nineButton.setStyleSheet("background-color: rgb(77, 77, 77);\n"
"color: rgb(223, 223, 223);")
        self.nineButton.setObjectName("nineButton")
        self.sevenButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("7"))
        self.sevenButton.setGeometry(QtCore.QRect(10, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.sevenButton.setFont(font)
        self.sevenButton.setStyleSheet("background-color: rgb(77, 77, 77);\n"
"color: rgb(223, 223, 223);")
        self.sevenButton.setObjectName("sevenButton")
        self.eightButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("8"))
        self.eightButton.setGeometry(QtCore.QRect(100, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.eightButton.setFont(font)
        self.eightButton.setStyleSheet("background-color: rgb(77, 77, 77);\n"
"color: rgb(223, 223, 223);")
        self.eightButton.setObjectName("eightButton")
        self.minusButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("-"))
        self.minusButton.setGeometry(QtCore.QRect(275, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.minusButton.setFont(font)
        self.minusButton.setStyleSheet("color: rgb(223, 223, 223);\n"
"background-color: rgb(255, 116, 16);")
        self.minusButton.setObjectName("minusButton")
        self.sixButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("6"))
        self.sixButton.setGeometry(QtCore.QRect(190, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.sixButton.setFont(font)
        self.sixButton.setStyleSheet("background-color: rgb(77, 77, 77);\n"
"color: rgb(223, 223, 223);")
        self.sixButton.setObjectName("sixButton")
        self.fourButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("4"))
        self.fourButton.setGeometry(QtCore.QRect(10, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.fourButton.setFont(font)
        self.fourButton.setStyleSheet("background-color: rgb(77, 77, 77);\n"
"color: rgb(223, 223, 223);")
        self.fourButton.setObjectName("fourButton")
        self.fiveButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("5"))
        self.fiveButton.setGeometry(QtCore.QRect(100, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.fiveButton.setFont(font)
        self.fiveButton.setStyleSheet("background-color: rgb(77, 77, 77);\n"
"color: rgb(223, 223, 223);")
        self.fiveButton.setObjectName("fiveButton")
        self.addButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("+"))
        self.addButton.setGeometry(QtCore.QRect(275, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.addButton.setFont(font)
        self.addButton.setStyleSheet("color: rgb(223, 223, 223);\n"
"background-color: rgb(255, 116, 16);")
        self.addButton.setObjectName("addButton")
        self.threeButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("3"))
        self.threeButton.setGeometry(QtCore.QRect(190, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.threeButton.setFont(font)
        self.threeButton.setStyleSheet("background-color: rgb(77, 77, 77);\n"
"color: rgb(223, 223, 223);")
        self.threeButton.setObjectName("threeButton")
        self.oneButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("1"))
        self.oneButton.setGeometry(QtCore.QRect(10, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.oneButton.setFont(font)
        self.oneButton.setStyleSheet("background-color: rgb(77, 77, 77);\n"
"color: rgb(223, 223, 223);")
        self.oneButton.setObjectName("oneButton")
        self.twoButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("2"))
        self.twoButton.setGeometry(QtCore.QRect(100, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.twoButton.setFont(font)
        self.twoButton.setStyleSheet("background-color: rgb(77, 77, 77);\n"
"color: rgb(223, 223, 223);")
        self.twoButton.setObjectName("twoButton")
        self.equalButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.math_it())
        self.equalButton.setGeometry(QtCore.QRect(275, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.equalButton.setFont(font)
        self.equalButton.setStyleSheet("color: rgb(223, 223, 223);\n"
"background-color: rgb(0, 0, 255);")
        self.equalButton.setObjectName("equalButton")
        self.decimalButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.dot_it())
        self.decimalButton.setGeometry(QtCore.QRect(190, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.decimalButton.setFont(font)
        self.decimalButton.setStyleSheet("background-color: rgb(77, 77, 77);\n"
"color: rgb(223, 223, 223);")
        self.decimalButton.setObjectName("decimalButton")
        self.plusminusButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.plus_minus_it())
        self.plusminusButton.setGeometry(QtCore.QRect(10, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.plusminusButton.setFont(font)
        self.plusminusButton.setStyleSheet("background-color: rgb(77, 77, 77);\n"
"color: rgb(223, 223, 223);")
        self.plusminusButton.setObjectName("plusminusButton")
        self.zeroButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("0"))
        self.zeroButton.setGeometry(QtCore.QRect(100, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.zeroButton.setFont(font)
        self.zeroButton.setStyleSheet("background-color: rgb(77, 77, 77);\n"
"color: rgb(223, 223, 223);")
        self.zeroButton.setObjectName("zeroButton")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 361, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    # Remove character
    def remove_it(self):
        # Grab what's on the screen already
        screen = self.outputLabel.text()
        # Remove last item in list/string
        screen = screen[:-1]
        # Output back to the screen
        self.outputLabel.setText(screen)

    # Let's Do Some Math!
    def math_it(self):
        # Grab what's on the screen already
        screen = self.outputLabel.text()
        try:
            # Do the math
            answer = eval(screen)
            # Output answer to the screen
            self.outputLabel.setText(str(answer))
        except:
            # Output error to the screen
            self.outputLabel.setText("ERROR")

    # Change from positive/negative
    def plus_minus_it(self):
        # Grab what's on the screen already
        screen = self.outputLabel.text()
        if "-" in screen:
            self.outputLabel.setText(screen.replace("-", ""))
        else:
            self.outputLabel.setText(f'-{screen}')

    # Add a decimal
    def dot_it(self):
        # Grab what's on the screen already
        screen = self.outputLabel.text()

        if screen[-1] == ".":
            pass
        else:
            self.outputLabel.setText(f'{screen}.')         

    def press_it(self, pressed):
        if pressed == "C":
            self.outputLabel.setText("0")
        else:
            # Check to see if starts with 0 and delete 0
            if self.outputLabel.text() == "0":
                self.outputLabel.setText("")    
            # Concatenate the pressed button with what was there already
            self.outputLabel.setText(f'{self.outputLabel.text()}{pressed}')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.outputLabel.setText(_translate("MainWindow", "0"))
        self.cButton.setText(_translate("MainWindow", "C"))
        self.percentButton.setText(_translate("MainWindow", "%")) 
        self.arrowButton.setText(_translate("MainWindow", "<<"))
        self.divideButton.setText(_translate("MainWindow", "/"))
        self.multiplyButton.setText(_translate("MainWindow", "x"))
        self.nineButton.setText(_translate("MainWindow", "9"))
        self.sevenButton.setText(_translate("MainWindow", "7"))
        self.eightButton.setText(_translate("MainWindow", "8"))
        self.minusButton.setText(_translate("MainWindow", "-"))
        self.sixButton.setText(_translate("MainWindow", "6"))
        self.fourButton.setText(_translate("MainWindow", "4"))
        self.fiveButton.setText(_translate("MainWindow", "5"))
        self.addButton.setText(_translate("MainWindow", "+"))
        self.threeButton.setText(_translate("MainWindow", "3"))
        self.oneButton.setText(_translate("MainWindow", "1"))
        self.twoButton.setText(_translate("MainWindow", "2"))
        self.equalButton.setText(_translate("MainWindow", "="))
        self.decimalButton.setText(_translate("MainWindow", "."))
        self.plusminusButton.setText(_translate("MainWindow", "+/-"))
        self.zeroButton.setText(_translate("MainWindow", "0"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
