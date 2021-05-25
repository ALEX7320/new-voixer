
from PySide2.QtCore import QRunnable,Slot,QThreadPool,QObject,Signal
class WorkerSignals(QObject):
    finished = Signal()

class Worker(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()
    @Slot()
    def run(self):
        try:result = self.fn(*self.args, **self.kwargs)
        except Exception as e:print(e)
        finally:self.signals.finished.emit()  # Done
