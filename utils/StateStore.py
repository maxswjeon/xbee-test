from datetime import datetime


class StateStore:
    def __init__(self):
        super().__init__()
        self.log = []

    def append(self, text: str):
        self.log.append((datetime.now(), text))

    def get(self):
        return self.log[-1]

    def get_all(self):
        return self.log
