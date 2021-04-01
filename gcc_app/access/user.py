from gcc_app.app import session
from gcc_app.models import UserModel


class UserAccess:
    def __init__(self, id=None,chat_id=None, is_bot=None,
                 first_name=None, last_name=None, username=None,
                 language_code=None):
        self.id = id
        self.chat_id = chat_id
        self.is_bot = is_bot
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.language_code = language_code

    def create_user(self):
        new_user = UserModel(chat_id=self.chat_id,
                             is_bot=self.is_bot,
                             first_name=self.first_name,
                             last_name=self.last_name,
                             username=self.username,
                             language_code=self.language_code)
        session.add(new_user)
        session.commit()
        return new_user


