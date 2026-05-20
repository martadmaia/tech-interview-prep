# A phrase is a palindrome if, 
# after converting all uppercase letters into lowercase letters 
# and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters 
# and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

def isPalindrome(s):
    new_s = "".join(char for char in s.lower() if char.isalnum())

    left, right = 0, len(new_s) - 1

    while left < right:
        if new_s[left] == new_s[right]:
            left += 1
            right -= 1
        else:
            return False

    return True
            

print(isPalindrome(" "))