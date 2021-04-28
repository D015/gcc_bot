import pickle
from typing import Any

import redis

from gcc_app.app import redis_db


def redis_set(name: Any, value: Any,
              connector: redis.client.Redis = redis_db) -> bool:
    if not (type(value) in {str, int, float, bool}):
        value = pickle.dumps(value)
    result = connector.set(name, value)
    return result


def redis_get(name: Any, connector: redis.client.Redis = redis_db) -> Any:
    value = connector.get(name)
    if type(value) is bytes:
        value = pickle.loads(value)
    return value




