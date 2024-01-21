class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashset = set()
        hashmap = {}
        
        for i in arr:
            hashmap[i] = hashmap.get(i, 0) + 1
            
        for k, v in hashmap.items():
            if v not in hashset:
                hashset.add(v)
                
            else:
                return False
            
        return True
        