import pytest
from mixer.backend.django import mixer
from api.models import Post


@pytest.fixture
def post(user):
    post = mixer.blend('api.post', author=user,
                       header='Hello', text='text', id=1)
    return post
