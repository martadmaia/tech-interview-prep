#Given a string of lowercase English Letters, rearrange the characters to form a new string
#representing the next immediate sequence in lexicographical order.
#If the given string is already last in lexicographical order among all possible arrangements,
#return the arrangement that's first in lexicographical order.

#What is the next lexicographical sequence?
#Say we have abc
#What is the greatest permutation of the string?
#cba (3 -> 2 ->1), instead of (1 -> 2 -> 3)

#What is the smallest permutation of the string?
#acb (1-> 3 -> 2)

#We want the next immediate sequence
#So the next string that is lexicographically "bigger"
#Which means, making the smallest possible change to the string, to get it a bigger order

#How do we find the suffix (the sequence at the end) that we need to change?
#Say we habe abcedda

#Is there anything we can do to edda, that would make it bigger? Or is it already in the highest
#order possible?

#So what is our pivot? What is the character that we CAN change to make the string bigger?
#If we change the c, to an e or a d, that would work.

#How do we choose which character to change it to?

#We want the next immediate sequence, not the greatest possible in order.

#So if we change the c to an e we get

#5 -> 3 -> 4 -> 4 -> 1

#If we change the c to a d we get

#4 -> 5 -> 4 -> 3 -> 1

#Going from right to left, we change the pivot (the first char we need to change) with
#the first char bigger than it

#But after this change, we're not done

#Our changed string is way too big now

#Just think that if it was d e d a c it would be larger than the original, but smaller than the changed string

#So what we do after changing the pivot, is reverse the suffix.

#That way we get next lexicographical sequence

#We use staged traversal

def nextLexicographicalSequence(s):

    letters = list(s)
    

    pivot = len(letters) - 2
    #Because we'll compare the second to last with the last
    #and so on

    #find the pivot
    while pivot >= 0 and letters[pivot] >= letters[pivot + 1]:

        pivot -= 1
        #We need to search until we find something smaller

    #if we got to the end of the string, and we didn't find anything smaller
    #it means the string is at its greatest possible lexicographical order
    #so we reverse it as per the requirements
    if pivot == -1:
        return "".join(reversed(letters)) #reversed is O(n), can also be achieved with list(s)[::-1]

    #so now we need to find the first element that is greater than our pivot
    #we start at the end of the string

    next_biggest_char = len(letters) - 1

    while letters[next_biggest_char] <= letters[pivot]:
        next_biggest_char -= 1

    letters[pivot], letters[next_biggest_char] = letters[next_biggest_char], letters[pivot]

    #finally reverse the sufix

    letters[pivot + 1:] = reversed(letters[pivot + 1:])

    return "".join(letters)

print(nextLexicographicalSequence("a"))
print(nextLexicographicalSequence("abcedda"))
print(nextLexicographicalSequence("ynitsed"))

    
        
    