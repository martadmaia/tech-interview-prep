# Given an array of positive integers nums and a positive integer target, 
# return the minimal length of a whose sum is greater than or equal to target. 
# If there is no such subarray, return 0 instead.

#Exceeds time...
#Problems:
#Recalculating sum instead of incrementing/decrementing
#Pop(0) shifts all elements. I should use pointers instead.
def minSubArrayLen(target, nums):
    result = []
    current_sum = 0
    current_min = float("inf")

    for right in range(len(nums)):
        current_sum += nums[right]
        result.append(nums[right])

        print("Current number", nums[right])
        print("Current result", result)

        if current_sum >= target:
            print("Current sum > target")
            while (sum(result) - result[0]) >= target:
                result.pop(0)

            if len(result) < current_min:   
                current_min = len(result)

            print("After while", result)
            print("Current min", current_min)

    return current_min if current_min != float("inf") else 0
            
    
def minSubArrayLen2(target, nums):
    left, sum = 0, 0
    min_len = float("inf")
    
    for right in range(len(nums)):
        sum += nums[right]

        while sum >= target:

            #size of the window, for example
            #[1, 3, 2, 6, 2, 1], target = 9
            #left at 0
            #right at 3
            #size of window = 3 - 0 + 1 = 4
        
            min_len = min(min_len, right - left + 1) 
            sum -= nums[left]
            left += 1
            
    return 0 if min_len == float("inf") else min_len
    


print(minSubArrayLen2(15, [5,1,3,5,10,7,4,9,2,8]))