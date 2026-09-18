import random
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QGridLayout, QLabel, QMainWindow, QVBoxLayout, QWidget
from ColorButton import ColorButton

import sys
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

from DifficultyDialog import DifficultyDialog

symbols = ["A", "B", "C", "D", "E", "F", "G", "H"]
gridSize = (4, 2)

class SimonSays(QWidget):
	def __init__(self):
		super().__init__()

		self.setStyleSheet("background-color: #000045")

		mainLayout = QVBoxLayout(self)
		mainLayout.setContentsMargins(20, 20, 20, 20)
		mainLayout.setSpacing(20)

		splitLayout = QHBoxLayout()
		splitLayout.setSpacing(20)
		mainLayout.addLayout(splitLayout)

		self.gamePanel = QWidget()
		self.gamePanel.setObjectName("gamePanel")
		self.gamePanel.setStyleSheet("#gamePanel { border: 2px solid white; }")
		splitLayout.addWidget(self.gamePanel, stretch=3)

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

		dialog = DifficultyDialog(self)
		result = dialog.exec()