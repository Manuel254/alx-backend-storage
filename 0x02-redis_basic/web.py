#!/usr/bin/env python3
"""Implements an expiring web cache and tracker"""
import redis
import requests
from typing import Callable
from functools import wraps


def count_url_access(func: Callable) -> Callable:
    """Decorator function that counts the number
    of times a particular URL was accessed
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Function responsible for incrementing count"""
        r = redis.Redis()
        key = "count:{}".format(*args)
        text = func(*args, **kwargs)
        r.incr(key)
        r.expire(key, 300)
        return text
    return wrapper


@count_url_access
def get_page(url: str) -> str:
    """Obtains the HTML content of a particular
    URL.
    Returns:
        content (str): The HTML content of a url
    """
    results = requests.get(url)
    return results.text


print(get_page("http://slowwly.robertomurray.co.uk"))
