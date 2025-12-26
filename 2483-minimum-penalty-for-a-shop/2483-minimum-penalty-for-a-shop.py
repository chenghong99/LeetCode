class Solution(object):
    def bestClosingTime(self, customers):
        """
        :type customers: str
        :rtype: int
        """

        curr = 0
        for c in customers:
            if c == "Y":
                curr += 1
        
        curr_min = curr
        idx = 0
        for i in range(1, len(customers) + 1):
            if customers[i - 1] == "Y":
                curr -= 1
            else:
                curr += 1
            if curr < curr_min:
                idx = i
                curr_min = curr
        return idx