from PySide6.QtWidgets import QWidget, QGridLayout
from DifficultyScreen import DifficultyScreen
from Game import Game
import SignalBus
from VictoryScreen import VictoryScreen

class SimonSays(QWidget):
	def __init__(self, parent):
		super().__init__(parent)

		self.setStyleSheet("background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #1e293b, stop:1 #0f172a);")

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

		SignalBus.bus.reloadSignal.connect(self.reload)

	def reload(self):
		self.victoryScreen.hide()
		self.difficultyScreen.show()