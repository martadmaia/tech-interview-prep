from collections import defaultdict

#Brute force intuition is just nested loops
#o(n^2)

#How to find an anagram?
#String has to contain all words in another string
#If I order the strings alphanumerically and compare them
#It should true return if they're the same, and thus an anagram, or false, it they
#don't contain all the same characters

#So if I just store the sorted version of the word, and then
#use that to look up, I should get O(n) time complexity

#Beats 83.16% runtime
#Beats 97.62% memory
#Spent 15 minutes
#What's my complexity?
#Memory O(n), worst case scenario my map grows to the size of strs
#Runtime -> sorted is O(nlogn) (n in this case is the size of the string), for loop O(n) --> so O(s log s * n),

def groupAnagrams(strs):
    seen_words = {} #O(1) for lookups
    

    for str in strs:
        sorted_str = "".join(sorted(str))

        if sorted_str in seen_words:
            seen_words[sorted_str].append(str)
        else:
            seen_words[sorted_str] = [str]

    return list(seen_words.values())

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

#With character frequency counting
#Key is now the frquency array for a particular str
#Values are all the strs with that same frequency array
#O(m*n*26) (So the length of the strs array * the length of the str * 26 for counting the frequency of the 26 lowercase chars)
def groupAnagrams_2(strs):
    result = defaultdict(list)
    #so we don't have to check if the value already exists or not, and can just append
    #remember that lists can't be keys, since they're mutable
    #so instead of a frequency array, we'll change it to a tuple - immutable

    for str in strs:
        count = [0] * 26 # one 0, for each lowercase char

        for char in str:
            count[ord(char) - ord("a")] += 1
            #ord returns the integer that represents char
            #it's any char though, so we need to subtract the value of a to get a number in the right range

        result[tuple(count)].append(str)

    return result.values()

    

    

    
    
    

