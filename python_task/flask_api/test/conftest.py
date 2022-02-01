import pytest
from flask.testing import FlaskClient
from api import Factory
from api.resources import blueprint
from api import factory

factory.environment = 'testing'


@pytest.yield_fixture(scope='session')
def factory_app():
    yield Factory(environment='testing')


@pytest.yield_fixture(scope='session')
def flask_app(factory_app):
    factory_app.set_flask()
    factory_app.set_celery()
    factory_app.register(blueprint)
    yield factory_app


@pytest.fixture(scope='session')
def flask_app_client(flask_app):
    app = flask_app.flask
    app.test_client_class = FlaskClient
    return app.test_client()