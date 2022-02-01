from flask import Flask
from celery import Celery
from api.config import config
import os


class Factory(object):
    def __init__(self, environment='default'):
        self._environment = os.getenv("APP_ENVIRONMENT")
        if not self._environment:
            self._environment = environment

    @property
    def environment(self):
        return self._environment

    @environment.setter
    def environment(self, environment):
        self._environment = environment

        self.flask.config.from_object(config[self._environment])

        self.celery.conf.update(self.flask.config)

    def set_flask(self, **kwargs):
        self.flask = Flask(__name__, **kwargs)

        self.flask.config.from_object(config[self._environment])

        return self.flask

    def set_celery(self, **kwargs):
        self.celery = Celery(__name__, **kwargs)

        self.celery.conf.update(self.flask.config)

        return self.celery

    def register(self, blueprint):
        self.flask.register_blueprint(blueprint)