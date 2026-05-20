# Given a 1-indexed array of integers numbers 
# that is already sorted in non-decreasing order, 
# find two numbers such that they add up to a 
# specific target number. 
# Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers index1 and index2, 
# each incremented by one, as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Your solution must use only constant extra space.

def twoSum(numbers, target):
    left = 0

    while left < len(numbers):

        for number in numbers[left + 1:]:
            sum = numbers[left] + number

            if sum == target:
                return [left + 1, numbers.index(number)+ 1]
                #index doesn't work, since there might be duplicates in the array, and I'll get the index of the first one

                #My right pointer should be updated as I go... Instead of a messy loop.   

            if sum > target:
                break

        left += 1

#My implementation after learning about NC's approach
#left pointer -> <- right pointer
#Because it's sorted we can do this
#And because we're told there's a unique solution each time
def twoSum2(numbers, target):
    left = 0
    right = len(numbers)-1

    while right > left:
        sum = numbers[left] + numbers[right]

        if sum > target:
            right -= 1

        elif sum < target:
            left += 1

        else:
            return [left + 1, right + 1]

print(twoSum2([-1,0], -1))
            
    

        

        

        