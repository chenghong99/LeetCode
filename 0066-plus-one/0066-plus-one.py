class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        ## iterate from the back, keep adding 1 until the sum does not lead to a 10. 

        curr = len(digits) - 1
        while curr >= 0:
            if (digits[curr] + 1) % 10 == 0:
                digits[curr] = 0
                curr -= 1
            else:
                digits[curr] += 1
                break 
        if digits[curr] == 0:
            digits.insert(0, 1)
        return digits
