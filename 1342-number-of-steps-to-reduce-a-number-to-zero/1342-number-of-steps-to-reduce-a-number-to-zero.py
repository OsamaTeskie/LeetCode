class Solution:
    def numberOfSteps(self, num: int) -> int:
        
        if num == 0:
            return 0
        return self.helper(num,0)
        
    
    def helper(self, num, total):
        
        if num == 1:
            return total+1
        else:
            if num % 2 == 0:
                return self.helper(num/2, total+1)
            else:
                return self.helper(num-1, total+1)