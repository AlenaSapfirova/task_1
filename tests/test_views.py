import pytest
from http import HTTPStatus


def test_register(user_client):
    data = {
        'username': 'test',
        'password': '12365Test_!'
    }
    response = user_client.post('/api/users/register/', data)
    print(response)
    assert response.status_code == HTTPStatus.CREATED, (
        'Валидные данные при авторизации не сохраняются в базе'
    )


def test_unauthorized_post(user_client):
    data = {
        'header': 'test',
        'text': 'text'
    }
    response = user_client.post('/api/posts/', data)
    assert response.status_code == HTTPStatus.UNAUTHORIZED, (
        'Неавторизованный пользователь смог создать пост'
    )


def test_authenticated_post(user_authenticated):
    data = {
        'header': 'test',
        'text': 'text'
    }
    response = user_authenticated.post('/api/posts/', data)
    assert response.status_code == HTTPStatus.CREATED, (
        'Авторизованный пользователь не смог создать пост'
    )


def test_unauthorized_post_get(user_client):
    response = user_client.get('/api/posts/')
    assert response.status_code == HTTPStatus.OK, (
        'Неавторизованный пользователь не может просматривать посты'
    )


def test_authenticated_get(user_authenticated):
    response = user_authenticated.get('/api/posts/')
    assert response.status_code == HTTPStatus.OK, (
        'Авторизованный пользователь не может просматривать посты'
    )


def test_autenticated_patch_post(user_authenticated, post):
    data = {
        'header': 'goodbay'
    }
    response = user_authenticated.patch('/api/posts/1/', data)
    assert response.status_code == HTTPStatus.OK, (
        'Авторизованный пользователь не может редактировать свои посты'
    )


def test_authenticated_patch_post_invalid(another_client, post):
    data = {
        'header': 'goodbay'
    }
    response = another_client.patch('/api/posts/1/', data)
    assert response.status_code == HTTPStatus.NOT_FOUND, (
        'Пользователь имеет возможность редактировать не свой код'
    )


def test_unauthorized_patch_post(user_client, post):
    data = {
        'header': 'goodbay'
    }
    response = user_client.patch('/api/posts/1/', data)
    assert response.status_code == HTTPStatus.UNAUTHORIZED, (
        'Неавторизованный пользователь может редактировать посты'
    )


def test_authenticated_delete_post_valid(user_authenticated, post):
    response = user_authenticated.delete('/api/posts/1/')
    assert response.status_code == HTTPStatus.NO_CONTENT, (
        'Пользователь не имеет возможность удалять свой пост'
    )


def test_authenticated_delete_post_invalid(another_client, post):
    response = another_client.delete('/api/posts/1/')
    assert response.status_code == HTTPStatus.NOT_FOUND, (
        'Пользователь имеет возможность удалять не свой пост'
    )


