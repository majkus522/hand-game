from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel

class Game(QWidget):
	def __init__(self, parent=None):
		super().__init__(parent)

		splitLayout = QHBoxLayout(self)
		splitLayout.setSpacing(20)

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