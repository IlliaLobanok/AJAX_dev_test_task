import logging


class TLogger(logging.Logger):
    def __init__(self, name, level=logging.NOTSET):
        super().__init__(name, level)
        handler = logging.FileHandler("tests/test_log.txt")
        handler.setLevel(logging.DEBUG)
        self.setLevel(logging.DEBUG)
        log_format = logging.Formatter("%(asctime)s ::: %(levelname)s ::: %(name)s ::: %(message)s")
        handler.setFormatter(log_format)
        self.addHandler(handler)
