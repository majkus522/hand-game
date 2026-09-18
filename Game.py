import json
import random

from PySide6.QtCore import Qt, Signal, QTimer
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QGridLayout

from ColorButton import ColorButton

class Game(QWidget):
	difficultySelected = Signal(str)
	symbols = []

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
		splitLayout.addWidget(self.game, stretch=3)

		self.cameraPanel = QWidget()
		self.cameraPanel.setObjectName("cameraPanel")
		self.cameraPanel.setStyleSheet("#cameraPanel { border: 2px solid white; }")

		cameraInner = QVBoxLayout(self.cameraPanel)
		cameraInner.setContentsMargins(20, 20, 20, 20)
		cameraInner.setSpacing(10)

		self.cameraText = QLabel("Podgląd Kamery")
		self.cameraText.setStyleSheet("color: white")
		self.cameraText.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
		self.cameraText.setFont(QFont("Arial", 22, QFont.Weight.Bold))
		self.cameraText.setWordWrap(True)

		cameraInner.addWidget(self.cameraText)
		cameraInner.addStretch()
		splitLayout.addWidget(self.cameraPanel, stretch=1)

		self.difficultySelected.connect(self.init)

		self.sequence = []
		self.sequenceStep = -1
		self.symbolsRemaining = self.symbols.copy()
		self.buttons = []
		self.symbolsOrder = []
		self.showingSequence = False

	def init(self, difficulty):
		grid_layout = QGridLayout()
		grid_layout.setSpacing(20)
		grid_layout.setContentsMargins(0, 0, 0, 0)

		data = dict(json.loads(open("difficulties.json", "r").read()))[difficulty]
		print(data)

		self.symbols = [chr(x + 65) for x in range(0, data["x"] * data["y"])]
		symbolsToDo = self.symbols.copy()
		self.symbolsRemaining = self.symbols.copy()
		for x in range(data["x"]):
			for y in range(data["y"]):
				letter = random.choice(symbolsToDo)
				self.symbolsOrder.append(letter)
				symbolsToDo.remove(letter)
				self.buttons.append(ColorButton(letter, self))
				grid_layout.addWidget(self.buttons[-1], y + 1, x + 1)

		grid_layout.setColumnStretch(0, 1)
		grid_layout.setColumnStretch(data["x"] + 1, 1)
		for i in range(data["x"]):
			grid_layout.setColumnStretch(i + 1, 0)

		grid_layout.setRowStretch(0, 1)
		grid_layout.setRowStretch(data["y"] + 1, 1)
		for i in range(data["y"]):
			grid_layout.setRowStretch(i + 1, 0)

		self.game.setLayout(grid_layout)

		l = random.choice(self.symbolsRemaining)
		self.symbolsRemaining.remove(l)
		self.sequence.append(l)
		QTimer.singleShot(1000, lambda: self.showSequence())
		self.showingSequence = True

	def keyPressEvent(self, event):
		if self.showingSequence:
			return
		if chr(event.key()) == self.sequence[self.sequenceStep]:
			self.buttons[self.symbolsOrder.index(chr(event.key()))].correct()
			self.success()
		else:
			self.fail()

	def fail(self):
		print("fail")
		for e in self.buttons:
			e.fail()
		self.sequence = []
		self.sequence.append(random.choice(self.symbols))
		QTimer.singleShot(2000, lambda: self.showSequence())

	def success(self):
		self.sequenceStep += 1
		if self.sequenceStep >= len(self.sequence):
			l = random.choice(self.symbolsRemaining)
			self.symbolsRemaining.remove(l)
			self.sequence.append(l)
			QTimer.singleShot(1000, lambda: self.showSequence())

	def showSequence(self):
		for e in self.buttons:
			e.reset()
		self.showingSequence = True
		self.label.setText(f"Current score: {len(self.sequence) - 1}")
		self.sequenceStep = -1
		self.showSequenceStep()

	def showSequenceStep(self):
		self.sequenceStep += 1
		print(self.buttons)
		self.buttons[self.symbolsOrder.index(self.sequence[self.sequenceStep])].glow()
		if len(self.sequence) > self.sequenceStep + 1:
			QTimer.singleShot(1000, lambda: self.showSequenceStep())
		else:
			self.sequenceStep = 0
			self.showingSequence = False