import tkinter.ttk as ttk

import serial.tools.list_ports

from utils.Background import background
from utils.XBee import XBee
from utils.Window import StatefulWindow


class ModuleSearchBar(ttk.Frame):
    def __init__(self, parent: StatefulWindow):
        super().__init__(parent, height="8m")
        self.pack_propagate(False)

        self.parent = parent
        self.background = parent.background
        self.ports = {}

        self.label_serial_ports = ttk.Label(self, text="Serial Ports", width=12)
        self.label_serial_ports.pack(side="left")

        self.combo_serial_ports = ttk.Combobox(self, state="disabled")
        self.combo_serial_ports.pack(side="left", expand=True, fill="both")

        frame = ttk.Frame(self, width="24m")
        frame.pack(side="left", fill="both")
        frame.pack_propagate(False)

        self.button_serial_reload = ttk.Button(
            frame,
            text="Reload",
            command=self.reload,
            state="disabled",
            padding=0,
        )
        self.button_serial_reload.pack(fill="both", expand=True)

        frame = ttk.Frame(self, width="24m")
        frame.pack(side="left", fill="both")
        frame.pack_propagate(False)

        self.button_serial_start = ttk.Button(
            frame, text="Connect", state="disabled", padding=0, command=self.connect
        )
        self.button_serial_start.pack(fill="both", expand=True)

    def set_status(self, text: str):
        self.parent.append(text)

    @background()
    def reload(self):
        self.set_status("Reloading serial ports")
        self.combo_serial_ports["state"] = "disabled"
        self.button_serial_start["state"] = "disabled"
        self.button_serial_reload["state"] = "disabled"

        self.parent.disconnect()

        print("Test")

        values = []
        ports = serial.tools.list_ports.comports()

        for port, desc, _ in sorted(ports):
            print(port, desc)
            try:
                self.set_status(f"Checking {desc} is an XBee module")

                module = serial.Serial(port)
                xbee = XBee(module)
                hardware, _ = xbee.verify()
                xbee.clean()

                if hardware is None:
                    self.set_status(f"{desc} is not an XBee module")
                    continue

                values.append(f"{hardware.name} ({port})")
                self.ports[f"{hardware.name} ({port})"] = port
            except serial.SerialException:
                self.set_status(f"Failed to open {port} ({desc})")
                continue

        self.combo_serial_ports["values"] = values
        if len(values) > 0:
            self.combo_serial_ports.set(values[0])

        self.combo_serial_ports["state"] = "readonly"
        self.button_serial_start["state"] = "normal"
        self.button_serial_reload["state"] = "normal"
        self.set_status(f"Found {len(values)} XBee modules")

    def connect(self):
        if self.parent.module is not None:
            self.parent.disconnect()
            self.combo_serial_ports["state"] = "readonly"
            self.button_serial_reload["state"] = "normal"
            self.button_serial_start["text"] = "Connect"
            return

        self.combo_serial_ports["state"] = "disabled"
        self.button_serial_reload["state"] = "disabled"
        self.button_serial_start["text"] = "Disconnect"

        module = serial.Serial(self.ports[self.combo_serial_ports.get()])
        self.parent.connect(module)
