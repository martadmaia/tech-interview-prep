#Given an array of integers, return the indexes of any two numbers that add 
#up to a target.
#The order of the indexes in the result doesn't matter.
#If no pair is found, return an empty array.

#Using hasmaps
#Could I store a key:value pair, of index:remainder for each visited element,
#And then for each iteration, if there is an element with the remainder I need, return that

def pair_sum(arr, target):
    visited_els = {}

    for index, num in enumerate(arr):
        remainder =  target - num

        if num in visited_els:
            return [visited_els[num], index]
        else:
            visited_els[remainder] = index

    return []

print(pair_sum([-1, 3, 4, 2], target=3))
print(pair_sum([-4, 0, 3, 2, -2, 1, 6], target=5))