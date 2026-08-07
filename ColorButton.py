from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QPushButton, QSizePolicy

class ColorButton(QPushButton):
	def __init__(self, text, backgroundColor, pressedColor, parent):
		super().__init__(text, parent)
		self.setFixedSize(100, 100)
		self.backgroundColor = backgroundColor
		self.pressedColor = pressedColor
		self.STYLE_TEMPLATE = """
            QPushButton
            {{
                background-color: {backgroundColor};
                color: white;
                border: none;
                font-weight: bold;
                font-size: 18px;
                margin: 0;
                padding: 0;
                box-shadow: none;
            }}
            QPushButton:pressed
            {{
                background-color: """ + pressedColor + """;
            }}
            """
		self.setStyleSheet(self.STYLE_TEMPLATE.format(backgroundColor=self.backgroundColor))
		self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

	def glow(self):
		self.setStyleSheet(self.STYLE_TEMPLATE.format(backgroundColor=self.pressedColor))
		QTimer.singleShot(500, lambda: self.setStyleSheet(self.STYLE_TEMPLATE.format(backgroundColor=self.backgroundColor)))