# A Python program to check if any two intervals overlap
 
# An interval has start time and end time
from datetime import datetime


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
 
# Function to check if any two intervals overlap
def isIntersect(arr, n):
   
    # Sort intervals in increasing order of start time
    arr.sort(key=lambda x: x.start)
 
    # In the sorted array, if start time of an interval
    # is less than end of previous interval, then there
    # is an overlap
    for i in range(1, n):
        if (arr[i - 1].end >= arr[i].start):
            return True
 
    # If we reach here, then no overlap
    return False
 
# Driver code
arr1 = [Interval(1, 3), Interval(7, 9), Interval(4, 6), Interval(10, 13)]
n1 = len(arr1)
if (isIntersect(arr1, n1)):
    print("Yes")
else:
    print("No")
 
arr2 = [Interval(6, 8), Interval(1, 3), Interval(2, 4), Interval(4, 7)]
n2 = len(arr2)
 
if (isIntersect(arr2, n2)):
    print("Yes")
else:
    print("No")

str_start_alarm1 = '01/01/22 00:00:01'
str_end_alarm1 = '01/01/22 00:00:10'

str_start_alarm2 = '01/01/22 00:00:04'
str_end_alarm2 = '01/01/22 00:00:16'

datetime_start_alarm1 = datetime.strptime(str_start_alarm1, '%m/%d/%y %H:%M:%S')
datetime_end_alarm1 = datetime.strptime(str_end_alarm1, '%m/%d/%y %H:%M:%S')

datetime_start_alarm2 = datetime.strptime(str_start_alarm2, '%m/%d/%y %H:%M:%S')
datetime_end_alarm2 = datetime.strptime(str_end_alarm2, '%m/%d/%y %H:%M:%S')

arr3 = [Interval(datetime_start_alarm1, datetime_end_alarm1), Interval(datetime_start_alarm2, datetime_end_alarm2)]
n3 = len(arr3)
 
if (isIntersect(arr3, n3)):
    print("Yes")
else:
    print("No")