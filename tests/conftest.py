from django.contrib.auth import get_user_model

import pytest
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken


@pytest.fixture
def user():
    User = get_user_model()
    return User.objects.create_user(
        username="asilbek",
        email="asilbekaliev@mail.ru",
        password="12345",
        is_staff=True,
    )


@pytest.fixture
def authenticated_api_client(user):
    client = APIClient()
    refresh = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")

    return client
