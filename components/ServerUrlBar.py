import tkinter as tk
import tkinter.ttk as ttk

import requests
from urllib.parse import urlparse, urlunparse

from utils.Background import background
from utils.Window import StatefulWindow


class ServerUrlBar(ttk.Frame):
    def __init__(self, parent: StatefulWindow):
        super().__init__(parent, height="8m")
        self.pack_propagate(False)

        self.parent = parent
        self.background = parent.background

        self.label = ttk.Label(self, text="Server URL", width=12)
        self.label.pack(side="left")

        self.textbox = ttk.Entry(self)
        self.textbox.pack(side="left", expand=True, fill="both")

        frame = ttk.Frame(self, width="48m")
        frame.pack(side="left", fill="y")
        frame.pack_propagate(False)

        self.button = ttk.Button(frame, text="Connect", padding=0, command=self.connect)
        self.button.pack(fill="both", expand=True)

        self.connected = False

    def set_status(self, text: str):
        self.parent.append(text)

    @background()
    def check_server(self):
        try:
            url = urlparse(self.textbox.get())
        except:
            self.set_status("Invalid URL")

            self.textbox["state"] = "normal"
            self.button["state"] = "normal"
            return

        if url.scheme not in ["http", "https"]:
            self.set_status("Invalid URL")

            self.textbox["state"] = "normal"
            self.button["state"] = "normal"
            return

        url._replace(path="/-/healthy")
        try:
            request = requests.get(f"{urlunparse(url)}", timeout=5)
            request.raise_for_status()
        except:
            self.set_status("Server not healthy")

            self.textbox["state"] = "normal"
            self.button["state"] = "normal"
            return

        self.textbox["state"] = "readonly"
        self.button["state"] = "normal"
        self.button["text"] = "Disconnect"
        self.set_status = "Connected to server"

    def connect(self):
        if self.connected:
            self.textbox["state"] = "normal"
            self.button["state"] = "normal"
            self.button["text"] = "Connect"
            return

        self.textbox["state"] = "readonly"
        self.button["state"] = "disabled"

        self.set_status("Checking server state")
        self.check_server()

    def get_server_url(self):
        return self.textbox.get()
