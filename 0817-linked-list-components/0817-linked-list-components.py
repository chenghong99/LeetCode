# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def numComponents(self, head, nums):
        """
        :type head: Optional[ListNode]
        :type nums: List[int]
        :rtype: int
        """
        ## hash nums into a hashset, iterate the linkedlist, if the next node is in the hashset they are connected. 
        hashset = set(nums)
        output = 0
        connected_flag = False

        while head:
            if head.val in hashset:
                connected_flag = True

            elif connected_flag == True:
                connected_flag = False
                output += 1
            head = head.next
        if connected_flag == True:
            output += 1
        return output

        