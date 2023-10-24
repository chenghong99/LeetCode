class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        num1_set = set(nums1)
        num2_set = set(nums2)
        ls = [[], []]
        
        for i in num1_set:
            if i not in num2_set:
                ls[0].append(i)
                
        for i in num2_set:
            if i not in num1_set:
                ls[1].append(i)
            
        return ls
        
        