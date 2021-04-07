from dataclasses import dataclass
from typing import Optional

from sqlalchemy.orm import DeclarativeMeta

from gcc_app.access.base import BaseAccess
from gcc_app.app import session
from gcc_app.models import UserModel


@dataclass
class UserAccess(BaseAccess):
    telegram_user_id: Optional[int] = None
    is_bot: Optional[bool] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    username: Optional[str] = None
    language_code: Optional[str] = None
    __model: Optional[DeclarativeMeta] = UserModel

    def create(self) -> int:
        new_user = UserModel(telegram_user_id=self.telegram_user_id,
                             is_bot=self.is_bot,
                             first_name=self.first_name,
                             last_name=self.last_name,
                             username=self.username,
                             language_code=self.language_code)
        session.add(new_user)
        session.commit()
        return new_user.id

    def create_for_start(self) -> int:
        user = self.query_by_telegram_user_id()
        if user:
            user_id = user.id
            if not user.active:
                user.active = True
                session.commit()
        else:
            user_id = self.create()
        return user_id

    def query_by_telegram_user_id(self) -> UserModel:
        user = session.query(UserModel).filter_by(
            telegram_user_id=self.telegram_user_id).first()
        return user
