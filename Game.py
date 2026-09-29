import json
import random
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QFont, QColor
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout
import SignalBus
from LetterButton import LetterButton

class Game(QWidget):
	SYMBOLS = ["A", "B", "C", "E", "I", "L", "M", "N", "O", "P", "R", "S", "T", "U", "V", "W", "Y"]
	COLORS = [QColor.fromHsv(int((i / 16.0) * 360), 180, 230) for i in range(16)]

	def __init__(self, parent=None):
		super().__init__(parent)

		self.setStyleSheet("border: 2px solid white")

		self.splitLayout = QVBoxLayout(self)
		self.splitLayout.setSpacing(30)

		self.game = QWidget()
		self.label = QLabel()

		SignalBus.bus.difficultySignal.connect(self.init)

		self.sequence = []
		self.sequenceStep = -1
		self.buttons = dict()
		self.showingSequence = False
		self.maxLength = -1

	def init(self, difficulty):
		self.sequence = []
		self.sequenceStep = -1
		self.buttons = dict()
		self.showingSequence = False
		self.maxLength = -1

		while self.splitLayout.count():
			child = self.splitLayout.takeAt(0)
			if child.widget():
				child.widget().deleteLater()

		self.game = QWidget()
		self.splitLayout.addWidget(self.game)

		self.label = QLabel("Obecny wynik: 0")
		self.label.setFont(QFont("Arial", 24, QFont.Weight.Bold))
		self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
		self.label.setContentsMargins(10, 10, 10, 10)
		self.label.setStyleSheet("border: none; background-color: transparent; color: #f1f5f9;")
		self.splitLayout.addWidget(self.label)

		grid_layout = QGridLayout()
		grid_layout.setSpacing(20)
		grid_layout.setContentsMargins(0, 0, 0, 0)

		data = json.loads(open("difficulties.json", "r").read())[difficulty]
		self.maxLength = data["sequenceLength"]
		symbolsToDo = self.SYMBOLS.copy()
		colorsToDo = self.COLORS.copy()

		for x in range(data["x"]):
			for y in range(data["y"]):
				letter = random.choice(symbolsToDo)
				symbolsToDo.remove(letter)
				color = random.choice(colorsToDo)
				colorsToDo.remove(color)
				self.buttons[letter] = LetterButton(letter, self, color)
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
		for e in self.buttons.values():
			e.fail()
		self.sequence = []
		self.sequence.append(random.choice(list(self.buttons.keys())))
		QTimer.singleShot(2000, lambda: self.showSequence())

	def success(self):
		self.buttons[self.sequence[self.sequenceStep]].press()
		self.sequenceStep += 1
		if self.sequenceStep >= len(self.sequence):
			letter = random.choice(list(self.buttons.keys()))
			self.sequence.append(letter)
			if len(self.sequence) > self.maxLength:
				SignalBus.bus.victorySignal.emit()
			else:
				QTimer.singleShot(1000, lambda: self.showSequence())

	def showSequence(self):
		self.showingSequence = True
		self.label.setText(f"Obecny wynik: {len(self.sequence) - 1}")
		self.sequenceStep = -1
		self.showSequenceStep()

	def showSequenceStep(self):
		self.sequenceStep += 1
		self.buttons[self.sequence[self.sequenceStep]].press()
		if len(self.sequence) > self.sequenceStep + 1:
			QTimer.singleShot(1000, lambda: self.showSequenceStep())
		else:
			self.sequenceStep = 0
			self.showingSequence = False