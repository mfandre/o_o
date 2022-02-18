# Encapuslation: protected your attributes!!!
# in python it is awkard because you dont have REAL private/protect methods/attributes

from turtle import pen
from typing import List


class Animal:
    __name: str = "Noname"

    def __init__(self, name: str = None):
        self.__name = name

    def name(self):
        print(self.__name)

    def intro(self):
        print("I`m an animal")

    def set_name(self, name):
        self.__name = name.replace("_", "")


animal: Animal = Animal("aaa")

animal.name()
print(animal._Animal__name)  # the reason to it be awkard
print(animal.__name)  # will except
