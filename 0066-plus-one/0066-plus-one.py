class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        counter = 0
        pos = len(digits) - 1
        
        while digits[pos] == 9:
            digits[pos] = 0
            counter += 1
            pos -= 1
            
        if counter == len(digits):
            digits.insert(0, 1)
            
        else:
            digits[pos] += 1
        return digits
            
        