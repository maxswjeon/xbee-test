import tkinter as ttk

from utils.Window import StatefulWindow


class StatusBar(ttk.Frame):
    def __init__(self, parent: StatefulWindow):
        super().__init__(parent)
        self.parent = parent

        self.label = ttk.Label(self)
        self.label.pack(side="left", fill="x")

        # Add a icon to open a new window with the log

    def set_status(self, text: str):
        self.label["text"] = text
