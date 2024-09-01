class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_pos = 0
        word2_pos = 0
        final = ''
        
        while word1_pos < len(word1) and word2_pos < len(word2):
            final += word1[word1_pos] + word2[word2_pos]
            word1_pos += 1
            word2_pos += 1
            
        final += word1[word1_pos:] + word2[word2_pos:]
        
        return final 
        