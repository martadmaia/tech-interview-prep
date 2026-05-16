#Sliding window
#Two Pointers

# Given a string s, find the length of the longest substring without duplicate characters.

#Need to keep track of chars already present
#Need to keep track of longest running sequence

def lengthOfLongestSubstring(s):
    visited_chars = []
    counter = 0

    string_len = len(s)

    if string_len == len(set(s)):
        return string_len
    
    for char in s:
        print("Current char", char)
        
        if char in visited_chars: #already had that char, need to reset the counter, but still preserve the best sequence so far
            visited_chars.append(char) #we need to keep the sequence going, now starting at current char

            print("Visited chars after adding", visited_chars)
            print("Set:", set(visited_chars))
            if set(visited_chars) != set(visited_chars[1:]): #Esta comparação não funciona
                print("Entered")
                counter = max(counter, len(visited_chars) - 1)
                visited_chars = [visited_chars[-1]]
            else:
                visited_chars.pop(0) #Retiramos o primeiro elemento, e continuamos
            
        else:
            visited_chars.append(char)

        print("Visited chars", visited_chars)

    return max(counter, len(visited_chars))


#Explicação Neetcode com Sliding Window
#É bom perceber que foi esse o meu pensamento, mesmo sem saber o nome do conceito
#Foi o que tentei fazer com o pop(0). "Encurtar" a janela.
#Também usa sets.
#Ele diminui a janela até não ter duplicates - neste caso "abcb", remove a -> "bcb", remove b -> "cb"
#Mas tem de ter maneira de ver qual foi o substring mais longo até ao momento
#Fazer um max depois com esse contador e com substring final
#Sliding window exige dois pointers
def lengthOfLongestSubstring2(s):
    unique_chars = set()
    left = 0
    result = 0

    for right in range(len(s)):
        while s[right] in unique_chars:
            unique_chars.remove(s[right])
            left += 1

        unique_chars.add(s[right])
        result = max(result, right - left + 1)

    return result
        