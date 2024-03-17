from utils.Background import Background
from utils.StateStore import StateStore


class Runnable:
    def __init__(self):
        super().__init__()
        self.background = Background()


class StatefulRunnable(Runnable, StateStore):
    def __init__(self):
        Runnable.__init__(self)
        super().__init__()
