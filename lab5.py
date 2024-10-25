import data
import math

# Write your functions for each part in the space below.

# Part 1
   # The function for Part 1 should be within the class in data.py.


# Part 2
   # The function for Part 2 should be within the class in data.py.


# Part 3
# Calculates the sum of two times
# INPUT: two Time objects to be added
# OUTPUT: Time object representing the sum of the input
def time_add(a : data.Time, b : data.Time) -> data.Time:
    seconds = a.second + b.second
    minutes = a.minute + b.minute + seconds // 60 # makes sure seconds remain under 60
    hours = a.hour + b.hour + minutes // 60 # makes sure minutes remain under 60
    seconds = seconds % 60
    minutes = minutes % 60
    return data.Time(hours, minutes, seconds % 60)

# Part 4
# Determines whether the elements in the list are strictly descending
# INPUT: list[float] whose values are to be tested
# OUTPUT: bool representing if the list is descending
def is_descending(float_list : list[float]) -> bool | None:
    if len(float_list) == 0:
        print("No values to test.")
        return None
    curr = float_list[0]
    for n in float_list:
        if (n > curr):
            return False
        curr = n
    return True

# Part 5
# Returns the index of the largest number in a list over a specified interval
# INPUT:  list[int] to be iterated over
# INPUT: integer to be the lower index, integer to be the higher index to be iterated through
# OUTPUT: integer representing the index of the largest number over the given interval
def largest_between(nums : list[int], lower : int, higher : int) -> int:
    if lower > higher: # Switches the value of lower and higher if lower > higher
        temp = lower
        lower = higher
        higher = temp
    largest = nums[lower]
    largest_index = lower
    for i in range(lower,higher):
        if (nums[i] > largest):
            largest = nums[i]
            largest_index = i
    return largest_index

# Part 6
# Calculates the distance between two points
# INPUT: 2 arguments of Point whose distance will be calculated
# OUTPUT: float representing the distance between the two Points
def distance(a : data.Point, b : data.Point) -> float:
    return math.sqrt((b.x - a.x)**2 + (b.y - a.y)**2)

# Determines the index of the Point farthest from the origin in a given list
# INPUT: list of type Point to be iterated over
# OUTPUT: index representing the index of the Point in the list that's farthest from the origin
def furthest_from_origin(points : list[data.Point]) -> int:
    origin = data.Point(0,0)
    if len(points) == 0: return None
    furthest = points[0]
    furthest_index = 0
    for i in range(len(points)):
        if (distance(points[i], origin) > distance(furthest, origin)):
            furthest = points[i]
            furthest_index = i
    return furthest_index