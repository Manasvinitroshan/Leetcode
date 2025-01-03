class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        text = s.strip().split() # strip comes before split
        
        return len(text[-1])