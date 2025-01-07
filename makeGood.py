class Solution:
    def makeGood(self, s: str) -> str:
        i = 0
        while i < len(s) - 1:
            if abs(ord(s[i]) - ord(s[i + 1])) == 32:  # Corrected condition for case difference
                s = s[:i] + s[i + 2:]  # Remove both characters at i and i+1
                i = max(i - 1, 0)  # Step back to check previous characters
            else:
                i += 1
        print(s)
        return s