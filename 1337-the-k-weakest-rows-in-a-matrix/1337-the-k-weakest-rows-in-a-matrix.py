class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        numbers = {}
        
        for i in range(len(mat)):
            numbers[i] = mat[i].count(1)
        
        numbers = dict(sorted(numbers.items(), key=lambda item: item[1]))             
        
        return list(numbers.keys())[:k]