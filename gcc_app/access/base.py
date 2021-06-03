import datetime
from dataclasses import dataclass
from typing import Optional, Union

from sqlalchemy.orm import DeclarativeMeta

from gcc_app.app import create_async_session
from gcc_app.models import UserModel, EventModel
from gcc_app.models.base import BaseModel


class BaseAccess:
    # id: Optional[int] = None
    # # todo type(timestamp) ?
    # timestamp: Optional[str] = None
    # active: Optional[bool] = None
    # archived: Optional[bool] = None
    # _obj: Union[UserModel, None] = None
    # __model: Optional[DeclarativeMeta] = BaseModel

    @staticmethod
    async def remove(_obj: Optional[DeclarativeMeta]) -> int:
        if _obj:
            _obj_id = _obj.id
            async with await create_async_session() as session:
                session.delete(_obj)
                session.commit()
            return _obj_id
        return None

    def query_by_id(self):
        obj = create_async_session().query(self.__model).get(self.id)
        return obj

    def activate(self):
        self._obj.active = True
        create_async_session().commit()

        return True

    def deactivate(self):
        self._obj.active = False
        create_async_session().commit()
        return False

    def archive(self):
        self._obj.archived = True
        create_async_session().commit()
        return True

    def unarchive(self):
        self._obj.archived = False
        create_async_session().commit()
        return False
