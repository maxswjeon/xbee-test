from random import choice
from string import printable

from utils.XBee import XBee


class RangeTest:
    def __init__(self, xbee: XBee, server, name, comment):
        self.xbee = xbee
        self.server = server
        self.name = name
        self.comment = comment

    def init(self, reset=False):
        self.xbee.assert_command_mode()

        if reset:
            # Restore Defaults
            self.xbee.AT("RE", self.name)

            # Apply Changes
            self.xbee.AT("AC", self.server)

        self.xbee.AT("MT", "0")

    def run(self, payload="", payload_length=0):
        if payload == "" and payload_length == 0:
            raise ValueError("Payload or payload_length must be set")

        if payload == "":
            payload = "".join(choice(printable) for _ in range(payload_length))

        self.xbee.assert_command_mode()

        self.xbee.AT("NI", self.name)

        # Last Packet RSSI
        self.xbee.AT("DB")

        # Recieved Error Count
        self.xbee.AT("ER")

        # Good Packets Recieved
        self.xbee.AT("GD")

        # MAC ACK Failure Count
        self.xbee.AT("EA")

        # Transmit Failure Count
        self.xbee.AT("TR")

        # MAC Unicast Transmissions
        self.xbee.AT("UA")

        # Serial Number High
        self.xbee.AT("SH")

        # Serial Number Low
        self.xbee.AT("SL")

        # Destination Address High
        self.xbee.AT("DH")

        # Destination Address Low
        self.xbee.AT("DL")

        # Transmit Options
        self.xbee.AT("TO", "C1")

        # API Mode (Esacpes: w/o 1 | w/ 2)
        self.xbee.AT("AP", "1")
