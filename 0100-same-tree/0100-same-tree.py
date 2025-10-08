# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """

        ## base case if both are none then return true, else if one of them is none and the other is not then return false
        ## recursive call, isSameTree left of p vs left of q and isSameTree right of p and right of q.

        if p == None and q == None:
            return True

        elif p == None or q == None:
            return False

        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False