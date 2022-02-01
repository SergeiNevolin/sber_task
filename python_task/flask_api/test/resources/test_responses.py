import pytest
import time

def test_environment(factory_app):
    assert factory_app.environment == 'testing'


@pytest.mark.parametrize('http_method,http_path,data', (
    ('POST', '/api/tags', {'url': 'https://www.google.com/'}),
))
def test_post_tags(http_method, http_path, data, flask_app_client):
    response = flask_app_client.open(method=http_method, path=http_path, json=data)
    assert response.status_code == 201
    assert response.content_type == 'application/json'
    assert 'task_id' in response.json.keys()


@pytest.mark.parametrize('http_path,data', (
    ('/api/tags', {'url': 'https://www.google.com/'}),
))
def test_get_tags(http_path, data, flask_app_client):
    post_response = flask_app_client.post(path=http_path, json=data)
    time.sleep(1)
    get_response = flask_app_client.open(method='GET', path=str('/api/tags/' + post_response.json['task_id']))
    assert get_response.status_code == 200
    assert get_response.content_type == 'application/json'
    assert get_response.json['state'] == 'SUCCESS'
    tags = get_response.json['tags']
    assert tags['html'] == 1
    assert tags['title'] == 1
    assert tags['a'] == 18


@pytest.mark.parametrize('http_path,data', (
    ('/api/tags', {'url': 'https://www.google/'}),
))
def test_get_tags_invalid_url(http_path, data, flask_app_client):
    post_response = flask_app_client.post(path=http_path, json=data)
    time.sleep(1)
    get_response = flask_app_client.open(method='GET', path=str('/api/tags/' + post_response.json['task_id']))
    assert get_response.status_code == 200
    assert get_response.content_type == 'application/json'
    assert get_response.json['state'] == 'FAILURE'


@pytest.mark.parametrize('http_path,data', (
    ('/api/tags', {'url': 'https://www.google/'}),
))
def test_get_tags_task_performed(http_path, data, flask_app_client):
    post_response = flask_app_client.post(path=http_path, json=data)
    get_response = flask_app_client.open(method='GET', path=str('/api/tags/' + post_response.json['task_id']))
    assert get_response.status_code == 200
    assert get_response.content_type == 'application/json'
    assert get_response.json['state'] == 'STARTED'