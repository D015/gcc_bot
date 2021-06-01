from dataclasses import dataclass
from typing import Optional

from sqlalchemy.orm import DeclarativeMeta

from gcc_app.access.base import BaseAccess
from gcc_app.app import created_async_session
from gcc_app.models import UserModel


class UserAccess(BaseAccess):
    # telegram_user_id: Optional[int] = None
    # is_bot: Optional[bool] = None
    # first_name: Optional[str] = None
    # last_name: Optional[str] = None
    # username: Optional[str] = None
    # language_code: Optional[str] = None
    # __model: Optional[DeclarativeMeta] = UserModel

    @staticmethod
    async def create(
        telegram_user_id: Optional[int] = None,
        is_bot: Optional[bool] = None,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        username: Optional[str] = None,
        language_code: Optional[str] = None,
    ) -> int:

        async with await created_async_session() as session:
            async with session.begin():
                new_user = UserModel(
                    telegram_user_id=telegram_user_id,
                    is_bot=is_bot,
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    language_code=language_code,
                )
                session.add(new_user)
            await session.commit()

        return new_user.id

    @classmethod
    async def create_for_start(cls) -> int:
        user = await cls.query_by_telegram_user_id()
        if user:
            async with await created_async_session() as session:
                user_id = user.id
                if not user.active:
                    user.active = True
                    session.commit()
        else:
            user_id = await cls.create()
        return user_id

    @staticmethod
    async def query_by_telegram_user_id(
        telegram_user_id: Optional[int] = None,
    ) -> UserModel:
        async with await created_async_session() as session:
            user = (
                session.query(UserModel)
                .filter_by(telegram_user_id=telegram_user_id)
                .first()
            )
        return user
