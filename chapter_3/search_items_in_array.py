import bisect
from datetime import datetime
import timeit
from typing import List
  
# initializing list
list = []

for i in range(100000000):
    list.append(i)

value_to_search = 99999999

print(f"Normal Search")
starttime = timeit.default_timer()
for i in range(len(list)):
    if value_to_search == list[i]:
        endtime = timeit.default_timer()
        break
print(f"execution time = {endtime - starttime}")

print(f"Bisect search")
starttime = timeit.default_timer()
# Return the index where to insert item x in list to maintain this list ordered, assuming a is sorted. 
bisect.bisect(list, value_to_search)
endtime = timeit.default_timer()
print(f"execution time = {endtime - starttime}")


print(f"========= Let's test in a list of objects =========")
#### You can use bisect to search in object list:
class Model:
    name:str
    description:str
    creation_time:datetime

    def __eq__(self, other):
        return (
            self.name == other.name
            and self.creation_time == other.creation_time
        )

    def __lt__(self, other):
        """Order by date ascending"""
        return self.creation_time < other.creation_time

list:List[Model] = []
for i in range(1000000):
    model:Model = Model()
    model.creation_time = datetime.now()
    model.name = f"model{i}"
    model.description = f"description model{i}"
    list.append(model)


print(f"Bisect search")
starttime = timeit.default_timer()
# Return the index where to insert item x in list to maintain this list ordered, assuming a is sorted. 
m:Model = Model()
m.creation_time = datetime.now()
print(bisect.bisect(list, m))
endtime = timeit.default_timer()
print(f"execution time = {endtime - starttime}")