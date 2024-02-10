import pytest
from mixer.backend.django import mixer
from rest_framework.test import APIClient

@pytest.fixture
def user(django_user_model):
    return mixer.blend('auth.user')

@pytest.fixture
def user_client(user):
    client = APIClient(user)
    return client

@pytest.fixture
def user_authenticated(user):
    client = APIClient()
    client.force_authenticate(user=user)
    return client

@pytest.fixture
def another_user(django_user_model):
    user = django_user_model.objects.create_user(username='TestUser',
                                                 password='1234567')
    return user

@pytest.fixture
def another_client(another_user):
    client = APIClient()
    client.force_authenticate(another_user)
    return client
