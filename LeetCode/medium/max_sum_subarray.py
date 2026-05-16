#Given an integer array nums, 
# find the subarray with the largest sum, 
# and return its sum.

def maxSubArray(nums):
    """
        :type nums: List[int]
        :rtype: int
    """
    
    result = [nums[0]]
    left = 0
    current_sum = float("-inf")

    for right in range(len(nums)):
        print("Current number", nums[right])
        print("Current sum", current_sum)
        
        if sum(result) + nums[right] > current_sum:
            print("Sum of result array + current number > current_sum")
            result.append(nums[right])
            current_sum = sum(result)

            print("After adding current number", result)
            print("Current sum", current_sum)
        else:
            result.pop(0)
            result.append(nums[right])
            left += 1

            print("sum is not greater")
            print("Updated result array", result)

    return max(current_sum, sum(nums))

print(maxSubArray([5, 4, -1, 7, 8]))

#Negative numbers don't contribute anything
#If array is made up of negative numbers, then the max subarray is just [max_value], the greatest negative number

#Neetcode's solution
#Remove negative prefixes
#Anytime current sum is negative we disregard it
#And reset the sum

def maxSubArray2(nums):
    """
        :type nums: List[int]
        :rtype: int
    """
    
    result = nums[0]
    current_sum = float("-inf")

    for num in nums:
        if current_sum < 0:
            current_sum = 0
        current_sum += num
        result = max(result, current_sum)

    return result
