from gcc_app.access.base import BaseAccess
from gcc_app.app import session
from gcc_app.models import User


class UserAccess(BaseAccess):
    def __init__(self, id=None, timestamp=None, active=None, archived=None,
                 _obj=None, chat_id=None, is_bot=None,
                 first_name=None, last_name=None, username=None,
                 language_code=None):
        super().__init__(id, timestamp, active, archived, _obj)
        # todo check the use of the attribute model
        # todo add check is_bot for boolean type
        self.chat_id = int(chat_id)
        self.is_bot = False if is_bot == 'false' else True
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.language_code = language_code

    def create_user(self):
        new_user = User(chat_id=self.chat_id,
                        is_bot=self.is_bot,
                        first_name=self.first_name,
                        last_name=self.last_name,
                        username=self.username,
                        language_code=self.language_code)
        session.add(new_user)
        session.commit()
        return new_user.id

    def create_user_for_start(self):
        user = self.query_by_chat_id()
        if user:
            user_id = user.id
            if user.archived:
                user.archived = False
        else:
            user_id = self.create_user()
        return user_id

    def query_by_chat_id(self):
        user = session.query(User).filter_by(chat_id=self.chat_id).first()
        return user
