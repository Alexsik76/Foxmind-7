import os


class Config(object):
    DATA_PATH = os.environ.get('DATA_PATH') or 'you-will-never-guess'