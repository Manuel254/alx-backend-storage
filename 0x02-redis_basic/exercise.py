#!/usr/bin/env python3
"""Creates a Cache class that initializes an instance of
the Redis client as a private variable.
The class has a method store that generates a uuid as the key
and stores the input data it gets from the parameter as the value
"""
import redis
import uuid
from typing import Union, Optional, Callable, Any


class Cache:
    """This class creates an instance of redis"""
    def __init__(self):
        """Instantiates an instance of redis client"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores key-value pair in db"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Union[Callable[..., Any], None]) -> Any:
        """Gets a value of a key and converts it
        to its desirable format
        """
        result = self._redis.get(key)

        if result is not None and fn is not None:
            return fn(result)
        return result

    def get_str(self, key: str) -> str:
        """Automatially parameterize Cache.get with
        string type
        """
        return self.get(key, fn=str).decode("utf-8")

    def get_int(self, key: int) -> int:
        """Automatially parameterize Cache.get with
        int type
        """
        return self.get(key, fn=int).decode("utf-8")
