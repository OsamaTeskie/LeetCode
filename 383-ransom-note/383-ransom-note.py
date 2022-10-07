class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        
        dicts = {}
        
        for letter in ransomNote:
            if letter in dicts:
                dicts[letter] += 1
            else:
                dicts[letter] = 1
                
        
        for letter in dicts:
            if dicts[letter] > magazine.count(letter):
                return False
            
        return True
    
    
    # x  =  set(ransomNote)
    #     x  =  list(x)
    #     for i in x :
    #         if magazine.count(i)  <  ransomNote.count(i):
    #             return False
    #     return True