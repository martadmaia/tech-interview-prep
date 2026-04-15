#### Description ####

#Até agora:  minutos

# Given an integer array nums sorted in non-decreasing order,
# remove the duplicates in-place such that each unique element 
# appears only once. The relative order of the elements should be kept the same.

# Consider the number of unique elements in nums to be k.
# After removing duplicates, return the number of unique elements k.

# The first k elements of nums should contain the unique numbers in sorted order. 
# The remaining elements beyond index k - 1 can be ignored.

#Primeira solução
#Runtime bate 100.00%
#Memory bate 66.42%
def remove_element_sorted_array(nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        print(id(nums))
        k = nums.count(val)
        nums[:] = [num for num in nums if num != val]+ [0 for i in range(k)]

        return k
