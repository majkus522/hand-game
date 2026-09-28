from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QWidget, QVBoxLayout, QFrame, QLabel, QPushButton
import SignalBus

class VictoryScreen(QWidget):
	victorySignal = Signal(bool)

	def __init__(self, parent=None):
		super().__init__(parent)

		overlay_layout = QVBoxLayout(self)
		overlay_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
		self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

		menu_frame = QFrame()
		menu_frame.setStyleSheet("""
		            QFrame {
		                background-color: white; 
		                border-radius: 15px; 
		                border: 2px solid #333;
		            }
		        """)
		menu_frame.setFixedSize(350, 400)

		frame_layout = QVBoxLayout(menu_frame)
		frame_layout.setContentsMargins(20, 20, 20, 20)
		frame_layout.setSpacing(15)

		title = QLabel("WYGRAŁEŚ")
		title.setStyleSheet("border: none; background-color: transparent;")
		title.setAlignment(Qt.AlignmentFlag.AlignCenter)
		title.setFont(QFont("Arial", 20, QFont.Weight.Bold))
		frame_layout.addWidget(title)

		button = QPushButton("Jeszcze raz")
		button.setFont(QFont("Arial", 14))
		button.setMinimumHeight(45)
		button.setStyleSheet("""
			QPushButton {
				background-color: #eee;
				border: 1px solid #aaa;
				border-radius: 5px;
			}
			QPushButton:hover {
				background-color: #ddd;
			}
		""")
		button.clicked.connect(lambda: SignalBus.bus.reloadSignal.emit())
		frame_layout.addWidget(button)

		overlay_layout.addWidget(menu_frame)
		SignalBus.bus.victorySignal.connect(lambda : self.show())