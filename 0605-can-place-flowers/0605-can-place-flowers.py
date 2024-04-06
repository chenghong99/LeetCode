class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        
        for i in range(len(flowerbed)):
            
            if len(flowerbed) == 1:
                if flowerbed[i] == 0:
                    count += 1
            
            elif i == 0 and len(flowerbed) > 1:
                if flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                    count += 1
                    flowerbed[i] = 1
                                        
            elif i == len(flowerbed) - 1 and len(flowerbed) > 1:
                if flowerbed[i] == 0 and flowerbed[i - 1] == 0:
                    count += 1
                    flowerbed[i] = 1
                    
            else:
                if flowerbed[i + 1] == 0 and flowerbed[i - 1] == 0 and flowerbed[i] == 0:
                    count += 1
                    flowerbed[i] = 1
            
            
        return count >= n
        