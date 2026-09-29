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

		mainShadow = QGraphicsDropShadowEffect(self)
		mainShadow.setBlurRadius(30)
		mainShadow.setColor(QColor(0, 0, 0, 150))
		mainShadow.setOffset(0, 8)
		menu_frame.setGraphicsEffect(mainShadow)

		frame_layout = QVBoxLayout(menu_frame)
		frame_layout.setContentsMargins(40, 40, 40, 40)
		frame_layout.setSpacing(20)

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

			baseColor = QColor(data[e]["color"])
			hoverColor = baseColor.lighter(120)
			backColor = baseColor.lighter(80)

			button.setStyleSheet(f"""
			    QPushButton
			    {{
			        background-color: {baseColor.name()};
			        color: #f8fafc;
			        border-radius: 8px;
			    }}
			    QPushButton:hover
			    {{
			        background-color: {hoverColor.name()};
			    }}
			    QPushButton:pressed
				{{
			        background-color: {backColor.name()};
			    }}
			""")
			shadow = QGraphicsDropShadowEffect(button)
			shadow.setBlurRadius(0)
			shadow.setColor(backColor)
			shadow.setOffset(4, 4)
			button.setGraphicsEffect(shadow)
			button.clicked.connect(lambda checked=False, current = e: SignalBus.bus.difficultySignal.emit(current))
			frame_layout.addWidget(button)

		overlay_layout.addWidget(menu_frame)
		SignalBus.bus.difficultySignal.connect(lambda: self.hide())