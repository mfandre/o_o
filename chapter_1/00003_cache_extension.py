class entity:
    """
    entity
    """

    id: str = 0


class eventframe(entity):
    pass


class Cache:
    def add(self, key: str, value: object):
        """
        Add a key/value entry to the cache
        """

    def get(self, key: str) -> object:
        """
        Get a value using the passed key from cache
        """

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
        if key in self.cache:
            self.cache[key] = None

    def get(self, key: str):
        if key in self.cache:
            return self.cache[key]
        return None


class FileCache(Cache):
    pass


class DbCache(Cache):
    pass


if __name__ == "__main__":
    file_cache = FileCache()
    file_cache.add("a", "b")  # will do nothing... is not implemented
    file_cache.add("c", "d")  # will do nothing... is not implemented

    memmory_cache = MemmoryCache()

    memmory_cache.add("key1", [1, 2, 3])
    memmory_cache.add("key2", "string")

    print(memmory_cache.get("key1"))
    print(memmory_cache.get("key2"))

    a = eventframe()
    print(a.id)
    print(isinstance(a, entity))
