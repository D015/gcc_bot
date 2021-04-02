from datetime import datetime

from sqlalchemy import (Column,
                        Boolean,
                        DateTime,
                        Integer,
                        String)

from gcc_app.app import DB


class BaseModel(DB):
    __tablename__ = 'base'

    id = Column(Integer, primary_key=True)

    timestamp = Column(DateTime, default=datetime.utcnow)
    active = Column(Boolean, default=True)
    archived = Column(Boolean, default=False)

    type = Column(String(50))

    __mapper_args__ = {
        'polymorphic_identity': 'base',
        'polymorphic_on': type
    }