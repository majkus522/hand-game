from PySide6.QtWidgets import QWidget, QGridLayout
from DifficultyScreen import DifficultyScreen
from Game import Game
from VictoryScreen import VictoryScreen

class SimonSays(QWidget):
	def __init__(self, parent):
		super().__init__(parent)

		self.setStyleSheet("background-color: #000045")

		mainLayout = QGridLayout(self)
		mainLayout.setContentsMargins(0, 0, 0, 0)
		mainLayout.setSpacing(20)

		self.gameScreen = Game(self)
		mainLayout.addWidget(self.gameScreen, 0, 0)

		self.difficultyScreen = DifficultyScreen(self)
		mainLayout.addWidget(self.difficultyScreen, 0, 0)

		self.victoryScreen = VictoryScreen(self)
		mainLayout.addWidget(self.victoryScreen, 0, 0)
		self.victoryScreen.hide()