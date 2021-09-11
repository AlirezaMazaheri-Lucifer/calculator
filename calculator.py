# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class Window(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("CALCULATOR")
		self.setWindowIcon(QIcon("./icon/calculator_icon.svg"))
		self.setGeometry(200 , 200 , 360 , 400)
		self.setFixedSize(360 , 400)
		
		self.UiComponents()

		self.show()

	
	def UiComponents(self):
		self.label = QLabel(self)
		self.label.setStyleSheet("QLabel{border : 4px solid #49c5dc;background : white;background : white;}")
		self.label.setFont(QFont('Arial', 20))
		self.label.setWordWrap(True)
		self.label.setGeometry(5, 5, 350, 70)
		self.label.setAlignment(Qt.AlignRight)


		push1 = QPushButton("1", self)
		push1.setFont(QFont('Arial', 15))
		push1.setStyleSheet("background-color: #e1e1e1;border: 1px solid #000000;color: #000000;")
		push1.setGeometry(5 , 250 , 80 , 40)
		push1.clicked.connect(self.action1)

		push2 = QPushButton("2", self)
		push2.setFont(QFont('Arial', 15))
		push2.setStyleSheet("background-color: #e1e1e1;border: 1px solid #000000;color: #000000;")
		push2.setGeometry(95, 250, 80, 40)
		push2.clicked.connect(self.action2)

		push3 = QPushButton("3", self)
		push3.setFont(QFont('Arial', 15))
		push3.setStyleSheet("background-color: #e1e1e1;border: 1px solid #000000;color: #000000;")
		push3.setGeometry(185, 250, 80, 40)
		push3.clicked.connect(self.action3)

		push4 = QPushButton("4", self)
		push4.setFont(QFont('Arial', 15))
		push4.setStyleSheet("background-color: #e1e1e1;border: 1px solid #000000;color: #000000;")
		push4.setGeometry(5, 200, 80, 40)
		push4.clicked.connect(self.action4)

		push5 = QPushButton("5", self)
		push5.setFont(QFont('Arial', 15))
		push5.setStyleSheet("background-color: #e1e1e1;border: 1px solid #000000;color: #000000;")
		push5.setGeometry(95, 200, 80, 40)
		push5.clicked.connect(self.action5)

		push6 = QPushButton("5", self)
		push6.setFont(QFont('Arial', 15))
		push6.setStyleSheet("background-color: #e1e1e1;border: 1px solid #000000;color: #000000;")
		push6.setGeometry(185, 200, 80, 40)
		push6.clicked.connect(self.action6)

		push7 = QPushButton("7", self)
		push7.setFont(QFont('Arial', 15))
		push7.setStyleSheet("background-color: #e1e1e1;border: 1px solid #000000;color: #000000;")
		push7.setGeometry(5, 150, 80, 40)
		push7.clicked.connect(self.action7)

		push8 = QPushButton("8", self)
		push8.setFont(QFont('Arial', 15))
		push8.setStyleSheet("background-color: #e1e1e1;border: 1px solid #000000;color: #000000;")
		push8.setGeometry(95, 150, 80, 40)
		push8.clicked.connect(self.action8)

		push9 = QPushButton("9", self)
		push9.setFont(QFont('Arial', 15))
		push9.setStyleSheet("background-color: #e1e1e1;border: 1px solid #000000;color: #000000;")
		push9.setGeometry(185, 150, 80, 40)
		push9.clicked.connect(self.action9)

		push0 = QPushButton("0", self)
		push0.setFont(QFont('Arial', 15))
		push0.setStyleSheet("background-color: #e1e1e1;border: 1px solid #000000;color: #000000;")
		push0.setGeometry(5, 300, 80, 40)
		push0.clicked.connect(self.action0)

		push00 = QPushButton("00", self)
		push00.setFont(QFont('Arial', 15))
		push00.setStyleSheet("background-color: #e1e1e1;border: 1px solid #000000;color: #000000;")
		push00.setGeometry(95, 300, 80, 40)
		push00.clicked.connect(self.action00)

		push000 = QPushButton("000", self)
		push000.setFont(QFont('Arial', 15))
		push000.setStyleSheet("background-color: #e1e1e1;border: 1px solid #000000;color: #000000;")
		push000.setGeometry(185, 300, 80, 40)
		push000.clicked.connect(self.action000)

		push_point = QPushButton(".", self)
		push_point.setFont(QFont('Arial', 15))
		push_point.setStyleSheet("background-color: #e1e1e1;border: 1px solid #000000;color: #000000;")
		push_point.setGeometry(5, 350, 260, 40)
		push_point.clicked.connect(self.action_point)

		push_equal = QPushButton("=", self)
		push_equal.setFont(QFont('Arial', 15))
		push_equal.setStyleSheet("background-color: #49c5dc;border: 1px solid #000000;font-weight: bold;color: #000000;")
		push_equal.setGeometry(275, 350, 80, 40)
		push_equal.clicked.connect(self.action_equal)

		push_plus = QPushButton("+", self)
		push_plus.setFont(QFont('Arial', 15))
		push_plus.setStyleSheet("background-color: #fab432;border: 1px solid #000000;font-weight: bold;color: #000000;")
		push_plus.setGeometry(275, 300, 80, 40)
		push_plus.clicked.connect(self.action_plus)

		push_minus = QPushButton("-", self)
		push_minus.setFont(QFont('Arial', 15))
		push_minus.setStyleSheet("background-color: #fab432;border: 1px solid #000000;font-weight: bold;color: #000000;")
		push_minus.setGeometry(275, 250, 80, 40)
		push_minus.clicked.connect(self.action_minus)

		push_mul = QPushButton("*", self)
		push_mul.setFont(QFont('Arial', 15))
		push_mul.setStyleSheet("background-color: #fab432;border: 1px solid #000000;font-weight: bold;color: #000000;")
		push_mul.setGeometry(275, 200, 80, 40)
		push_mul.clicked.connect(self.action_mul)

		push_div = QPushButton("/", self)
		push_div.setFont(QFont('Arial', 15))
		push_div.setStyleSheet("background-color: #fab432;border: 1px solid #000000;font-weight: bold;color: #000000;")
		push_div.setGeometry(275, 150, 80, 40)
		push_div.clicked.connect(self.action_div)

		push_clear = QPushButton("Clear", self)
		push_clear.setFont(QFont('Arial', 15))
		push_clear.setStyleSheet("background-color: #ff7e70;border: 1px solid #000000;color: #000000;")
		push_clear.setGeometry(5, 100, 170, 40)
		push_clear.clicked.connect(self.action_clear)

		# del one character button
		push_del = QPushButton("Delete", self)
		push_del.setFont(QFont('Arial', 15))
		push_del.setStyleSheet("background-color: #ff7e70;border: 1px solid #000000;color: #000000;")
		push_del.setGeometry(185, 100, 170, 40)
		push_del.clicked.connect(self.action_del)


	def action_equal(self):
		# get the label text
		equation = self.label.text()

		try:
			# getting the ans
			ans = eval(equation)
			# setting text to the label
			self.label.setText(str(ans))
		except:
			# setting text to the label
			self.label.setText("Wrong Input")

	def action_plus(self):
		# appending label text
		text = self.label.text()
		self.label.setText(text + " + ")

	def action_minus(self):
		# appending label text
		text = self.label.text()
		self.label.setText(text + " - ")

	def action_div(self):
		# appending label text
		text = self.label.text()
		self.label.setText(text + " / ")

	def action_mul(self):
		# appending label text
		text = self.label.text()
		self.label.setText(text + " * ")

	def action_point(self):
		# appending label text
		text = self.label.text()
		self.label.setText(text + ".")

	def action0(self):
		# appending label text
		text = self.label.text()
		self.label.setText(text + "0")

	def action00(self):
		# appending label text
		text = self.label.text()
		self.label.setText(text + "00")

	def action000(self):
		# appending label text
		text = self.label.text()
		self.label.setText(text + "000")

	def action1(self):
		# appending label text
		text = self.label.text()
		self.label.setText(text + "1")

	def action2(self):
		# appending label text
		text = self.label.text()
		self.label.setText(text + "2")

	def action3(self):
		# appending label text
		text = self.label.text()
		self.label.setText(text + "3")

	def action4(self):
		# appending label text
		text = self.label.text()
		self.label.setText(text + "4")

	def action5(self):
		# appending label text
		text = self.label.text()
		self.label.setText(text + "5")

	def action6(self):
		# appending label text
		text = self.label.text()
		self.label.setText(text + "6")

	def action7(self):
		# appending label text
		text = self.label.text()
		self.label.setText(text + "7")

	def action8(self):
		# appending label text
		text = self.label.text()
		self.label.setText(text + "8")

	def action9(self):
		# appending label text
		text = self.label.text()
		self.label.setText(text + "9")

	def action_clear(self):
		# clearing the label text
		self.label.setText("")

	def action_del(self):
		# clearing a single digit
		text = self.label.text()
		print(text[:len(text)-1])
		self.label.setText(text[:len(text)-1])


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())