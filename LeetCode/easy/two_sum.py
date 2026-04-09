#### Description ###

#Até agora: 80 minutos

#Given an array of integers nums and an integer target, 
#return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, 
#and you may not use the same element twice.
#You can return the answer in any order.

#recebe array com números (ints)
#retorna índices de números que adicionados atingem número alvo

#instinto é passar pela lista, pegar num número e comparar com todos os números a seguir, assim que encontrar break, porque a solução é única


#1ª Solução
#Accepted, mas solução fraca
#Runtime bate 20.44% das soluções 
#Memory bate 25.37% das soluções

def two_sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    result = [0, 0]

    for index in range(len(nums)):
        result[0] = index

        for index_2 in range(index + 1, len(nums)):
            if nums[index] + nums[index_2] == target:
                result[1] = index_2

                return result
            
#E se calcular o resto consoante o número do indíce atual e o alvo, e comparar só? Comparações mais rápidas do que somas não?
#2ª Solução
#Accepted, melhor do que a primeira em termos de runtime
#Runtime bate 39.57%
#Memory bate 25.37%
def two_sum_2(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    result = [0, 0]

    for index in range(len(nums)):
        result[0] = index

        remainder = target - nums[index]

        for index_2 in range(index + 1, len(nums)):
            if nums[index_2] == remainder:
                result[1] = index_2

                return result
            
#Neste momento complexidade é O(n²) porque faço duas passagens pela lista em cade iteração
#Como resolver?

#3ª Solução
#Accepted, muito melhor do que a segunda em termos de memória
#Runtime bate 40.29%
#Memory bate 88.26%
def two_sum_3(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    for index in range(len(nums)):
        
        current_number = nums[index]

        remainder = target - current_number

        try:
            index_2 = nums.index(remainder)
            ###Complexidade list.index(element) é O(n)...

            if index != index_2:
                return [index, index_2]
        except ValueError:
            continue

#O problema é a procura linear, por isso vamos usar um dicionário.
#4ª Solução, melhor em runtime, mas a memória é horrível
#Runtime bate 54.79%
#Memory bate 25.37%
def two_sum_4(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    dict_nums = {nums[index]:index for index in range(len(nums))}

    for index in range(len(nums)):
        current_num = nums[index]

        remainder = target - current_num

        possible_index_2 = dict_nums.get(remainder)
        if possible_index_2 and possible_index_2 != index:
            return [index, possible_index_2]
        
#Runtime bate 57.21%
#Memory bate 59.38%
def two_sum_5(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    nums_indexes = {}

    for index in range(len(nums)):

        current_num = nums[index]

        remainder = target - current_num

        if nums_indexes.get(remainder) is not None: #Cuidado aqui, não posso fazer só o get, pq pode-me retornar um índice 0, e o Python avalia-o como falso e não entra no if
            return [nums_indexes.get(remainder), index]
        else:
            nums_indexes[current_num] = index

    return [0, 0]

#6ª Solução, melhor em runtime, mas a memória é horrível
#Runtime bate 100%
#Memory bate 23.34%
def two_sum_6(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for index in range(1,len(nums)):
        for second_index in range(1, len(nums)):
            if nums[second_index] + nums[second_index - index] == target:
                return [second_index, second_index-index]
    
    return [0,0]



#Complexidade da quinta solução
#Primeiro Loop corre aproximadamente n vezes (de 0 a n - 1). Complexidade O(n)
#Para memória, O(n), porque o dicionário pode crescer até n elementos no pior cenário.


#Complexidade da sexta solução
#Primeiro Loop corre aproximadamente n vezes (de 1 a n - 1). Complexidade O(n)
#Segundo Loop a mesma coisa (de index a n - 1). Complexidade O(n)
#Nested loops. O(n**n)
#Para a memória, não estou a guardar nada em memória, exceto index e second index. O(1).



            

            






