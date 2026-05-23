#Primeira solução
#Runtime bate 41.79%
#Memory bate 0.25%
#Tempo 6minutos
def missingNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    transform_set = set(nums) #usei set para otimizar lookup O(1)
    n = len(nums)


    for i in range(n + 1): #n + 1 para ser inclusive

        if i not in transform_set:
            return i



#Primeira solução
#Runtime bate 14.64%
#Memory bate 69.46%
#O(n²)
def missingNumber2(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)


    for i in range(n + 1): 
        if i not in nums:
            return i


#O(1) space - não posso usar hashmap

# Runtime 34.94%
# Memory 94.52%
def missingNumber3(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)

    #sorted_nums = nums.sort() CUIDADO que assim não é O(1)
    nums.sort() #Ler documentação, diferença entre sorted() e sort() 
    #O(n)

    #Ideia: verificar índice contra 
    #Erro index out of range
    for i in range(n): 
        if i != nums[i]:
            return i

    return n


