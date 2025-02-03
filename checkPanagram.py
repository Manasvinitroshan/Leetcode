class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        hashmap = set()
        counter = 0
        
        for c in sentence:
            if c in hashmap:
                continue
            else:
                hashmap.add(c)
                counter+=1
        
        return (counter == 26)