import sys

from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea,QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow)
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtWidgets, uic

from itertools import chain

import translate

def main():
	app = QApplication(sys.argv)
	main = User_gui()
	sys.exit(app.exec_())


class User_gui(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.scroll = QScrollArea()
		self.widget = QWidget()
		self.vbox = QVBoxLayout()

		self.vbox.addWidget(QLabel('Translate it!'))
		user_queue = input('Enter lookup: ')
		print('Showing results for:', user_queue)
		
		information = translate.search_item(user_queue)
		
		for item in information:
				for element in item:
					self.vbox.addWidget(QLabel(element))

		self.widget.setLayout(self.vbox)

		self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
		self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
		self.scroll.setWidgetResizable(True)
		self.scroll.setWidget(self.widget)
		
		self.setCentralWidget(self.scroll)
		self.setGeometry(500, 500, 500, 500)
		self.setWindowTitle('Translate It!')
		self.show()

		return

if __name__ == '__main__': 
    main()