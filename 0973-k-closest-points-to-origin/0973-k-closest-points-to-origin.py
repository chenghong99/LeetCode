class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        
        new_arr = []
        
        for i in points:
            val = i[0]**2 + i[1]**2
            new_arr.append((val, i))
            
        new_arr.sort()
        final = []
        
        for a, b in new_arr[:k]:
            final.append(b)
            
        return final
            
        
        
        
        
## we select the sum of the squared values 
## we sort by the indiv array. 
        