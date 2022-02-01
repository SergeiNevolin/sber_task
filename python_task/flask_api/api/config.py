import os


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')
    
    TITLE = "Flask RESTful API"
    VERSION = "0.1.0"

    CELERY_TRACK_STARTED = True
    CELERY_BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
    BROKER_URL = CELERY_BROKER_URL

class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    

class StagingConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False

    CELERY_BROKER_URL = 'redis://redis:6379/0'
    CELERY_RESULT_BACKEND = 'redis://redis:6379/0'
    BROKER_URL = CELERY_BROKER_URL


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}