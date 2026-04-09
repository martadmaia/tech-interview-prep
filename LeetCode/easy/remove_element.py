#### Description ####

# Given an integer array nums and an integer val, remove all 
# occurrences of val in nums in-place. The order of the elements 
# may be changed. Then return the number of elements in nums which 
# are not equal to val.

# Consider the number of elements in nums which are not equal to val 
# be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums 
# contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k.

#Primeira solução
#Runtime bate 100.00%
#Memory bate 66.42%
def removeElement(nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        print(id(nums))
        k = nums.count(val)
        nums[:] = [num for num in nums if num != val]+ [0 for i in range(k)]

        return k




def removeElement2(nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        print("in Function")
        print(id(nums))
        k = nums.count(val)
        nums = [num for num in nums if num != val]
        nums =nums + [0 for i in range(k)]

        print("after modifying in function")
        print(id(nums))
        return k

nums = [3, 2, 2, 3]
val = 3
print("Before calling")
print(nums)
print(id(nums))
k = removeElement2(nums, val)
print("after calling")
print(nums)

print(id(nums))

###
#Careful!
#In the first solution, we are are changing it in place
#nums[:]= ...
#This allows us to modify it without assigning the variable to a new object. The id(nums) stays the same.
#We are assigning new values to the actual elements of that list.

#In the second solution we are virtually assigning a new object to nums. id(nums) changes. The pointer changes, and the outside, global variable, remains unchanged.





        

