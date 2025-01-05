class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if(s == t):
            return True

          while(i < len(s) and j < len(t)):
            if(s[i] == t[j]):
                