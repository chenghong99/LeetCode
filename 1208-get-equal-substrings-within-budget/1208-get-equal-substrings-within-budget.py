class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        ## sliding window qn, if curr_cost < maxCost then keep adding element,if exceeds then remove from head 

        head = 0
        max_len = 0
        cum_cost = 0

        for tail in range(len(s)):
            curr_cost = abs(ord(s[tail]) - ord(t[tail]))
            while curr_cost + cum_cost > maxCost:
                    cum_cost -= abs(ord(s[head]) - ord(t[head]))
                    head += 1
            cum_cost += curr_cost
            max_len = max(max_len, tail - head + 1)
        return max_len

                

