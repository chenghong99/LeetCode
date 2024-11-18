class Solution:
    def candy(self, ratings: List[int]) -> int:
        ## create an array whr all kids get 1 -> iterate front and back -> for each iteartion we compare the ratings to update the num of candies 
        
        arr_left = [1 for i in range(len(ratings))]
        arr_right = [1 for i in range(len(ratings))]
        
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                arr_right[i] = arr_right[i-1] + 1
                
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                arr_left[i] = arr_left[i+1] + 1
        
        candies = 0
        for i in range(len(arr_left)):
            candies += max(arr_left[i], arr_right[i])
            
        return candies