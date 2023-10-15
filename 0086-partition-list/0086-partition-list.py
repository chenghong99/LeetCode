# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        smaller_x = ListNode()
        larger_x = ListNode()

        before_x = smaller_x
        after_x = larger_x

        while head != None:
            if head.val < x:
                before_x.next = head
                head = head.next
                before_x = before_x.next
                before_x.next = None

            else:
                after_x.next = head
                head = head.next 
                after_x = after_x.next
                after_x.next = None

        before_x.next = larger_x.next
        return smaller_x.next

        