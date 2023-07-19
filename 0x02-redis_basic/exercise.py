#!/usr/bin/env python3
"""Creates a Cache class that initializes an instance of
the Redis client as a private variable.
The class has a method store that generates a uuid as the key
and stores the input data it gets from the parameter as the value
"""
import redis
import uuid
from typing import Union, Optional, Callable, Any
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Decorator function that counts how many times
    methods of the Cache class are called
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function that performs the increment
        functionality
        """
        val = method(self, *args, **kwargs)
        self._redis.incr(key)
        return val
    return wrapper


class Cache:
    """This class creates an instance of redis"""
    def __init__(self):
        """Instantiates an instance of redis client"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores key-value pair in db"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """Gets a value of a key and converts it
        to its desirable format
        """
        result = self._redis.get(key)

        if fn:
            result = fn(result)
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
