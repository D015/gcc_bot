from dataclasses import dataclass
from typing import Optional, Union

from sqlalchemy.orm import DeclarativeMeta

from gcc_app.app import session
from gcc_app.models import User
from gcc_app.models.base import BaseModel


@dataclass
class BaseAccess:
    id: Optional[int] = None
    timestamp: Optional[str] = None
    active: Optional[bool] = None
    archived: Optional[bool] = None
    _obj: Union[User, None] = None
    __model: Optional[DeclarativeMeta] = BaseModel

    def remove_object(self):
        if self._obj:
            _obj_id = self._obj.id
            session.delete(self._obj)
            session.commit()
            return _obj_id
        return None

    def query_object_by_id(self):
        obj = session.query(self.__model).get(self.id)
        return obj

    def activate(self):
        self._obj.active = True
        return True

    def deactivate(self):
        self._obj.active = False
        return False

    def archive(self):
        self._obj.archived = True
        return True

    def unarchive(self):
        self._obj.archived = False
        return False
