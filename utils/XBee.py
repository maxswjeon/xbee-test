import serial
import time

from digi.xbee.models.hw import HardwareVersion
from digi.xbee.devices import XBeeDevice


class XBee(XBeeDevice):
    def __init__(self, port: serial.Serial):
        super().__init__(port.name, 9600)

        self.port = port
        self.last_command_time = None
        self.command_mode = False
        self.__state = "serial"

        self.port.timeout = 1
        self.port.set_buffer_size(rx_size=64 * 1024, tx_size=64 * 1024)
        self.port.reset_input_buffer()
        self.port.reset_output_buffer()

    def AT(self, command: str | bytes | None = None, *args):
        if command is None:
            self.port.write(b"AT\r")
            self.last_command_time = time.time_ns()
            time.sleep(0.1)
            return

        if isinstance(command, str):
            command = command.encode()

        params = b""
        for arg in args:
            if isinstance(arg, str):
                arg = arg.encode()
            params += b" " + arg

        payload = b"AT " + command + params + b"\r"
        self.port.write(payload)
        self.port.flush()
        self.last_command_time = time.time_ns()
        time.sleep(0.1)

    def assert_command_mode(self):
        try:
            self.AT()
        except serial.SerialException:
            self.port.write(b"+++")
            time.sleep(1.5)

        response = self.port.read(3)
        if response != b"OK\r":
            time.sleep(1.5)
            self.port.write(b"+++")
            time.sleep(1.5)
        else:
            return False

        self.port.read(3)

        self.command_mode = True
        self.last_command_time = time.time_ns()

        return True

    def verify(self):
        if self.__state == "module":
            return self.get_hardware_version(), self.get_firmware_version()

        if not self.assert_command_mode():
            print("Failed to enter command mode")
            return (None, None)

        self.AT("HV")
        time.sleep(1)
        hardware = self.port.read_all()
        if len(hardware) != 5:
            return (None, None)

        self.hardware = HardwareVersion.get(int(hardware[:2].decode(), 16))

        self.AT("VL")
        time.sleep(1)
        self.firmware = self.port.read_all()

        self.port.close()
        self.open()

        return self.hardware, self.firmware

    def clean(self):
        if self.__state == "module":
            self.close()
        else:
            self.port.close()
