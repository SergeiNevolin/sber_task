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

Для запуска Celery необходимо запустить Redis и выполнить команду:
```
celery -A run.celery worker --loglevel=info
```

## Использование
Создание задачи:
```
curl -i -X POST -H "Content-Type: application/json" -d '{"url":"https://www.google.com/"}' localhost:5000/api/tags
```
Ответ приходит в виде: {'task_id': '<task_id>'}

Получение состояния задачи:
```
curl -X GET -H "Content-Type: application/json" localhost:5000/api/tags/<task_id>
```
