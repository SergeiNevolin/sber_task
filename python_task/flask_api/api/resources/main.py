from flask_restful import Resource
from flask import request
from api import factory

from bs4 import BeautifulSoup
import requests
from collections import Counter
import json

# celery instance
celery = factory.celery


class Tags(Resource):
    """Создание задачи по подсчету тегов"""

    def post(self):
        content = request.json
        task = count_tags.apply_async((content['url'],))
        return {'task_id': task.id}, 201


class TagsStatus(Resource):
    """Получение тегов для задачи по ее id"""

    def get(self, id):
        task = count_tags.AsyncResult(id)
        if task.state == 'PENDING':
            # состояние неизвестно
            response = {
                'state': task.state,
                'status': 'state is unknown'
            }
        elif task.state == 'STARTED':
            # задача запущена
            response = {
                'state': task.state,
                'status': 'started by a worker'
            }
        elif task.state == 'SUCCESS':
            # задача выполенена
            response = {
                'state': task.state,
                'tags': json.loads(task.info['tags'])
            }
        else:
            # произошла ошибка при выполнении
            response = {
                'state': task.state,
                'status': str(task.info)
            }
        return response


@celery.task(bind=True)
def count_tags(self, url):
    """Функция подсчета количества тегов каждого вида"""

    html_content = requests.get(url).text

    soup = BeautifulSoup(html_content, "html.parser")
    all_tags = [tag.name for tag in soup.find_all()]

    tags_counter = Counter(all_tags)
    tags = json.dumps(tags_counter)

    return {'tags': tags}
