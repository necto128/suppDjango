import pytest
from django.contrib.auth.models import User
from django.urls import reverse
import uuid

"""+@pytest.mark.django_db
def test_view_unauthorized(client):
   url = reverse('requests')
   response = client.get(url)
   assert response.status_code == 401"""


@pytest.fixture
def test_password():
    return 'strong-test-pass'


@pytest.fixture
def create_user(db, django_user_model, test_password):
    def make_user(**kwargs):
        kwargs['password'] = test_password
        if 'username' not in kwargs:
            kwargs['username'] = str(uuid.uuid4())
        return django_user_model.objects.create_user(**kwargs)

    return make_user


@pytest.fixture
def auto_login_user(db, client, create_user, test_password):
    def make_auto_login(user=None):
        if user is None:
            user = create_user()
        client.login(username=user.username, password=test_password)
        return client, user

    return make_auto_login


"""@pytest.fixture
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

@pytest.mark.django_db
def test_auth_view(client, create_user, test_password):
   user = create_user()
   url = reverse('token_obtain_pair')
   client.login(
       username=user.username, password=test_password
   )
   response = client.get(url)
   assert response.status_code == 200"""
