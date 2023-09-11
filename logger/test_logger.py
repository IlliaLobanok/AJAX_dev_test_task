import logging


class TLogger(logging.Logger):
    def __init__(self, name, level=logging.NOTSET):
        super().__init__(name, level)

    def t_start(self, test):
        self.info(f"Test {test.__qualname__} started.")

    def t_finish(self, test):
        self.info(f"Test {test.__qualname__} finished.")
