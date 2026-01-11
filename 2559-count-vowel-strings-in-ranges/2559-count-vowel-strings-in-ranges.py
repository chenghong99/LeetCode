class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        ## pre count all the word in words and store in hashmap with key as index and value as valid number before 
        hashmap = {-1:0} ## initialise start to be 0
        curr_counter = 0

        for pos, word in enumerate(words):
            if word[0] in ['a','e','i','o','u'] and word[-1] in ['a','e','i','o','u']:
                curr_counter += 1
            hashmap[pos] = curr_counter 

        output = []
        for l, r in queries:
            output.append(hashmap[r] - hashmap[l - 1])
        return output

