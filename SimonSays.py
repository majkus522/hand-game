from PySide6.QtWidgets import QWidget, QGridLayout

from DifficultyScreen import DifficultyScreen
from Game import Game

symbols = ["A", "B", "C", "D", "E", "F", "G", "H"]
gridSize = (4, 2)

class SimonSays(QWidget):
	def __init__(self):
		super().__init__()

		self.setStyleSheet("background-color: #000045")

		mainLayout = QGridLayout(self)
		mainLayout.setContentsMargins(0, 0, 0, 0)
		mainLayout.setSpacing(20)

		self.gameScreen = Game(self)
		mainLayout.addWidget(self.gameScreen, 0, 0)

		self.difficultyScreen = DifficultyScreen(self)
		mainLayout.addWidget(self.difficultyScreen, 0, 0)
		self.difficultyScreen.difficultySelected.connect(self.start_game)

	def start_game(self, difficulty):
		self.difficultyScreen.hide()
		self.gameScreen.difficultySelected.emit(difficulty)