from PySide6.QtCore import QTimer
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QPushButton, QSizePolicy, QGraphicsDropShadowEffect

class LetterButton(QPushButton):
	def __init__(self, text, parent, color):
		super().__init__(text, parent)
		self.setFixedSize(150, 150)

		self.backColor = color.lighter(80).name()
		self.setStyleSheet(f"""
			QPushButton
		    {{
		        color: white;
		        background-color: {color.name()};
		        border: none;
		        border-radius: 10px;
		        font-size: 70px;
		        font-weight: 900;
		        margin-top: 0px;
                margin-left: 0px;
		        padding: 0;
		        transform: translate(7, 7);
		    }}
		    QPushButton[state="press"]
		    {{
		        background-color: {self.backColor};
		        margin-top: 7px;
                margin-left: 7px;
		    }}
		    QPushButton[state="fail"]
		    {{
		        background-color: #ff0000;
		    }}
		""")
		self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

		self.shadow = QGraphicsDropShadowEffect(self)
		self.shadow.setBlurRadius(0)
		self.shadow.setColor(self.backColor)
		self.shadow.setOffset(7, 7)
		self.setGraphicsEffect(self.shadow)

	def press(self):
		self.setProperty("state", "press")
		self.style().polish(self)
		self.shadow.setOffset(0, 0)
		QTimer.singleShot(500, lambda: self.reset())

	def fail(self):
		self.setProperty("state", "fail")
		self.style().polish(self)
		self.shadow.setColor("#cc0000")
		QTimer.singleShot(1000, lambda: self.reset())

	def reset(self):
		self.setProperty("state", "none")
		self.shadow.setOffset(7, 7)
		self.shadow.setColor(self.backColor)
		self.style().polish(self)