import tkinter

from utils.Runnable import StatefulRunnable


class Window(tkinter.Tk):
    def __init__(self):
        super().__init__()


class StatefulWindow(Window, StatefulRunnable):
    def __init__(self):
        StatefulRunnable.__init__(self)
        super().__init__()
