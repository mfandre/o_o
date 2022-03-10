# A function that can accept different types

from turtle import pen
from typing import List

print(len([1, 2, 3]))

print(len("minha string"))


# An object method that overrides the parent method (same signature)
# look the example below, the animal can have different behaviors on children objects


class Animal:
    _name: str = "Noname"

    def __init__(self, name: str = None):
        self._name = name

    def name(self):
        print(self._name)

    def intro(self):
        print("I`m an animal")


class Bird(Animal):
    def intro(self):
        print("I`m a bird!!!")

    def flight(self):
        print(">>>>>>>Most of the birds can fly but some cannot.")


class Penguin(Bird):
    def flight(self):
        print(">>>>>>>Fck... I can't fly... but I can swim")

    def swim(self):
        print("I`m Swimming")


class Dog(Animal):
    def run(self):
        print("I`m Running")


print("###### animal")
animal: Animal = Animal()
animal.intro()

print("###### penguin")

penguin: Animal = Penguin("duhh")
penguin.intro()
penguin.flight()
penguin.swim()

print("###### generic_bird")

generic_bird: Animal = Bird("rare bird")
generic_bird.intro()
generic_bird.flight()

print("###### dog")

dog: Animal = Dog("tod")
dog.intro()
dog.run()

print("###### list all animals")
# But where it helps me????
# + Reuse behaviors, like flight to other birds that can flight
#   - you wont need to recode it to all birds since almost can fly, you just need to define the parent class
# + You can apply different behaviors in the child class...
#   - look the flight of penguin... the behavior is diferent from his father (parent class)!
list_of_animals: List[Animal] = [dog, generic_bird, penguin, animal]
for i in range(len(list_of_animals)):
    list_of_animals[i].name()
    list_of_animals[i].intro()
