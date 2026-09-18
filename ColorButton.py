from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QPushButton, QSizePolicy

class ColorButton(QPushButton):
	def __init__(self, text, parent):
		super().__init__(text, parent)
		self.setFixedSize(200, 200)
		self.STYLE_TEMPLATE = """
            QPushButton
            {{
                color: {color};
                border: none;
                font-size: 60px;
                font-weight: 700;
                margin: 0;
                padding: 0;
                box-shadow: none;
            }}
            """
		self.setStyleSheet(self.STYLE_TEMPLATE.format(color="white"))
		self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

	def glow(self):
		self.setStyleSheet(self.STYLE_TEMPLATE.format(color="yellow"))
		QTimer.singleShot(500, lambda: self.reset())

	def correct(self):
		self.setStyleSheet(self.STYLE_TEMPLATE.format(color="green"))

	def reset(self):
		self.setStyleSheet(self.STYLE_TEMPLATE.format(color="white"))

	def fail(self):
		self.setStyleSheet(self.STYLE_TEMPLATE.format(color="red"))
		QTimer.singleShot(1000, lambda: self.reset())