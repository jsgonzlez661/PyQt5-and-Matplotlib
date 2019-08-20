# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QFileDialog
import pandas as pd


class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(541, 553)
		MainWindow.setWindowIcon(QIcon('icon.ico'))
		MainWindow.setMinimumSize(QtCore.QSize(541, 553))
		MainWindow.setMaximumSize(QtCore.QSize(541, 553))
		MainWindow.setStyleSheet("QLabel{\n"
"/*color: white;*/\n"
"}\n"
"QPushButton{\n"
"background-color: #54afcd;\n"
"border-radius: 5px;\n"
"color: white;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: #359aca;\n"
"border-radius: 5px;\n"
"color: white;\n"
"}\n"
"QLineEdit{\n"
"background-color: white;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"")
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.label = QtWidgets.QLabel(self.centralwidget)
		self.label.setGeometry(QtCore.QRect(180, 0, 211, 31))
		font = QtGui.QFont()
		font.setPointSize(12)
		self.label.setFont(font)
		self.label.setObjectName("label")
		self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit.setGeometry(QtCore.QRect(10, 60, 371, 31))
		self.lineEdit.setObjectName("lineEdit")
		self.pushButton = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton.setGeometry(QtCore.QRect(390, 60, 141, 31))
		self.pushButton.setObjectName("pushButton")
		self.label_2 = QtWidgets.QLabel(self.centralwidget)
		self.label_2.setGeometry(QtCore.QRect(100, 40, 171, 16))
		font = QtGui.QFont()
		font.setPointSize(10)
		self.label_2.setFont(font)
		self.label_2.setObjectName("label_2")
		self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_2.setGeometry(QtCore.QRect(390, 120, 141, 31))
		self.pushButton_2.setObjectName("pushButton_2")
		self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit_2.setGeometry(QtCore.QRect(10, 120, 371, 31))
		self.lineEdit_2.setObjectName("lineEdit_2")
		self.label_3 = QtWidgets.QLabel(self.centralwidget)
		self.label_3.setGeometry(QtCore.QRect(90, 100, 221, 16))
		font = QtGui.QFont()
		font.setPointSize(10)
		self.label_3.setFont(font)
		self.label_3.setObjectName("label_3")
		self.MplWidget = MplWidget(self.centralwidget)
		self.MplWidget.setGeometry(QtCore.QRect(10, 200, 521, 341))
		self.MplWidget.setObjectName("MplWidget")
		self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_3.setGeometry(QtCore.QRect(200, 160, 141, 31))
		self.pushButton_3.setObjectName("pushButton_3")
		MainWindow.setCentralWidget(self.centralwidget)
		self.pushButton.clicked.connect(self.openFileGDP)
		self.pushButton_2.clicked.connect(self.openFileUPY)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "Analyzing US Economic Data"))
		self.label.setText(_translate("MainWindow", "Analyzing US Economic Data"))
		self.pushButton.setText(_translate("MainWindow", "Load"))
		self.label_2.setText(_translate("MainWindow", "Upload GDP data (csv file)"))
		self.pushButton_2.setText(_translate("MainWindow", "Load"))
		self.label_3.setText(_translate("MainWindow", "Upload unemployment data (csv file)"))
		self.pushButton_3.setText(_translate("MainWindow", "Plot"))
		self.pushButton_3.clicked.connect(self.update_graph)

	def openFileGDP(self):
		fileName = QFileDialog.getOpenFileName(None, 'Open File', "", "CSV File (*.csv)")
		self.lineEdit.setText(fileName[0])  

	def openFileUPY(self):
		fileName = QFileDialog.getOpenFileName(None, 'Open File', "", "CSV File (*.csv)")
		self.lineEdit_2.setText(fileName[0])  

	def update_graph(self):

		gdp_file = self.lineEdit.text()
		upy_file = self.lineEdit_2.text()

		if(gdp_file != "" and upy_file  != ""):
			GDP = pd.read_csv(gdp_file)
			upy = pd.read_csv(upy_file)

			x = pd.DataFrame(GDP['date'])			
			gdp_change = pd.DataFrame(GDP['change-current'])
			unemployment = pd.DataFrame(upy['unemployment'])

			self.MplWidget.canvas.axes.clear()
			self.MplWidget.canvas.axes.plot(x, gdp_change)
			self.MplWidget.canvas.axes.plot(x, unemployment)
			self.MplWidget.canvas.axes.legend(["% GDP change", "% unemployment"],loc='upper right')
			self.MplWidget.canvas.axes.set_title("Year vs %")
			self.MplWidget.canvas.axes.set_ylabel("%")
			self.MplWidget.canvas.axes.grid(linewidth=0.2)
			self.MplWidget.canvas.draw()

from mplwidget import MplWidget

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
