import sys

from PyQt5.QtWidgets import QApplication, QLabel, QWidget

import translate

def main():
	app = QApplication(sys.argv)
	gui = User_gui()
	sys.exit(app.exec_())

class User_gui(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		user_queue = input('Enter lookup: ')
		print('Showing results for:', user_queue)
		information = translate.search_item(user_queue)
		definitions = []
		for item in information:
				for element in item:
					definitions.append(QLabel(element, self))
		count = 1
		for item in definitions:
			item.move(0, count * 13)
			count +=1
			item.show()
		self.setGeometry(500, 500, 500, 500)
		self.setWindowTitle('Translate It!')
		self.show()

if __name__ == '__main__': 
    main()