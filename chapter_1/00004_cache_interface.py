from abc import ABC, abstractmethod


class Cache(ABC):
    @abstractmethod
    def add(self, key: str, value: object):
        """
        Add a key/value entry to the cache
        """

    @abstractmethod
    def get(self, key: str):
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

    def my_specific_method(self):
        print("my specific mehtod")

        


class FileCache(Cache):
    pass


if __name__ == "__main__":
    memmory_cache = MemmoryCache()

    memmory_cache.add("key1", [1, 2, 3])
    memmory_cache.add("key2", "string")
    memmory_cache.my_specific_method()
    print(memmory_cache.get("key1"))
    print(memmory_cache.get("key2"))

    # will raise because the child class not implement all methods!
    # and why this is important???
    # Because you can define CONTRACTS, if a new developer want to create a new cache,
    # he MUST create those methods or will fail.
    # But the real benefit is... imagine you use this Memmory Cache at you application,
    # if do you want to change all to file cache, you just simple need to replace MemmoryCache to FileCache,
    # because ALL your code use the SAME METHODS call... the change is very easy...
    # Stay in mind, its better to develop to interface than to fixed parameters, its uncouple your code,
    # and permit to easly add extensions!
    print("will raise because the child class not implement all methods!")
    file_cache = FileCache()
    file_cache.add("a", "b")
    file_cache.add("c", "d")
