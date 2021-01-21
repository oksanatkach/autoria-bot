import os


class Config:
    def __init__(self):
        self.autoriaKey = os.environ['autoriaKey'] if 'autoriaKey' in os.environ else ''
        self.telebotToken = os.environ['telebotToken'] if 'telebotToken' in os.environ else ''


config = Config()
