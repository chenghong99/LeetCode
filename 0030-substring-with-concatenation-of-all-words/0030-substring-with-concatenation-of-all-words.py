class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        len_of_words = len(words[0])
        len_of_total_words = len_of_words * len(words)
        output = []
        words_map = dict()
         
        s_map = dict()
        
        for word in words:
            words_map[word] = words_map.get(word, 0) + 1

        words_map_copy = words_map.copy()
        hashset = set()

        for char in range(len(s) - len_of_total_words + 1):
            output.append(char)
            for j in range(char, char + len_of_total_words , len_of_words):
                store = words_map_copy.get(s[j:j+len_of_words])
                if (store != None) and (s[j:j+len_of_words] not in hashset):
                    s_map[s[j:j+len_of_words]] = x = s_map.get(s[j:j+len_of_words], 0) + 1
                    if x == store:
                        hashset.add(s[j:j+len_of_words])
                else:
                    s_map = dict()
                    output.pop(-1)
                    hashset = set()
                    break
            s_map = dict()
            hashset = set()
        return output
            
                
                    