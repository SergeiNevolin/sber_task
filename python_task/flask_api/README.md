# RESTful API Flask

## Установка

Для установки можно воспользоваться (для Windows):
```
make setup
```

или командой:
```
pip install .
```

## Запуск

```
make run
```
или
```
python run.py
```

Для Celery необходимо запустить Redis и выполнить команду:
```
celery -A run.celery worker --loglevel=info
```
