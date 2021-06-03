from datetime import datetime

from sqlalchemy import Column, Boolean, DateTime, Integer


class BaseModel:

    id = Column(Integer, primary_key=True, autoincrement=True)

    timestamp = Column(DateTime, default=datetime.utcnow)
    active = Column(Boolean, default=True)
    archived = Column(Boolean, default=False)
