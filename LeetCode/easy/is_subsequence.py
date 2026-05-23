# Given two strings s and t, 
# return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string 
# that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

#if left pointer runs out - Means we found our solution
#if right pointer runs out - Means we can't find it

def isSubsequence(s, t):
    left = 0 #pointing at first element of s
    right = 0 #pointing at first element of t
    sub = []

    while left < len(s) and right < len(t):
        if s[left] == t[right]:
            left += 1
        right += 1

    return True if left == len(s) else False
                
        


print(isSubsequence("ab", "baab"))