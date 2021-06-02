from sqlalchemy import Column, Boolean, String, Integer, ForeignKey

from gcc_app.app import DB
from gcc_app.models.base import BaseModel


class UserModel(DB, BaseModel):
    __tablename__ = "user"

    telegram_user_id = Column(Integer, index=True, unique=True)
    is_bot = Column(Boolean)
    first_name = Column(String(50))
    last_name = Column(String(50))
    username = Column(String(50))
    language_code = Column(String(6))

    # __mapper_args__ = {'eager_defaults': True}

    def __init__(self, *args, **kwargs):
        super(UserModel, self).__init__(*args, **kwargs)

    __mapper_args__ = {"eager_defaults": True}

    def __repr__(self):
        return (
            f"User id {self.id} {self.username} "
            f"telegram_user_id {self.telegram_user_id}"
        )
