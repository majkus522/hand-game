from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QFont, QColor
from PySide6.QtWidgets import QWidget, QVBoxLayout, QFrame, QLabel, QPushButton, QGraphicsDropShadowEffect
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
				background-color: #1e293b; 
				border-radius: 15px; 
				border: 2px solid #3b82f6; 
			}
		""")
		menu_frame.setFixedSize(350, 400)

		mainShadow = QGraphicsDropShadowEffect(self)
		mainShadow.setBlurRadius(30)
		mainShadow.setColor(QColor(0, 0, 0, 150))
		mainShadow.setOffset(0, 8)
		menu_frame.setGraphicsEffect(mainShadow)

		frame_layout = QVBoxLayout(menu_frame)
		frame_layout.setContentsMargins(20, 20, 20, 20)
		frame_layout.setSpacing(20)

		title = QLabel("WYGRAŁEŚ")
		title.setStyleSheet("border: none; background-color: transparent; color: #f1f5f9;")
		title.setAlignment(Qt.AlignmentFlag.AlignCenter)
		title.setFont(QFont("Arial", 22, QFont.Weight.Bold))
		frame_layout.addWidget(title)

		repeatButton = QPushButton("Jeszcze raz")
		repeatButton.setFont(QFont("Arial", 14))
		repeatButton.setMinimumHeight(45)
		repeatButton.setStyleSheet("""
			QPushButton
			{
				background-color: #3b82f6;
				color: #f8fafc;
				border-radius: 8px;
			}
			QPushButton:hover
			{
				background-color: #2563eb;
			}
			QPushButton:pressed
			{
				background-color: #1d4ed8;
			}
		""")
		repeatShadow = QGraphicsDropShadowEffect(repeatButton)
		repeatShadow.setBlurRadius(0)
		repeatShadow.setColor("#2f68c5")
		repeatShadow.setOffset(4, 4)
		repeatButton.setGraphicsEffect(repeatShadow)
		repeatButton.clicked.connect(lambda: SignalBus.bus.reloadSignal.emit())
		frame_layout.addWidget(repeatButton)

		closeButton = QPushButton("Wyjdź z gry")
		closeButton.setFont(QFont("Arial", 14))
		closeButton.setMinimumHeight(45)
		closeButton.setStyleSheet("""
			QPushButton
			{
				background-color: #3b82f6;
				color: #f8fafc;
				border-radius: 8px;
			}
			QPushButton:hover
			{
				background-color: #2563eb;
			}
			QPushButton:pressed
			{
				background-color: #1d4ed8;
			}
		""")
		closeShadow = QGraphicsDropShadowEffect(closeButton)
		closeShadow.setBlurRadius(0)
		closeShadow.setColor("#2f68c5")
		closeShadow.setOffset(4, 4)
		closeButton.setGraphicsEffect(closeShadow)
		closeButton.clicked.connect(lambda: self.window().close())
		frame_layout.addWidget(closeButton)

		overlay_layout.addWidget(menu_frame)
		SignalBus.bus.victorySignal.connect(lambda : self.show())