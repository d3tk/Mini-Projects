## binary search project 
# Start: January 20th 2022
# End: January 20th 2022
# Declan Kutscher github: d3tk 

import random as rd
import time

# naive search
# return index if found, -1 if not found.
def naive_search(i, key):
    for num in range(len(i)):
        if i[num] == key:
            return num
    return -1


#binary search
#return index if found, else return -1
def binary_search(nums, key, lo = None, hi = None):
    nums.sort() # sort if not already sorted.

    if hi is None:
        hi = len(nums) - 1 
    if lo is None:
        lo = 0
    if hi < lo:
        return -1
    
    mdpt = (hi + lo)//2

    if nums[mdpt] == key:
        return mdpt
    elif key < nums[mdpt]:
        return binary_search(nums, key, lo, hi = mdpt-1)
    else:
        return binary_search(nums, key, mdpt+1, hi)

if __name__ == '__main__':
    length = 10000

    sortedList = set()
    while len(sortedList) < length:
        sortedList.add(rd.randint(-3*length, 3*length))
    sortedList = sorted(list(sortedList))

    start = time.time()
    for target in sortedList:
        naive_search(sortedList, target)
    end = time.time()
    print("Naive search time: ", (end - start), "seconds")

    start = time.time()
    for target in sortedList:
        binary_search(sortedList, target)
    end = time.time()
    print("Binary search time: ", (end - start), "seconds")



