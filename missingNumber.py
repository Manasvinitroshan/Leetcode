class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)
        hashmap = set(nums)
        
        for i in range(n):
            if i in hashmap:
                continue
            
            if i not in hashmap:
                return i 
            
        
        return n
        
        
        