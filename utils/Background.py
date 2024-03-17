from functools import wraps
from threading import Thread, Lock, Condition


class Background:
    def __init__(self):
        self.thread = Thread(target=self.__thread)
        self.backlog = []
        self.lock = Lock()
        self.condition = Condition(self.lock)
        self.kill = False

    def __thread(self):
        while not self.kill:
            try:
                if len(self.backlog) == 0:
                    with self.condition:
                        self.condition.wait()

                if len(self.backlog) == 0:
                    # might have been woken up to die
                    continue

                task = self.backlog.pop(0)
                task()
            except:
                pass

    def start(self):
        self.thread.start()

    def stop(self):
        self.kill = True
        with self.condition:
            self.condition.notify()
        self.thread.join()

    def run(self, method):
        with self.lock:
            self.backlog.append(method)
            self.condition.notify()


def background(variable: str = "background"):
    def wrap(method):
        @wraps(method)
        def decorator(self, *args, **kwargs):
            def task():
                method(self, *args, **kwargs)

            getattr(self, variable).run(task)

        return decorator

    return wrap
