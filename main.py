import sys
from PySide6.QtWidgets import QApplication
from SimonSays import SimonSays

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = SimonSays()
	window.resize(1500, 800)
	window.show()
	sys.exit(app.exec())