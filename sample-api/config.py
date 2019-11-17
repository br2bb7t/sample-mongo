import os


class Config(object):
    DEBUG = True
    SECRET_KEY = 'dev'
    SAMPLE_DB_URI = os.environ['SAMPLE_DB_URI']


class DevelopmentConfig(Config):
    DEBUG = False
