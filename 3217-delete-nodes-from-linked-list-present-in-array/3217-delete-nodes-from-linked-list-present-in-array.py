# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        ## convert list to set to search values 
        
        hashset = set(nums)
        perm_head = ListNode()
        perm_head.next = head
        prev = perm_head

        while head:
            if head.val in hashset:
                head = head.next 
                prev.next = head
            else:
                head = head.next
                prev = prev.next 

        return perm_head.next
             
        