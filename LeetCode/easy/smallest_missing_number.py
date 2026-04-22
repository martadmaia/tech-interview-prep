def findSmallestMissingPositive1(orderNumbers):
    
    if not len(orderNumbers):
        return 1
        
    if len(orderNumbers) == 1 and orderNumbers[0] == 1:
        return 2
        
    for i in range(len(orderNumbers)):
        if i + 1 not in orderNumbers:
            return i + 1

    return len(orderNumbers) + 1

#Second solution
#Constant memory
#We use the original array as a hashmap
def findSmallestMissingPositive2(orderNumbers):
    
    pos_range = len(orderNumbers)
    contains_1 = False #we check this because we'll be changing invalid elements to 1 after

    for i in range(pos_range):
        if orderNumbers[i] == 1:
            contains_1 = True
        if not (0 < orderNumbers[i] <=pos_range):
            orderNumbers[i] = 1

    if not contains_1:
        return 1

    #edge case when array is [1]
    #probably need to handle differently
    if len(orderNumbers) == 1 and orderNumbers[0] == 1:
        return 2

    #So now we change values to the negative, but we don't change absolute values
    #The goal is marking every element that exists, and turn its corresponding index's value to negative
    #So: [3, 1, 6, 3]
    #If I'm iterating over the first 3 (index 0)
    #I would go to index 3 - 1, which is 6 and turn it to -6
    #That way, I know 3 exists somewhere in my array
    for i in range(pos_range):
        value = abs(orderNumbers[i])

        if value - 1 < pos_range:
            orderNumbers[value - 1] = -abs(orderNumbers[value - 1])

    #finally check for positive numbers
    #first positive number we find is the missing integer
    for i in range(pos_range):
        if orderNumbers[i] > 0:
            return i + 1

    #if nothing was returned that means the entire range of possible numbers is covered
    #ex. [1, 2, 3]
    #in this case the smallest missing integer is the len(numbers) + 1
    return pos_range + 1

#Requires auxiliary set
#So O(n) for memory
#Take away from this
#Set look up is O(1)!!!!!!!! Hence the faster runtime!!!
#Set look up O(1) != List look up O(n)!!!!!
def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=1
        nums=set(nums)
        while True:
            if i not in nums:
                return i
            i+=1