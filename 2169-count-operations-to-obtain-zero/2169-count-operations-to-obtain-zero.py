class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        
        return self.helper(num1, num2, 0)
        
    def helper(self, num1, num2, total):
        
        if num1 == 0 or num2 == 0:
            return total
        else:
            if num1 >= num2:
                return self.helper(num1-num2, num2, total+1)
            return self.helper(num1, num2-num1, total+1)