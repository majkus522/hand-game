import json
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QColor
from PySide6.QtWidgets import QWidget, QVBoxLayout, QFrame, QLabel, QPushButton, QGraphicsDropShadowEffect
import SignalBus

class DifficultyScreen(QWidget):
	def __init__(self, parent=None):
		super().__init__(parent)

		overlay_layout = QVBoxLayout(self)
		overlay_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
		self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

		menu_frame = QFrame()
		menu_frame.setStyleSheet("""
		    QFrame {
		        background-color: #1e293b; 
		        border-radius: 15px; 
		        border: 2px solid #3b82f6; 
		    }
		""")
		menu_frame.setFixedSize(450, 480)

		shadow = QGraphicsDropShadowEffect(self)
		shadow.setBlurRadius(30)
		shadow.setColor(QColor(0, 0, 0, 150))
		shadow.setOffset(0, 8)
		menu_frame.setGraphicsEffect(shadow)

		frame_layout = QVBoxLayout(menu_frame)
		frame_layout.setContentsMargins(40, 40, 40, 40)
		frame_layout.setSpacing(15)

		title = QLabel("Wybierz poziom trudności")
		title.setStyleSheet("border: none; background-color: transparent; color: #f1f5f9;")
		title.setAlignment(Qt.AlignmentFlag.AlignCenter)
		title.setFont(QFont("Arial", 22, QFont.Weight.Bold))
		frame_layout.addWidget(title)

		data = dict(json.loads(open("difficulties.json", "r").read()))
		for e in data.keys():
			button = QPushButton(data[e]["text"])
			button.setFont(QFont("Arial", 14, QFont.Weight.Bold))
			button.setMinimumHeight(45)
			button.setStyleSheet("""
			    QPushButton {
			        background-color: #0f172a;
			        color: #f8fafc;
			        border: 1px solid #3b82f6;
			        border-radius: 8px;
			    }
			    QPushButton:hover {
			        background-color: #2563eb;
			        border: 1px solid #60a5fa;
			    }
			    QPushButton:pressed {
			        background-color: #1d4ed8;
			    }
			""")
			button.clicked.connect(lambda checked=False, current = e: SignalBus.bus.difficultySignal.emit(current))
			frame_layout.addWidget(button)

		overlay_layout.addWidget(menu_frame)
		SignalBus.bus.difficultySignal.connect(lambda: self.hide())