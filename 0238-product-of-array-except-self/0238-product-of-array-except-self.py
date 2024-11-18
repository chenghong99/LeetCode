class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ## traverse 2 ways from front and back -> first way from front and populate the array -> second way from back and populate the back.
        
        output = [1 for i in range(len(nums))] ## O(n) space for output 
        cumulative_multiply = 1
        
        for i in range(1, len(nums)):
            cumulative_multiply *= nums[i - 1]
            output[i] = cumulative_multiply
        
        cumulative_multiply = 1
        for i in range(len(nums) - 2, -1, -1):
            cumulative_multiply *= nums[i + 1]
            output[i] *= cumulative_multiply
            
        return output
        
        