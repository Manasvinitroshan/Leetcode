class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        text = s.strip().split()
        
        return len(text[-1])