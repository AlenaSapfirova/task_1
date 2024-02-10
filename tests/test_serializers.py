import pytest

from api.serializers import UserSerializer
from api.models import User

@pytest.mark.django_db
def test_serializer_user():
    data = {
        'username': 'test',
        'password': '1234Test!'
    }

    serializer = UserSerializer(data=data)
    assert serializer.is_valid(), (
        'Валидные данные не проходят проверку'
    )
    serializer.save()
    assert User.objects.filter(username='test').exists(), (
        'Пользователь не создался при сохранении экземпляра'
    )
    user = User.objects.get(username='test')
    assert user.check_password('1234Test!'), (
        'Пароль пользователя после дешифровки не соответствует'
        'начальным данным'
    )
