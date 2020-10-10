import os


class Config(object):
    DATA_PATH = os.environ.get('DATA_PATH') or 'path_is_not_set'
