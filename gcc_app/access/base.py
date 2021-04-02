from dataclasses import dataclass
from typing import Optional, Union

from sqlalchemy.orm import DeclarativeMeta

from gcc_app.app import session
from gcc_app.models import User
from gcc_app.models.base import BaseModel


@dataclass
class BaseAccess:

    # def __init__(self, id=None, timestamp=None, active=None, archived=None,
    #              _obj=None, model=None):
    #     self.id = id
    #     self.timestamp = timestamp
    #     self.active = active
    #     self.archived = archived
    #     self._obj = _obj
    #     self.model = model
    id: Optional[int]
    timestamp: Optional[str]
    active: Optional[bool]
    archived: Optional[bool]
    _obj: Union[User, None]
    # todo check the use of the attribute model
    # model: Optional[User]

    def remove_object(self):
        if self._obj:
            _obj_id = self._obj.id
            session.delete(self._obj)
            session.commit()
            return _obj_id
        return None

    def query_object_by_id(self):
        obj = self.model.query.get(self.id)
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
