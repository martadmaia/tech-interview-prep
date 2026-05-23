#Given two strings ransomNote and magazine, 
#return true if ransomNote can be constructed by using 
#the letters from magazine and false otherwise.
#Each letter in magazine can only be used once in ransomNote.

#My thinking is -> populate a dictionary with the available chars in magazine
#Use that dictionary to check if all the chars in ransom note exist or not in magazine
#Optimised lookups, and can keep track of quantities

#Runtime beats 79.04%
#Memory beats 87.20%

#Took 7 minutes to think of and implement

#Let's think Complexity: 
#O(n) for space -> dictionary can have n entries (n being the size of magazine)
#Wrong -> dictionary can have 26 entries at most, so constant O(1)
#From the description
#ransomNote and magazine consist of lowercase English letters.
#O(n + m) for time -> iterate over magazine and over ransom with o(1) lookups 
def canConstruct(ransomNote, magazine):
    available_chars = {}

    for char in magazine:
        if char in available_chars:
            available_chars[char] += 1
        else:
            available_chars[char] = 1

    for char in ransomNote:
        if char in available_chars and available_chars[char] >= 1:
            available_chars[char] -= 1
        else:
            return False

    return True

#Can optimise using defaultdict() and saving the checking of whether the chat already
#exists in available_chars
#Beats 87.77% runtime

