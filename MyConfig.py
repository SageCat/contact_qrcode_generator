from configparser import ConfigParser


class MyConfig(ConfigParser):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename
        self.read(filename, encoding='utf-8')