class Solution:
    def isPalindrome(self, s: str) -> bool:

        cleaned_text = s.replace(",", "").replace("!", "").replace(" ", "").replace(":", "").replace(".", "").replace("'", "").replace("{", "").replace("}", "").replace("[", "").replace("]", "").replace("-", "").replace(" \ ", "").replace("\"", "").lower()
        print(cleaned_text)
        left = 0
        right = len(cleaned_text) - 1
        while left < right:
            if not cleaned_text[left].isalnum():
                left+=1
            if not cleaned_text[right].isalnum():
                right-=1

            elif(cleaned_text[right] == cleaned_text[left]):
                left+=1
                right-=1
            
            else:
                return False
            
        return True
            
        