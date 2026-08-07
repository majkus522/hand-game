import random
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QGridLayout, QLabel, QMainWindow, QVBoxLayout, QWidget
from ColorButton import ColorButton

symbols = ["A", "B", "C", "D"]

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("Hand Game 2.0")
		self.resize(720, 480)

		self.sequence = []
		self.sequenceStep = -1

		self.buttons = []
		self.buttons.append(ColorButton(symbols[0], "#00E676", "#00A859", self))
		self.buttons.append(ColorButton(symbols[1], "#FF5252", "#D32F2F", self))
		self.buttons.append(ColorButton(symbols[2], "#FFEB3B", "#FBC02D", self))
		self.buttons.append(ColorButton(symbols[3], "#448AFF", "#1976D2", self))

		for e in self.buttons:
			e.clicked.connect(self.handleButton)

		# 2x2 Grid Layout for Simon Game arrangement
		grid_layout = QGridLayout()
		grid_layout.setSpacing(20)
		grid_layout.setContentsMargins(0, 0, 0, 0)

		grid_layout.setColumnStretch(0, 1)
		grid_layout.setColumnStretch(1, 0)
		grid_layout.setColumnStretch(2, 0)
		grid_layout.setColumnStretch(3, 1)
		grid_layout.setRowStretch(0, 1)
		grid_layout.setRowStretch(1, 0)
		grid_layout.setRowStretch(2, 0)
		grid_layout.setRowStretch(3, 1)

		for i in range(len(self.buttons)):
			grid_layout.addWidget(self.buttons[i], int(i / 2) + 1, int(i % 2) + 1)

		self.label = QLabel(self)
		self.label.setText("Current score: 0")

		# Main Layout
		main_layout = QVBoxLayout()
		main_layout.addWidget(self.label)
		main_layout.addLayout(grid_layout)

		# Container widget
		container = QWidget()
		container.setLayout(main_layout)
		self.setCentralWidget(container)

		self.sequence.append(random.choice(symbols))
		QTimer.singleShot(1000, lambda: self.showSequence())

	def handleButton(self):
		if self.sender().text() == self.sequence[self.sequenceStep]:
			self.success()
		else:
			self.fail()

	def fail(self):
		self.sequence = []
		self.sequence.append(random.choice(symbols))

	def success(self):
		self.sequenceStep += 1
		if self.sequenceStep >= len(self.sequence):
			self.sequence.append(random.choice(symbols))
			QTimer.singleShot(1000, lambda: self.showSequence())

	def showSequence(self):
		self.label.setText(f"Current score: {len(self.sequence) - 1}")
		self.sequenceStep = -1
		self.showSequenceStep()

	def showSequenceStep(self):
		self.sequenceStep += 1
		self.buttons[symbols.index(self.sequence[self.sequenceStep])].glow()
		if len(self.sequence) > self.sequenceStep + 1:
			QTimer.singleShot(1000, lambda: self.showSequenceStep())
		else:
			self.sequenceStep = 0