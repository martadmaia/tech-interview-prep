#My thinking here is to map it to an integer version, where
#each char corresponds to a particular int, 
#maintaining the order of appearance of the char
#I then compare the two mapped strings, and if they have the exact same pattern
#I return true

#Runtime beats 70.46%
#Memory beats 88.90%

#Complexity O(2n) -> O(n)
#Strings are the same size, so two for loops.
def map_to_string(string):
    result = []
    count_distinct = 0
    map_char_int = {}
    
    for char in string:
        if char in map_char_int:
            result.append(map_char_int[char])
        else:
            count_distinct += 1
            map_char_int[char] = count_distinct
            result.append(count_distinct)

    return result

def isIsomorphic(s, t):
    s_mapping = map_to_string(s)
    t_maping = map_to_string(t)

    return s_mapping == t_maping
    

print(isIsomorphic("f11", "b23"))