import sys
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout
from SimonSays import SimonSays

class MainWindow(QWidget):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("Game")
		self.setStyleSheet("background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #1e293b, stop:1 #0f172a);")
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