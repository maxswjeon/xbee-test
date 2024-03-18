import wx

import ctypes
from threading import Thread, Lock, Condition, Event

import serial.tools.list_ports
from digi.xbee.devices import XBeeDevice

from windows.BaseMainWindow import BaseMainWindow


class MainWindow(BaseMainWindow):
    def __init__(self):
        super().__init__(None)

        self.thread = Thread(target=self.__thread)
        self.thread_lock = Lock()
        self.thread_wait = Condition(self.thread_lock)
        self.thread_kill = Event()
        self.thread_queue = []

        self.device = None

        self.button_metadata_save.Disable()
        self.button_metadata_reset.Disable()
        self.button_clear.Disable()
        self.button_start.Disable()

        self.Bind(wx.EVT_SHOW, self._on_show)
        self.Bind(wx.EVT_CLOSE, self._on_close)
        self.Bind(wx.EVT_BUTTON, self._on_button_refresh, self.button_refresh)
        self.Bind(wx.EVT_BUTTON, self._on_button_serial, self.button_serial)
        self.Bind(wx.EVT_BUTTON, self._on_button_server, self.button_server)
        self.Bind(
            wx.EVT_BUTTON, self._on_button_metadata_save, self.button_metadata_save
        )
        self.Bind(
            wx.EVT_BUTTON, self._on_button_metadata_reset, self.button_metadata_reset
        )
        self.Bind(wx.EVT_BUTTON, self._on_clear, self.button_clear)
        self.Bind(wx.EVT_BUTTON, self._on_button_start, self.button_start)
        self.Bind(wx.EVT_TEXT, self._on_metadata_change, self.textbox_module_id)
        self.Bind(wx.EVT_TEXT, self._on_metadata_change, self.textbox_distance)
        self.Bind(wx.EVT_TEXT, self._on_metadata_change, self.textbox_notes)

        self._on_button_refresh(None)

    def __thread(self):
        while not self.thread_kill.is_set():
            if len(self.thread_queue) == 0:
                with self.thread_wait:
                    self.thread_wait.wait()

            if self.thread_kill.is_set():
                break

            task = self.thread_queue.pop(0)
            task()

    def background(self, task):
        self.thread_queue.append(task)

        with self.thread_wait:
            self.thread_wait.notify()

    def _on_show(self, evt):
        self.thread.start()

    def _on_close(self, evt):
        self.thread_kill.set()
        with self.thread_wait:
            self.thread_wait.notify()
        self.thread.join()
        self.Destroy()

    def _on_button_refresh(self, evt):
        self.button_refresh.Disable()
        self.combobox_serial.Clear()
        self.ports = serial.tools.list_ports.comports()
        for port in self.ports:
            self.combobox_serial.Append(port.description)
        self.combobox_serial.SetSelection(0)
        self.button_refresh.Enable()

    def _on_button_serial(self, evt):
        if self.device:
            self.device.close()
            self.device = None
            self.button_refresh.Enable()
            self.combobox_serial.Enable()
            self.button_serial.SetLabelText("Connect")
            return
        self.button_refresh.Disable()
        self.combobox_serial.Disable()
        self.button_serial.SetLabelText("Connecting")

        port = self.ports[self.combobox_serial.GetSelection()].device
        self.background(lambda: self.serial_connect(port))

    def _on_button_server(self, evt):
        print("Connecting to server")
        self.background(self.__on_button_server)

    def _on_button_metadata_save(self, evt):
        print("Saving metadata")
        self.background(self.__on_button_metadata_save)

    def _on_button_metadata_reset(self, evt):
        print("Resetting metadata")
        self.background(self.__on_button_metadata_reset)

    def _on_clear(self, evt):
        print("Clearing data")
        self.background(self.__on_clear)

    def _on_button_start(self, evt):
        print("Starting experiment")
        self.background(self.__on_button_start)

    def _on_metadata_change(self, evt):
        self.button_metadata_save.Enable()
        self.button_metadata_reset.Enable()

    def serial_connect(self, port):
        try:
            self.device = XBeeDevice()
            self.device.open(port, 9600)
        except:
            wx.MessageDialog(
                self,
                "Failed to connect to serial port",
                "Error",
                wx.OK | wx.CENTER | wx.ICON_ERROR,
            ).ShowModal()

            self.button_refresh.Enable()
            self.combobox_serial.Enable()
            self.button_serial.SetLabelText("Connect")

            self.device = None
            return
