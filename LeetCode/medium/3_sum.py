# Given an integer array nums, 
# return all the triplets [nums[i], nums[j], nums[k]] 
# such that i != j, i != k, and j != k, 
# and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set 
# must not contain duplicate triplets.

#O(n^2)
def threeSum(nums):
    if len(nums) == 3 and sum(nums) == 0:
        return [nums]

    result = []
    
    #sort to keep track of and prevent duplicates
    #If we get to a point and all the elements are positive
    #no point in carrying on
    #We basically want to find out first possible number
    #and then run two sum

    nums.sort() #O(nlogn)

    for index, num in enumerate(nums):
        #Because of the duplicates
        #If the previous element is the same, we've already checked
        #all possible solutions with that element in the starting
        #position
        if index > 0 and num == nums[index-1]:
            continue

        left, right = index + 1, len(nums) - 1

        while left < right:
            three_sum = num + nums[left] + nums[right]

            if three_sum > 0:
                right -= 1
            elif three_sum < 0:
                left += 1
            else:
                result.append([num, nums[left], nums[right]])
                left += 1
                while nums[left] == nums[left - 1] and left < right:
                    left += 1

    return result
    
print(threeSum([-1,0,1,2,-1,-4]))

#Returning to it following Alex xu's book
#Given an array of integers, return all triplets such that a+b+c = 0.
#The solution must not contain duplicate triplets.
#If no such triplets are found, return an empty array.
def threeSum2(nums):
    nums.sort() #O(nlogn)
    
    result = [] #for storing valid triplets
    #loop for choosing my first element

    for index, num in enumerate(nums):

        if num > 0:
            break

        if index > 0 and nums[index - 1] == num:
            continue
        
        left, right = index + 1, len(nums) - 1

        while left < right:
            sum_three = num + nums[left] + nums[right]

            if sum_three > 0:
                right -= 1
            elif sum_three < 0:
                left += 1
            else:
                result.append([num, nums[left], nums[right]])
                left += 1

                while nums[left] == nums[left - 1] and left < right:
                    left += 1
    return result
    
                

        

        
    


    
    
    

    