class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        ## extract out the diagonal 
        ## for each num in diagonals check 
        ## for each num iterate 
        diag = []
        for i in range(len(nums)):
            diag.append(nums[i][i])
            diag.append(nums[i][len(nums) - 1 - i])
        diag.sort()
        for elem in diag[::-1]:
            is_prime = True
            for i in range(2, elem):
                if elem % i == 0:
                    is_prime = False
                    break
            if is_prime == True and elem != 1:
                return elem
        return 0
        
            
            