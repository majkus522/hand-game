from PySide6.QtCore import QObject, Signal

class SignalBus(QObject):
	difficultySignal = Signal(str)
	victorySignal = Signal()
	reloadSignal = Signal()

bus = SignalBus()