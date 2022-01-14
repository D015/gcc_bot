from typing import Optional

from sqlalchemy.future import select

from .base import BaseAccess
from app import create_async_session
from models import UserModel


class UserAccess(BaseAccess):
    @staticmethod
    async def create(
        telegram_user_id: Optional[int] = None,
        is_bot: Optional[bool] = None,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        username: Optional[str] = None,
        language_code: Optional[str] = None,
    ) -> int:

        async with await create_async_session() as session:
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
            # await session.commit()
        return new_user.id

    @classmethod
    async def create_for_start(
        cls,
        telegram_user_id: Optional[int] = None,
        is_bot: Optional[bool] = None,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        username: Optional[str] = None,
        language_code: Optional[str] = None,
    ) -> int:
        user = await cls.query_by_telegram_user_id(
            telegram_user_id=telegram_user_id
        )
        if not user:
            user_id = await cls.create(
                telegram_user_id=telegram_user_id,
                is_bot=is_bot,
                first_name=first_name,
                last_name=last_name,
                username=username,
                language_code=language_code,
            )
        else:
            user_id = user.id
            if not user.active:
                async with await create_async_session() as session:
                    async with session.begin():
                        user.active = True
                        session.add(user)

        return user_id

    @staticmethod
    async def query_by_telegram_user_id(
        telegram_user_id: Optional[int] = None,
    ) -> UserModel:
        async with await create_async_session() as session:
            users = await session.execute(
                select(UserModel).filter_by(telegram_user_id=telegram_user_id)
            )
            user = users.scalars().first()
        return user
