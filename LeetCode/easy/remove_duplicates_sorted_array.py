#### Description ####

#Até agora: 73 minutos

# Given an integer array nums sorted in non-decreasing order,
# remove the duplicates in-place such that each unique element 
# appears only once. The relative order of the elements should be kept the same.

# Consider the number of unique elements in nums to be k.
# After removing duplicates, return the number of unique elements k.

# The first k elements of nums should contain the unique numbers in sorted order. 
# The remaining elements beyond index k - 1 can be ignored.

#Primeira solução (...)
#Runtime bate 59.38%
#Memory bate 5.21%

nums = [0,0,1,1,1,2,2,3,3,4]

def remove_element_sorted_array(nums):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        current_num = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == current_num:
                nums[i] = "_"

            else:
                current_num = nums[i]
        
        nums[:] = [x for x in nums if x != "_"]

        return len(nums)
            

#
def remove_element_sorted_array_2(nums):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        nums[:] = sorted(set(nums))
        return len(nums)
        

                
                
print(remove_element_sorted_array_2(nums))
print(nums)
