class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ## for constant space solution, can use cycle detection algorithm. treat the problem as a linked list. 
        ## [1,3,4,2,2] the linked list version will look like 0 -> 1 -> 3 -> 2 -> 4 -> 2 -> 4 -> 2 -> 4 the cycle can be seen at the latter portion.
        ## we can apply cycle detection fast & slow pointer algo to resolve this problem 

        fast = 0
        slow = 0
        head = 0 

        while True: ## it is guaranteed to hv a cycle 
            fast = nums[nums[fast]]
            slow = nums[slow]
            if slow == fast:
                break 

        while head != slow:
            head = nums[head]
            slow = nums[slow]

        return head

        