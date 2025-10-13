# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """

        dummy_node = ListNode()
        dummy_node.next = head 
        fix_node = dummy_node
        prev_node = dummy_node
        curr_pos = 0

        while True:
            if curr_pos == left-1:
                prev_node.next = None
                prev = None
                first = head
                for i in range(right - left + 1):
                    curr = head
                    head = head.next 
                    curr.next = prev
                    prev = curr
                prev_node.next = prev
                first.next = head
                break
            else:
                prev_node = prev_node.next
                head = head.next
                curr_pos += 1
        return fix_node.next

                    
