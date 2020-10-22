from PyQt5.QtWidgets import QApplication, QLabel 
import translate
from sys import argv

def user_gui(input): 
	app = QApplication([])
	
	information = translate.search_item(input)
	print('Showing results for:', input)
	#print(information)
	definitions = []
	for item in information:
		#print(item)
		for element in item:
			definitions.append(QLabel(element))
	for item in definitions:
		item.show()

	#label = QLabel()
	#label.show()
	app.exec()

user_gui(*argv[1:])