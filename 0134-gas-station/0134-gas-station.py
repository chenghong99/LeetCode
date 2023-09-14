class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """

        if sum(gas) < sum(cost):
            return -1

        else:
            total = 0
            index = 0
            for i in range(len(gas)):
                total += (gas[i] - cost[i])
                if total < 0:
                    total = 0
                    index = i + 1
            return index
