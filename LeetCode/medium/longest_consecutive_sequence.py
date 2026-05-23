#Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

#You must write an algorithm that runs in O(n) time.

#consecutive elements 
#so no duplicates
#I had the right thinking here, of conceptualising the consecutiveness but I needed to find a way to isolate the sequences

def longestConsecutive(nums):
    result = set()
    visited_els = set()


    if len(nums) == 1:
        return 1

    for num in nums:
        print("CURRENT NUM", num)
        print("Result before checking", result)
        print("Visited before checking", visited_els)
        if num + 1 in visited_els or num - 1 in visited_els:
            if num + 1 in visited_els:
                result.add(num + 1)
            if num - 1 in visited_els:
                result.add(num - 1)
            result.add(num)
            visited_els.add(num)
        
        else:
            visited_els.add(num)

        print("Result after checking",result)
        print("Visited after checking",visited_els)

    return len(result)

# print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
# print(longestConsecutive([0]))
# print(longestConsecutive([]))
# print(longestConsecutive([0,2,3,1,10,12,11,14,15,13]))


#O(nlogn) > O(n)
#So this approach doesn't meet requirements
#And it doesn't work with duplicates
#It fails on all accounts
def longestConsecutive2(nums):
    nums.sort()
    max_sequence = 0
    start_sequence = 0

    print("Numbers after sorting", nums)

    for index in range(1, len(nums)):
        print("Current number", nums[index])
        print("Difference between current and previous", nums[index] - nums[index - 1])
        if nums[index] - nums[index - 1] != 1:
            print("Entered the if")
            max_sequence = max(max_sequence, (index - 1) - start_sequence + 1)
            start_sequence = index


    max_sequence = max(max_sequence, (len(nums) - 1) - start_sequence + 1)

    return max_sequence
            
print(longestConsecutive2([1, 0, 1, 2]))

#get the start of the sequence, by looking for the numbers that don't have a left neighbor
#Take the array and convert into set
def longestConsecutive_3(nums):
    nums_set = set(nums)
    max_sequence = 0

    for number in nums_set:
        if (number - 1) not in nums_set: #start of sequence
            length_current_sequence = 1
            #while consecutive numbers increase sequence length
            while (number + length_current_sequence) in nums_set:
                length_current_sequence += 1
            max_sequence = max(max_sequence, length_current_sequence)

    return max_sequence
    