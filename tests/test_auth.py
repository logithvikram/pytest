
import pytest
from unittest.mock import Mock
from source.auth import AuthService
from source.auth import User

@pytest.fixture
def user_repository():
    return Mock()

@pytest.fixture
def auth_service(user_repository):
    return AuthService(user_repository)

def test_login_success(auth_service, user_repository):
    user = User(username="testuser", password="testpass")
    user_repository.find_user_by_username.return_value = user

    result = auth_service.login("testuser", "testpass")

    assert result is True
    assert auth_service.is_authenticated() is True

def test_login_failure(auth_service, user_repository):
    user_repository.find_user_by_username.return_value = None

    result = auth_service.login("testuser", "wrongpass")

    assert result is False
    assert auth_service.is_authenticated() is False

def test_logout(auth_service, user_repository):
    user = User(username="testuser", password="testpass")
    user_repository.find_user_by_username.return_value = user
    auth_service.login("testuser", "testpass")

    auth_service.logout()

    assert auth_service.is_authenticated() is False
