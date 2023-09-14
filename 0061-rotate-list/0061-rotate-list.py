# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        curr_LL = []
        new_LL = []
        curr = head
        while curr != None:
            curr_LL.append(curr)
            curr = curr.next

        if len(curr_LL) == 0:
            return head

        k = k % len(curr_LL)

        for i in range(k):
            node = curr_LL.pop(-1)
            curr_LL[-1].next = None
            node.next = curr_LL[0]
            curr_LL.insert(0, node)

        return curr_LL[0]