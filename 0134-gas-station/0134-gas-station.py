class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """

        if sum(gas) < sum(cost):
            return -1 ## if sum(gas) more, there will def be a way

        curr_gas = 0
        ans = 0

        for pos, vol in enumerate(gas):
            curr_gas += vol
            if curr_gas < cost[pos]:
                curr_gas = 0
                ans = pos + 1
            else:
                curr_gas -= cost[pos]

        return ans