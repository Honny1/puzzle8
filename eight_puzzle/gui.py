# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui-eigh-puzzle.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import time

from eight_puzzle.puzzle import Puzzle


class Ui_GUI(object):
    def __init__(self):
        super().__init__()
        self.goal = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 0],
        ]
        self.start = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 0],
        ]
        self.comboBoxs = []
        self.lcdNumbers = []
        self.moves = []

    def setupUi(self, GUI):
        GUI.setObjectName("GUI")
        GUI.resize(780, 507)
        self.centralwidget = QtWidgets.QWidget(GUI)
        self.centralwidget.setObjectName("centralwidget")

        self.Start = QtWidgets.QPushButton(self.centralwidget)
        self.Start.setGeometry(QtCore.QRect(530, 430, 104, 36))
        self.Start.setObjectName("Start")
        self.Start.clicked.connect(self.run)

        self.radioButton_s = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_s.setGeometry(QtCore.QRect(470, 210, 113, 25))
        self.radioButton_s.setObjectName("radioButton_s")
        self.radioButton_s.clicked.connect(self.set_goal)
        self.radioButton_s.setChecked(True)

        self.radioButton_g = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_g.setGeometry(QtCore.QRect(610, 210, 113, 25))
        self.radioButton_g.setObjectName("radioButton_g")
        self.radioButton_g.clicked.connect(self.set_start)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(420, 280, 351, 101))
        self.label.setObjectName("label")

        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(40, 440, 341, 24))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setValue(0)

        self.lcdNumber_1 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_1.setGeometry(QtCore.QRect(30, 10, 121, 131))
        self.lcdNumber_1.setDigitCount(1)
        self.lcdNumber_1.setObjectName("lcdNumber_1")

        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setGeometry(QtCore.QRect(160, 10, 121, 131))
        self.lcdNumber_2.setDigitCount(1)
        self.lcdNumber_2.setObjectName("lcdNumber_2")

        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_3.setGeometry(QtCore.QRect(290, 10, 121, 131))
        self.lcdNumber_3.setDigitCount(1)
        self.lcdNumber_3.setObjectName("lcdNumber_3")

        self.lcdNumber_4 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_4.setGeometry(QtCore.QRect(30, 150, 121, 131))
        self.lcdNumber_4.setDigitCount(1)
        self.lcdNumber_4.setObjectName("lcdNumber_4")

        self.lcdNumber_5 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_5.setGeometry(QtCore.QRect(160, 150, 121, 131))
        self.lcdNumber_5.setDigitCount(1)
        self.lcdNumber_5.setObjectName("lcdNumber_5")

        self.lcdNumber_6 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_6.setGeometry(QtCore.QRect(290, 150, 121, 131))
        self.lcdNumber_6.setDigitCount(1)
        self.lcdNumber_6.setObjectName("lcdNumber_6")

        self.lcdNumber_7 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_7.setGeometry(QtCore.QRect(30, 290, 121, 131))
        self.lcdNumber_7.setDigitCount(1)
        self.lcdNumber_7.setObjectName("lcdNumber_7")

        self.lcdNumber_8 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_8.setGeometry(QtCore.QRect(160, 290, 121, 131))
        self.lcdNumber_8.setDigitCount(1)
        self.lcdNumber_8.setObjectName("lcdNumber_8")

        self.lcdNumber_9 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_9.setGeometry(QtCore.QRect(290, 290, 121, 131))
        self.lcdNumber_9.setDigitCount(1)
        self.lcdNumber_9.setObjectName("lcdNumber_9")

        self.comboBox_1 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_1.setGeometry(QtCore.QRect(460, 30, 71, 37))
        self.comboBox_1.setEditable(True)
        self.comboBox_1.setMaxCount(10)
        self.comboBox_1.setObjectName("comboBox_1")
        self.comboBox_1.addItems([str(i) for i in range(9)])

        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(550, 30, 71, 37))
        self.comboBox_2.setEditable(True)
        self.comboBox_2.setMaxCount(10)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItems([str(i) for i in range(9)])

        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(640, 30, 71, 37))
        self.comboBox_3.setEditable(True)
        self.comboBox_3.setMaxCount(10)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItems([str(i) for i in range(9)])

        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(460, 90, 71, 37))
        self.comboBox_4.setEditable(True)
        self.comboBox_4.setMaxCount(10)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItems([str(i) for i in range(9)])

        self.comboBox_5 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_5.setGeometry(QtCore.QRect(550, 90, 71, 37))
        self.comboBox_5.setEditable(True)
        self.comboBox_5.setMaxCount(10)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItems([str(i) for i in range(9)])

        self.comboBox_6 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_6.setGeometry(QtCore.QRect(640, 90, 71, 37))
        self.comboBox_6.setEditable(True)
        self.comboBox_6.setMaxCount(10)
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItems([str(i) for i in range(9)])

        self.comboBox_7 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_7.setGeometry(QtCore.QRect(460, 150, 71, 37))
        self.comboBox_7.setEditable(True)
        self.comboBox_7.setMaxCount(10)
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItems([str(i) for i in range(9)])

        self.comboBox_8 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_8.setGeometry(QtCore.QRect(550, 150, 71, 37))
        self.comboBox_8.setEditable(True)
        self.comboBox_8.setMaxCount(10)
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_8.addItems([str(i) for i in range(9)])

        self.comboBox_9 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_9.setGeometry(QtCore.QRect(640, 150, 71, 37))
        self.comboBox_9.setEditable(True)
        self.comboBox_9.setMaxCount(10)
        self.comboBox_9.setObjectName("comboBox_9")
        self.comboBox_9.addItems([str(i) for i in range(9)])

        GUI.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(GUI)
        self.statusbar.setObjectName("statusbar")
        GUI.setStatusBar(self.statusbar)

        self.retranslateUi(GUI)
        QtCore.QMetaObject.connectSlotsByName(GUI)

        for i in range(1, 10):
            self.comboBoxs.append(getattr(self, "comboBox_" + str(i)))
            self.lcdNumbers.append(getattr(self, "lcdNumber_" + str(i)))

        self.set_values_comboBoxs(self.start)

    def retranslateUi(self, GUI):
        _translate = QtCore.QCoreApplication.translate
        GUI.setWindowTitle(_translate("GUI", "Eight puzzle solver by HONY"))
        self.Start.setText(_translate("GUI", "Start"))
        self.radioButton_s.setText(_translate("GUI", "Start"))
        self.radioButton_g.setText(_translate("GUI", "Goal"))
        self.label.setText(_translate("GUI", ""))

    def run(self):
        if self.radioButton_s.isChecked():
            self.set_start()
        if self.radioButton_g.isChecked():
            self.set_goal()
        if (self.check_duplicite_values(self.get_arr_from_pattern(self.start))
                and self.check_duplicite_values(self.get_arr_from_pattern(self.goal))):
            self.label.setText("Processing...")
            start_time = time.time()
            puzzle = Puzzle(self.start, self.goal)
            self.moves = puzzle.process()
            if self.moves:
                self.label.setText(
                    "Solved in --- {time} seconds ---\nMoves: {moves}".format(
                        time=(
                            time.time() -
                            start_time),
                        moves=len(
                            self.moves) - 1))
                self.horizontalSlider.setMaximum(len(self.moves) - 1)
                self.horizontalSlider.valueChanged.connect(self.valuechange)
                self.set_values_lcdNumbers(self.start)
            else:
                self.label.setText("It has no solution!!")
        else:
            self.label.setText("err - Duplicate values!")

    def valuechange(self):
        self.set_values_lcdNumbers(self.moves[self.horizontalSlider.value()])

    def check_duplicite_values(self, arr):
        return len(arr) == len(set(arr))

    def set_goal(self):
        self.goal = self.get_pattern_from_arr(self.get_values_from_comboBoxs())

    def set_start(self):
        self.start = self.get_pattern_from_arr(
            self.get_values_from_comboBoxs())

    def get_values_from_comboBoxs(self):
        out = []
        for i in range(len(self.comboBoxs)):
            out.append(int(self.comboBoxs[i].currentText()))
        return out

    def get_arr_from_pattern(self, pattern):
        out = []
        for i in range(3):
            for j in range(3):
                out.append(pattern[i][j])
        return out

    def get_pattern_from_arr(self, arr):
        arr.reverse()
        out = []
        for i in range(3):
            row = []
            for j in range(3):
                row.append(arr.pop())
            out.append(row)
        return out

    def set_values_comboBoxs(self, val):
        val = self.get_arr_from_pattern(val)
        for i in range(len(self.comboBoxs)):
            self.comboBoxs[i].setCurrentText(str(val[i]))

    def set_values_lcdNumbers(self, val):
        val = self.get_arr_from_pattern(val)
        for i in range(len(self.lcdNumbers)):
            self.lcdNumbers[i].display(val[i])


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GUI = QtWidgets.QMainWindow()
    ui = Ui_GUI()
    ui.setupUi(GUI)
    GUI.show()
    sys.exit(app.exec_())
