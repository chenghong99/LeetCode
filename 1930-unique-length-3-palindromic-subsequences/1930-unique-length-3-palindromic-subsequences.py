class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        hashset = set() ## to add all palindrone seq 
        all_occur = {} ## count all letters in seq

        for char in s:
            all_occur[char] = all_occur.get(char, 0) + 1 ## populate dic if num occurence 

        curr_iter = {}
        for char in s:
            curr_iter[char] = curr_iter.get(char, 0) + 1
            for key, value in curr_iter.items():
                if key == char:
                    value += 1
                if all_occur.get(key) - value > 0:
                    string = key + char + key
                    hashset.add(string)
                    
        return len(hashset)
            