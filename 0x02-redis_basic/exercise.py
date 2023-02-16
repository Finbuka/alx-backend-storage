#!/usr/bin/env python3
"""
Exercise file
"""
import redis
from typing import Union, Optional, Callable
import uuid


class Cache:
    """
    cache class
    """

    def __init__(self) -> None:
        """
        constructor function
        """
        self._redis = redis.Redis(host="localhost", port=6379, db=0)
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        store function : saves data and returns the key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
        self, key: str, fn: Optional[Callable] = None
    ) -> Union[str, bytes, int, float]:
        """convert the data back to the desired format"""
        value = self._redis.get(key)
        return fn(value) if fn is not None else value

    def get_int(self, key: str) -> int:
        """parametrize Cache.get with correct conversion function"""
        value = self._redis.get(key)
        try:
            value = int(value.decode("utf-8"))
        except ValueError:
            value = 0
        return value

    def get_str(self, key: str) -> str:
        """parametrize Cache.get with correct conversion function"""
        value = self._redis.get(key)
        return value.decode("utf-8")
