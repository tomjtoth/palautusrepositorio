import re
from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository
)


rex = {
    # on oltava merkeistä a-z koostuva vähintään 3 merkin pituinen merkkijono
    'uname': re.compile(r"^[a-z]{3,}$"),

    # on oltava pituudeltaan vähintään 8 merkkiä ja se ei saa koostua pelkästään kirjaimista
    'passw': re.compile(r"^(?![a-zA-Z]{8,}$).{8,}$")
}


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password, password_confirmation):
        self.validate(username, password, password_confirmation)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password, password_confirmation):
        if not username or not password:
            raise UserInputError("Username and password are required")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
        if not rex['uname'].match(username):
            raise UserInputError(
                "Username complexity requirements unsatisfied")

        if not rex['passw'].match(password):
            raise UserInputError(
                "Password complexity requirements unsatisfied")

        if password != password_confirmation:
            raise UserInputError("Passwords don't match")


user_service = UserService()
