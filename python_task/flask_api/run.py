from api import factory

factory.environment = 'default'

# flask instance
app = factory.flask

# celery instance
celery = factory.celery

if __name__ == '__main__':
    app.run()