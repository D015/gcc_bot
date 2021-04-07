import datetime
from dataclasses import dataclass
from typing import Optional, Union

from sqlalchemy.orm import DeclarativeMeta

from gcc_app.app import session
from gcc_app.models import User
from gcc_app.models.base import BaseModel


@dataclass
class BaseAccess:
    id: Optional[int] = None
    # todo type(timestamp) ?
    timestamp: Optional[str] = None
    active: Optional[bool] = None
    archived: Optional[bool] = None
    _obj: Union[User, None] = None
    __model: Optional[DeclarativeMeta] = BaseModel

    def remove(self):
        if self._obj:
            _obj_id = self._obj.id
            session.delete(self._obj)
            session.commit()
            return _obj_id
        return None

    def query_by_id(self):
        obj = session.query(self.__model).get(self.id)
        return obj

    def activate(self):
        self._obj.active = True
        session.commit()

        return True

    def deactivate(self):
        self._obj.active = False
        session.commit()
        return False

    def archive(self):
        self._obj.archived = True
        session.commit()
        return True

    def unarchive(self):
        self._obj.archived = False
        session.commit()
        return False
