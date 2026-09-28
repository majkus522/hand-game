from PySide6.QtCore import QObject, Signal

class SignalBus(QObject):
	difficultySignal = Signal(str)
	victorySignal = Signal(bool)

bus = SignalBus()