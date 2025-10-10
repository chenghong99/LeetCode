# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        ## every traversal, left most node check with right most node. 
        def is_mirror(root1, root2):
            if root1 == None and root2 == None:
                return True 
            elif root1 == None or root2 == None:
                return False 
            if root1.val == root2.val:
                return is_mirror(root1.left, root2.right) and is_mirror(root1.right, root2.left)
            else:
                return False
        return is_mirror(root.left, root.right)

