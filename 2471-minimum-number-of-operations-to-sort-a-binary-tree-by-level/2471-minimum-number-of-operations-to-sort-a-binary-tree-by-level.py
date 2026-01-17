# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.append(root)
        swaps = 0

        while queue:
            curr_nodes = len(queue)
            level_node = []

            for i in range(curr_nodes):
                temp = queue.popleft()
                level_node.append(temp.val)

                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
            sorted_level_node = sorted(level_node)
            pos_dic = {}

            for i, x in enumerate(level_node):
                pos_dic[x] = i

            for i in range(len(level_node)):
                if level_node[i] != sorted_level_node[i]:
                    temp = level_node[i]
                    temp_pos = pos_dic[sorted_level_node[i]]
                    level_node[i], level_node[pos_dic[sorted_level_node[i]]] = level_node[pos_dic[sorted_level_node[i]]], level_node[i]
                    pos_dic[temp] = temp_pos
                    swaps += 1                

        return swaps

        