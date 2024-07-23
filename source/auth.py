class AuthService:
    def __init__(self, user_repository):
        self.user_repository = user_repository
        self.logged_in_user = None

    def login(self, username, password):
        user = self.user_repository.find_user_by_username(username)
        if user and user.check_password(password):
            self.logged_in_user = user
            return True
        return False

    def logout(self):
        self.logged_in_user = None

    def is_authenticated(self):
        return self.logged_in_user is not None

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_password(self, password):
        return self.password == password