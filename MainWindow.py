import random
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QGridLayout, QLabel, QMainWindow, QVBoxLayout, QWidget
from ColorButton import ColorButton

symbols = ["A", "B", "C", "D", "E", "F", "G", "H"]
gridSize = (4, 2)

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("Hand Game 2.0")
		self.resize(720, 480)
		self.setStyleSheet("""
			QMainWindow
			{
				background-color: #000045;
			}
			QLabel
			{
				color: white;
				font-size: 20px;
			}
		""")

		self.sequence = []
		self.sequenceStep = -1
		self.symbolsRemaining = symbols.copy()

		grid_layout = QGridLayout()
		grid_layout.setSpacing(20)
		grid_layout.setContentsMargins(0, 0, 0, 0)

		self.buttons = []
		self.symbolsOrder = []
		symbolsToDo = symbols.copy()
		for x in range(gridSize[0]):
			for y in range(gridSize[1]):
				letter = random.choice(symbolsToDo)
				self.symbolsOrder.append(letter)
				symbolsToDo.remove(letter)
				self.buttons.append(ColorButton(letter, self))
				grid_layout.addWidget(self.buttons[-1], y + 1, x + 1)

		grid_layout.setColumnStretch(0, 1)
		grid_layout.setColumnStretch(gridSize[0] + 1, 1)
		for i in range(gridSize[0]):
			grid_layout.setColumnStretch(i + 1, 0)

		grid_layout.setRowStretch(0, 1)
		grid_layout.setRowStretch(gridSize[1] + 1, 1)
		for i in range(gridSize[1]):
			grid_layout.setRowStretch(i + 1, 0)

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
		self.sequence.append(random.choice(symbols))
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
		self.buttons[self.symbolsOrder.index(self.sequence[self.sequenceStep])].glow()
		if len(self.sequence) > self.sequenceStep + 1:
			QTimer.singleShot(1000, lambda: self.showSequenceStep())
		else:
			self.sequenceStep = 0
			self.showingSequence = False