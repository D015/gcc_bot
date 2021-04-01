from gcc_app.app import session


class BaseAccess:

    def __init__(self, id=None, _obj=None, model=None):
        self.id = id
        self._obj = _obj
        self.model = model

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
