from typing import List


class Animal:  # simple class
    __name: str = "Noname"  # "private" attribute, but take care... python is awkard with private...
    attribute: int = 0  # public attribute

    def __init__(
        self, name: str = None
    ):  # constructor, with name parameter with default value None
        self.__name = name

    def name(self):  # method
        print(self.__name)

    def intro(self):  # method
        print("I`m an animal")


class Bird(Animal):  # Inheritance... a bird is an animal
    pass


print("lets create an animal:")
animal: Animal = Animal(
    "animal1"
)  # animal is an object because IS AN INSTANCE OF Animal class
print(animal)  # will print something like <__main__.Animal object at 0x10c05ecd0>
# this is the address "0x10c05ecd0" of the object animal that you create

# if you call animal.name you are getting the name of object that are save in the memory address 0x10c05ecd0
animal.name()  # calling a method... its calling the name the specific object that you create

print("lets create another animal:")
animal2: Animal = Animal(
    "animal2"
)  # animal is an object because IS AN INSTANCE OF Animal class
print(animal2)  # check the addres will be different
animal2.name()

print ("======= animal 3")

animal3: Animal = Animal(
    "animal3"
) 
animal3.attribute = animal3.attribute + 1

print ("======= animal 4")
animal4: Animal = Animal(
    "animal4"
) 
print(animal4.attribute)

print("The address will be different, so you HAVE two animals saved in your memmory!")

# How its "saved in memmory? The python interpreter say to Operational System (OS):
# - Python: Hey I want to save this bunch of bytes (you object is converted to byte behind the scenes)
# - OS: If the OS has free memmory it will save in some Address and the python will receive this address...
#       If not probably you gonna receive some memmory allocation exception


# About private attributes...
# print(animal._Animal__name)  # It will print the name of the attribute the reason to it be awkard
# print(animal.__name)  # will except... uncomment and try it!!!


# But you are asking... why this shit is important... and how it will help me to
# build better software:
# Using polymorphism and inheritance, object-oriented programming allows you to
# reuse individual components. In an object-oriented system, the amount of work
# involved in revising and maintaining the system is reduced, since many problems
# can be detected and corrected in the design phase.


# Lets go file by file...
