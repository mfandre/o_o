# Using @property decorator
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value...")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value


celsius = Celsius(0)
celsius.temperature = 10
print(celsius.temperature)

# why: Readability and prevent to others coders make mess. Look the follow tutorial,
# you can make a property have private acess. In that way you prevent to outside users to change attributes that they souldnt.
# good tutorial: https://www.freecodecamp.org/news/python-property-decorator/
# I dont like... it's so confusing... but its important to know that exists!
