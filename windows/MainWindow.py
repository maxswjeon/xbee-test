import tkinter.ttk as ttk

from components.ModuleSearchBar import ModuleSearchBar
from components.ServerUrlBar import ServerUrlBar
from components.StatusBar import StatusBar
from components.SettingsBar import SettingsBar

from utils.Window import StatefulWindow
from utils.XBee import XBee


class MainWindow(StatefulWindow):
    def __init__(self):
        super().__init__()
        self.protocol("WM_DELETE_WINDOW", self.__on_close)

        self.title("XBee Range Test Module")
        self.geometry("800x600")
        self.resizable(True, True)

        self.searchbar = ModuleSearchBar(self)
        self.searchbar.pack(side="top", expand=False, fill="x")

        self.serverbar = ServerUrlBar(self)
        self.serverbar.pack(side="top", expand=False, fill="x")

        self.settingsbar = SettingsBar(self)
        self.settingsbar.pack(side="top", expand=False, fill="x")

        self.button_start = ttk.Button(
            self, text="Start", padding=0, command=self.start
        )
        self.button_start.pack(side="top", expand=False, fill="x")

        self.statusbar = StatusBar(self)
        self.statusbar.pack(side="bottom", expand=False, fill="x")

        self.module = None

    def append(self, text: str):
        super().append(text)
        self.statusbar.set_status(text)

    def connect(self, serial):
        self.module = XBee(serial)
        hardware, firmware = self.module.verify()
        if hardware is None or firmware is None:
            self.disconnect()

        self.settingsbar.textbox_src["text"] = str(self.module.get_64bit_addr())

    def disconnect(self):
        self.module.clean()
        self.module = None

    def start(self):
        pass

    def __on_show(self):
        self.background.start()
        self.searchbar.reload()

    def __on_close(self):
        self.background.stop()
        self.destroy()

    def show(self):
        self.__on_show()
        self.mainloop()
