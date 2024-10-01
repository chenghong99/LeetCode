class Solution:
    def candy(self, ratings: List[int]) -> int:
        right = [1 for i in range(len(ratings))]
        left = [1 for i in range(len(ratings))]
        
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                right[i] = right[i - 1] + 1
                
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                left[i] = left[i + 1] + 1
                
        candies = 0
        for i in range(len(ratings)):
            candies += max(right[i], left[i])
            
        return candies 
            