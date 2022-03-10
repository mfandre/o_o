"""
Static methods allow you to create a method without SELF parameter. 
It can be called using the class name instead of to create a class instance to call the method.
"""

from datetime import datetime


class DateParserWithStatic:
    @staticmethod
    def parse_pi_date(date_str: str) -> datetime:
        try:
            has_milliseconds: bool = False

            if "." in date_str:
                has_milliseconds = True

            if has_milliseconds:
                if (
                    len(date_str) > 26
                ):  # this is because %f of python is only 6 digits and except when date is 2021-11-10T15:52:32.9200947Z (7 millisecond digits)
                    return datetime.strptime(
                        date_str[:26] + "Z", "%Y-%m-%dT%H:%M:%S.%fZ"
                    )
                return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%fZ")

            return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")
        except ValueError:
            return None


class DateParserWithoutStatic:
    def parse_pi_date(self, date_str: str) -> datetime:
        try:
            has_milliseconds: bool = False

            if "." in date_str:
                has_milliseconds = True

            if has_milliseconds:
                if (
                    len(date_str) > 26
                ):  # this is because %f of python is only 6 digits and except when date is 2021-11-10T15:52:32.9200947Z (7 millisecond digits)
                    return datetime.strptime(
                        date_str[:26] + "Z", "%Y-%m-%dT%H:%M:%S.%fZ"
                    )
                return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%fZ")

            return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")
        except ValueError:
            return None


# Static variables
class Example:
    Variable = 2  # static variable


print(Example.Variable)  # prints 2   (static variable)

# Access through an instance
instance = Example()
print(instance.Variable)  # still 2  (ordinary variable)


# Change within an instance
instance.Variable = 3  # (ordinary variable)
print(instance.Variable)  # 3   (ordinary variable)
print(Example.Variable)  # 2   (static variable)


# Change through Class
Example.Variable = 5  # (static variable)
print(instance.Variable)  # 3  (ordinary variable)
print(Example.Variable)  # 5  (static variable)

# Static methods
date1: datetime = DateParserWithStatic.parse_pi_date("2021-11-10T15:52:32.9200947Z")
print(date1)

parser2 = DateParserWithoutStatic()
date2: datetime = parser2.parse_pi_date("2021-11-10T15:52:32.9200947Z")
print(date2)
# will except... need to pass self attribute... we need to use the instance, that automatically pass self
date3 = DateParserWithoutStatic.parse_pi_date("2021-11-10T15:52:32.9200947Z")

# Why use static??? group methods/variables that can be executed/store without a instance...
# Most common use: parsers, constants, translations, cache (in memory)
