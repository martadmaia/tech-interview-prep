#Given an integer array nums and an integer k, 
#return true if nums has a good subarray or false otherwise.
#A good subarray is a subarray where:
#     its length is at least two, and
#     the sum of the elements of the subarray is a multiple of k.
# Note that:
#     A subarray is a contiguous part of the array.
#     An integer x is a multiple of k if there exists an integer 
#     n such that x = n * k. 0 is always a multiple of k.

#I don't have any negative numbers in my array, as per the constraints.
#So what might happen is a subarray like this [0, 0], which would be suitable in this case

#So I can stop as soon as I find a suitable subarray
#I'll need to implement a sliding window (dynamically sized?)

#Brute force aproach
#O(n^2)
def checkSubarraySum(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """

    for i in range(len(nums)):
        current_sum = nums[i]
        
        for j in range(i + 1, len(nums)):
            
            current_sum += nums[j]

            if current_sum % k == 0:
                return True


    return False

    


print(checkSubarraySum([23, 2, 6, 4, 7], 13))

#Neetcode's proposed solution using hashmap
#His logic
#If I calculate the remainder, of a subarray, and hash it, so key is the remanider and the index is the end of that array
#when I move through my array, and add another element
#if I somehow get the same remainder from that sum, that means I must have added a multiple of 6

#let's see
#23 % 6 = 5 (23 - 18)
#23 + 2 = 25 % 6 = 1
#25 + 4 = 29 % 6 = 5

#So since [23] and [23, 2, 4] have the same remainder, that means that I must have added a 6
#How did I get from 23 to 29, and get the same remainder? I had to have added a 6, so there has to be a subarray whose sum is 6.
#How do I find it?

def checkSubarraySum2(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    #First entry, to prevent us from returning true when the first element is a multiple of k.
    #Remember, a good array has to be at least 2 elements long.
    remainder_map = {0: -1}
    current_sum = 0

    for index, num in enumerate(nums):
        current_sum += num
        remainder = current_sum % k

        if remainder not in remainder_map:
            remainder_map[remainder] = index
         
        elif index - remainder_map[remainder] > 1:
            return True

    return False

#For returning the indexes I would need to return
#[remainder_map[remainder] + 1, index] ?
        
        
