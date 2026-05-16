#Find the max sum subarray of a fixed size k

def maxSumSizeK(nums, k):
    result = []
    current_sum = float("-inf")
    left = 0

    for right in range(k, len(nums) + 1):
        # print("Current number", nums[right])
        print(sum(nums[left:right]))
        if sum(nums[left:right]) > current_sum:
            result = nums[left:right]
            current_sum = sum(nums[left:right])
            print(result)
            print(current_sum)
        left += 1

    print(result)
    return current_sum

print(maxSumSizeK([4, 2, 1, 7, 8, 1, 2, 8, 1, 0], 3))  
print(maxSumSizeK([100, 200, 300, 400], 2))   
print(maxSumSizeK([1, 4, 2, 10, 23, 3, 1, 0, 20], 4))
print(maxSumSizeK([100, 200, 300, 400], 1))
        
    
    