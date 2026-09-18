from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QWidget, QVBoxLayout, QFrame, QLabel, QPushButton

class DifficultyScreen(QWidget):
	difficultySelected = Signal(str)

	def __init__(self, parent=None):
		super().__init__(parent)

		overlay_layout = QVBoxLayout(self)
		overlay_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
		self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
		self.setStyleSheet("background-color: rgba(0, 0, 0, 150);")

		menu_frame = QFrame()
		menu_frame.setStyleSheet("""
		            QFrame {
		                background-color: white; 
		                border-radius: 15px; 
		                border: 2px solid #333;
		            }
		        """)
		menu_frame.setFixedSize(350, 300)

		frame_layout = QVBoxLayout(menu_frame)
		frame_layout.setContentsMargins(20, 20, 20, 20)
		frame_layout.setSpacing(15)

		title = QLabel("Choose Difficulty")
		title.setStyleSheet("border: none; background-color: transparent;")
		title.setAlignment(Qt.AlignmentFlag.AlignCenter)
		title.setFont(QFont("Arial", 20, QFont.Weight.Bold))
		frame_layout.addWidget(title)

		self.btn_easy = QPushButton("Easy")
		self.btn_normal = QPushButton("Normal")
		self.btn_hard = QPushButton("Hard")

		for btn in (self.btn_easy, self.btn_normal, self.btn_hard):
			btn.setFont(QFont("Arial", 14))
			btn.setMinimumHeight(45)
			btn.setStyleSheet("""
		                QPushButton {
		                    background-color: #eee;
		                    border: 1px solid #aaa;
		                    border-radius: 5px;
		                }
		                QPushButton:hover {
		                    background-color: #ddd;
		                }
		            """)
			frame_layout.addWidget(btn)

		self.btn_easy.clicked.connect(lambda: self.difficultySelected.emit("Bardzo łatwe"))
		self.btn_normal.clicked.connect(lambda: self.difficultySelected.emit("Łatwe"))
		self.btn_hard.clicked.connect(lambda: self.difficultySelected.emit("Normalne"))
		self.btn_hard.clicked.connect(lambda: self.difficultySelected.emit("Trudne"))
		self.btn_hard.clicked.connect(lambda: self.difficultySelected.emit("Bardzo trudne"))

		overlay_layout.addWidget(menu_frame)