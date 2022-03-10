# Its important to read 00004_cache_interface.py BEFORE!!!
# This file will make more sense after you read the previous example!

from abc import ABC, abstractmethod
from time import sleep


class Cache(ABC):
    @abstractmethod
    def add(self, key: str, value: object):
        """
        Add a key/value entry to the cache
        """

    @abstractmethod
    def get(self, key: str) -> object:
        """
        Get a value using the passed key from cache
        """

    @abstractmethod
    def remove(self, key: str):
        """
        Remove a value using the passed key from cache
        """


# look the documentantion get from Parent class
class MemmoryCache(Cache):
    cache: dict = {}

    def add(self, key: str, value: object):
        self.cache[key] = value

    def remove(self, key: str):
        self.cache[key] = None

    def get(self, key: str):
        if key in self.cache:
            return self.cache[key]
        return None


class NullCache(Cache):
    def add(self, key: str, value: object):
        """Do nothing"""

    def remove(self, key: str):
        """Do nothing"""

    def get(self, key: str):
        return None


class DoSomeCrazyJobWithoutDependencyInjection:
    attribute1: int
    attribute2: int
    cache: MemmoryCache

    def __init__(self, attr1: str, attr2: int):
        self.attribute1 = attr1
        self.attribute2 = attr2
        self.cache = MemmoryCache()

    def some_work_to_be_done(self) -> int:
        value: int = self.cache.get("some_work_to_be_done")
        if value is None:
            sleep(5)  # just to be slow
            value = self.attribute1 + self.attribute2
            self.cache.add("some_work_to_be_done", value)

        return value

    def some_other_work(self) -> int:
        value: int = self.cache.get("some_other_work")
        if value is None:
            sleep(5)  # just to be slow
            value = self.attribute1 * self.attribute2
            self.cache.add("some_other_work", value)

        return value


class DoSomeCrazyJobDependencyInjection:
    attribute1: int
    attribute2: int
    cache: Cache

    def __init__(self, attr1: str, attr2: int, cache: Cache):
        self.attribute1 = attr1
        self.attribute2 = attr2
        self.cache = cache

    def some_work_to_be_done(self) -> int:
        value: int = self.cache.get("some_work_to_be_done")
        if value is None:
            value = self.attribute1 + self.attribute2
            self.cache.add("some_work_to_be_done", value)

        return value

    def some_other_work(self) -> int:
        value: int = self.cache.get("some_other_work")
        if value is None:
            value = self.attribute1 * self.attribute2
            self.cache.add("some_other_work", value)

        return value


if __name__ == "__main__":
    test1: DoSomeCrazyJobWithoutDependencyInjection = (
        DoSomeCrazyJobWithoutDependencyInjection(2, 3)
    )

    # first hit cache, and dont exists keys... slow because sleeps
    print("first hit cache, and dont exists keys... slow because sleeps")
    print(test1.some_work_to_be_done())
    print(test1.some_other_work())

    # second hit cache... should be fast because already exists in cache
    print("second hit cache... should be fast because already exists in cache")
    print(test1.some_work_to_be_done())
    print(test1.some_other_work())

    # now imagine if I want to change my cache to memmory cache...
    # I will need to modify my file and replace memmory to another cache that I want...
    # Its ok... but can be much better using DEPENDENCY INJECTION...
    # Why we dont put our cache creation out side of my DoSomeCrazyJob class?
    # look the class DoSomeCrazyJobDependencyInjection, we add cache in our constructor...
    # and if we want to pass a new type of cache we just neeed to do something like that:

    print(
        "Dependency Injection example... will be fast because I remove the sleep, and the cache do nothing..."
    )
    null_cache: Cache = MemmoryCache()
    test2: DoSomeCrazyJobDependencyInjection = DoSomeCrazyJobDependencyInjection(
        100, 40, null_cache
    )
    print(test2.some_work_to_be_done())
    print(test2.some_other_work())
