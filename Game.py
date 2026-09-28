import json
import random
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QGridLayout
import signalBus
from ColorButton import ColorButton

class Game(QWidget):
	SYMBOLS = ["A", "B", "C", "E", "I", "L", "M", "N", "O", "P", "R", "S", "T", "U", "V", "W", "Y"]

	def __init__(self, parent=None):
		super().__init__(parent)

		splitLayout = QHBoxLayout(self)
		splitLayout.setSpacing(20)

		self.gamePanel = QVBoxLayout()

		self.label = QLabel(self)
		self.label.setText("Current score: 0")
		self.gamePanel.addWidget(self.label)

		self.game = QWidget()
		self.game.setObjectName("game")
		self.game.setStyleSheet("#game { border: 2px solid white; }")
		splitLayout.addWidget(self.game)

		signalBus.bus.difficultySignal.connect(self.init)

		self.sequence = []
		self.sequenceStep = -1
		self.buttons = dict()
		self.showingSequence = False
		self.maxLength = -1

	def init(self, difficulty):
		grid_layout = QGridLayout()
		grid_layout.setSpacing(20)
		grid_layout.setContentsMargins(0, 0, 0, 0)

		data = json.loads(open("difficulties.json", "r").read())[difficulty]
		self.maxLength = data["sequenceLength"]
		symbolsToDo = self.SYMBOLS.copy()
		for x in range(data["x"]):
			for y in range(data["y"]):
				letter = random.choice(symbolsToDo)
				symbolsToDo.remove(letter)
				self.buttons[letter] = ColorButton(letter, self)
				grid_layout.addWidget(self.buttons[letter], y + 1, x + 1)

		grid_layout.setColumnStretch(0, 1)
		grid_layout.setColumnStretch(data["x"] + 1, 1)
		for i in range(data["x"]):
			grid_layout.setColumnStretch(i + 1, 0)

		grid_layout.setRowStretch(0, 1)
		grid_layout.setRowStretch(data["y"] + 1, 1)
		for i in range(data["y"]):
			grid_layout.setRowStretch(i + 1, 0)

		self.game.setLayout(grid_layout)

		self.sequence.append(random.choice(list(self.buttons.keys())))
		self.showingSequence = True
		QTimer.singleShot(1000, lambda: self.showSequence())

	def keyPressEvent(self, event):
		if self.showingSequence:
			return
		if chr(event.key()) == self.sequence[self.sequenceStep]:
			self.success()
		else:
			self.fail()

	def fail(self):
		for e in self.buttons:
			e.fail()
		self.sequence = []
		self.sequence.append(random.choice(list(self.buttons.keys())))
		QTimer.singleShot(2000, lambda: self.showSequence())

	def success(self):
		self.buttons[self.sequence[self.sequenceStep]].correct()
		self.sequenceStep += 1
		if self.sequenceStep >= len(self.sequence):
			letter = random.choice(list(self.buttons.keys()))
			self.sequence.append(letter)
			if len(self.sequence) > self.maxLength:
				signalBus.bus.victorySignal.emit(True)
			else:
				QTimer.singleShot(1000, lambda: self.showSequence())

	def showSequence(self):
		for e in self.buttons.values():
			e.reset()
		self.showingSequence = True
		self.label.setText(f"Current score: {len(self.sequence) - 1}")
		self.sequenceStep = -1
		self.showSequenceStep()

	def showSequenceStep(self):
		self.sequenceStep += 1
		print(self.buttons)
		print(self.sequence)
		self.buttons[self.sequence[self.sequenceStep]].glow()
		if len(self.sequence) > self.sequenceStep + 1:
			QTimer.singleShot(1000, lambda: self.showSequenceStep())
		else:
			self.sequenceStep = 0
			self.showingSequence = False