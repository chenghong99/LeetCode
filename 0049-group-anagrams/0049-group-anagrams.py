class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        hashmap = {}
        final = []
        
        for word in strs:
            new_word = tuple(sorted(word))
            if hashmap.get(new_word) == None:
                hashmap[new_word] = [word]
                
            else:
                hashmap.get(new_word).append(word)
                
        for k, v in hashmap.items():
            final.append(v)
            
        return final 
            
            
        
        
## iterate and sort 
## data structure use hashmap 
# key wil be sorted word and map is a list of the angrmas.
## iterate and combine in the end 

