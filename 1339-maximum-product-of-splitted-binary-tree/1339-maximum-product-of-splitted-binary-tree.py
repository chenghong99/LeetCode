# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        arr = []
        def fn(node):
            if node == None:
                return 0
            ans = node.val + fn(node.left) + fn(node.right)
            arr.append(ans)
            return ans 

        ans = fn(root)
        div = 10**9 + 7
        max_product = 0
        for i in arr:
            max_product = max(max_product, (ans-i)*i)
        return max_product % div
        