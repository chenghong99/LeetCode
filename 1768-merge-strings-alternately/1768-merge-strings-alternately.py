class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word = ""
        while word1 and word2:
            word += word1[0] + word2[0]
            word1 = word1[1:]
            word2 = word2[1:]
            
        if word1 or word2:
            word += word1 + word2
            
        return word
        