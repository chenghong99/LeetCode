# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        temp = head
        all_node = []
        
        while temp != None:
            all_node.append(temp)
            temp = temp.next 
        
        if len(all_node) == 1:
            return None
        
        else:
            to_remove = all_node[len(all_node) - n]
            if to_remove == head:
                head = to_remove.next
            else:
                before_to_remove = all_node[len(all_node) - n - 1]
                before_to_remove.next = to_remove.next
            return head
            