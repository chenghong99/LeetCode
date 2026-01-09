# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ## smallest will always be 1 layer above the deepest node. 
        # find deepest node and return the head. 
        ## for all the deepest node traverse up until we find a commn head 
        ## store depth, head of each node. for eash traversal 

        hashmap = {}
        parent_map = {}
        queue = deque()
        queue.append([root, 1])
        hashmap[1] = [[root, None]]
        parent_map[root] = None

        while queue:
            temp = queue.popleft()
            if temp[0].right:
                parent_map[temp[0].right] = temp[0]
                key = temp[1] + 1
                if key not in hashmap:
                    hashmap[key] = []
                hashmap[key].append([temp[0].right, temp[0]])
                queue.append([temp[0].right, temp[1] + 1])
            if temp[0].left:
                parent_map[temp[0].left] = temp[0]
                key = temp[1] + 1
                if key not in hashmap:
                    hashmap[key] = []
                hashmap[key].append([temp[0].left, temp[0]])
                queue.append([temp[0].left, temp[1] + 1])
        head_set = set()
        for node, node_head in hashmap.get(max(hashmap.keys())):
            head_set.add(node)

        while len(head_set) != 1:
            head_set = {parent_map[node] for node in head_set}

        return head_set.pop()
            