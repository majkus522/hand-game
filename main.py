import sys
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout
from SimonSays import SimonSays

class MainWindow(QWidget):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("Game")
		self.setStyleSheet("background-color: #000045")
		self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
		self.showFullScreen()

		layout = QVBoxLayout(self)
		layout.setContentsMargins(
			20, 20, 300, 120
		)
		self.game_widget = SimonSays(parent=self)
		layout.addWidget(self.game_widget)

if __name__ == "__main__":
	app = QApplication(sys.argv)

	window = MainWindow()
	window.show()

	sys.exit(app.exec())