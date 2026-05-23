class Solution:
    
    def get_squared_sum(self, list_nums):
        sum = 0
        for number in list_nums:
            sum += number ** 2
        return sum

    def get_digits(self, number):
        digits = []

        while number > 0:
            digits.append(number % 10)
            number = number // 10
        
        return digits

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen_result = set()
        digits = self.get_digits(n)
        current_sum = self.get_squared_sum(digits)

        print("Initial digits", digits)
        print("Current sum", current_sum)

        while current_sum != 1:
            digits = self.get_digits(current_sum)
            current_sum = self.get_squared_sum(digits)

            print(" Digits after recalculating", digits)
            print("Current sum after recalculating", current_sum)
            
            if current_sum in seen_result:
                return False
            
            seen_result.add(current_sum)
        
        return True



#Improvements would be condensing the two helper functions into one, without needing the extra list
#Linked list? Another approach, but I haven't worked much with that DS.

class Solution_2:
    
    def get_squared_sum(self, number):
        sum = 0

        while number > 0:
            sum += (number % 10) ** 2
            number = number // 10
        
        return sum

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen_result = set()
        current_sum = self.get_squared_sum(n)

        while current_sum != 1:
            current_sum = self.get_squared_sum(current_sum)

            if current_sum in seen_result:
                return False
            
            seen_result.add(current_sum)
        
        return True

sol = Solution_2()

print(sol.isHappy(7))