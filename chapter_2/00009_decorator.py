# A decorator: It lets us add new functionality to an existing function without modifying it.
# Its powerful!!! Give us a way to separe concepts and decouple our code!

# imagine that we have this funcion:
# def initial_function():
#    print("Initial Functionality")


import functools

# Now I want to add more logic in it withou change the orignal one!
from datetime import datetime
from time import sleep


def my_crazy_decorator(f):
    def new_function():
        print("Extra Functionality")
        f()

    return new_function


@my_crazy_decorator
def initial_function():
    print("Initial Functionality")


initial_function()


# Looks simple, and it is simple!
# The python understands the @decorator_name sintax and do the magic to you!

# its possible to create a decorator inside a class. Its improve readability and organize better.


class Cache(object):
    cache_data: dict = {}

    def __init__(self, any_parameter):
        self.any_parameter = any_parameter

    def check_in_cache(self, key):
        if key not in Cache.cache_data:
            return None
        value = Cache.cache_data[key]
        return value

    def set_in_cache(self, key, value):
        Cache.cache_data[key] = value

    def __call__(self, fn):
        @functools.wraps(fn)  # only to preserve the orignal func documentation
        def decorated(*args, **kwargs):
            key = fn.__name__

            print(
                f"you can use self.any_parameter {self.any_parameter} inside your logic!"
            )
            cache_value = self.check_in_cache(key)
            if cache_value is None:
                cache_value = fn(*args, **kwargs)
                self.set_in_cache(key, cache_value)

            return cache_value

        return decorated


class SimulateHttpRequestWithouCacheDecorator:
    def get(self, url: str) -> str:
        return f"{str(datetime.now())} | {url}"


class SimulateHttpRequest:
    @Cache("1")
    def get(self, url: str) -> str:
        return f"[GET] {str(datetime.now())} | {url}"

    def post(self, url: str) -> str:
        return f"[POST] {str(datetime.now())} | {url}"


request_without_cache = SimulateHttpRequestWithouCacheDecorator()

print(request_without_cache.get("url1"))
sleep(1)
print(request_without_cache.get("url2"))
sleep(1)
print(request_without_cache.get("url3"))


request = SimulateHttpRequest()
print(request.get("url1"))
sleep(1)
print(request.get("url2"))
sleep(1)
print(request.get("url3"))
