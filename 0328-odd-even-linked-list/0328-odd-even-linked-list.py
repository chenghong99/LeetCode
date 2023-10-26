# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = odd_head = ListNode()
        even = even_head = ListNode()
        odd_num = True
        
        while head != None:
            if odd_num:
                odd.next = head
                odd = odd.next
                head = head.next
                odd.next = None
                odd_num = False
            else:
                even.next = head
                even = even.next
                head = head.next
                even.next = None
                odd_num = True
                            
        odd.next = even_head.next
        
        return odd_head.next
            
        