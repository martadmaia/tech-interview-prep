#Given an array of integers, modify the array in place to move all zeros to the end while
#Maintaining the relative order of non-zero elements.
#Unidirectional traversal
def shiftZeros(nums):
    left = 0

    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]

            left += 1

    return nums
print(shiftZeros([0, 0, 1, 1, 1]))