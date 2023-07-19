#!/usr/bin/env python3
"""Creates a Cache class that initializes an instance of
the Redis client as a private variable.
The class has a method store that generates a uuid as the key
and stores the input data it gets from the parameter as the value
"""
import redis
import uuid
from typing import Union


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
