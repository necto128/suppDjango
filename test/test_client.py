import pytest
from django.urls import reverse
import uuid
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


@pytest.fixture
def test_password():
    return 'strong-test-pass'


@pytest.fixture
def create_user(db, django_user_model, test_password):
    def make_user(**kwargs):
        kwargs['password'] = 'strong-test-pass'
        if 'username' not in kwargs:
            kwargs['username'] = str(uuid.uuid4())
        return django_user_model.objects.create_user(**kwargs)

    return make_user


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()


@pytest.fixture
def get_or_create_token(db, create_user):
    user1 = create_user()
    token, _ = Token.objects.get_or_create(user=user1)
    return token


@pytest.mark.django_db
def test_auth_request(api_client, get_or_create_token):
    url = reverse('token_obtain_pair')
    api_client.credentials(HTTP_AUTHORIZATION='Token ' + get_or_create_token.key)
    response = api_client.get(url)
    assert response.status_code == 200
