# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# from copy import deepcopy

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.pathes = []

        def collect_pathes(node, path):
            new_path = path + [node.val]

            if not node.left and not node.right:
                if sum(new_path) == targetSum:
                    self.pathes.append(new_path)
                return
            
            if node.left:
                collect_pathes(node.left, new_path)
            if node.right:
                collect_pathes(node.right, new_path)

        if root:
            collect_pathes(root, [])
        return self.pathes
