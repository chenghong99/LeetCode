class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        ## start iterating from the first index, use an accumulating variable to count the fuel accumulated so far. if it reaches negative reset to 0 

        if sum(gas) < sum(cost):
            return -1

        accumulate, pos = 0, 0
        for i in range(len(gas)):
            accumulate += gas[i] - cost[i]
            if accumulate < 0:
                pos = i + 1
                accumulate = 0
        return pos
