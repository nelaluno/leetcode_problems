# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def max_depth(node):
    left_count, right_count = 0, 0
    if node.left:
        left_count = max_depth(node.left)
    if node.right:
        right_count = max_depth(node.right)

    return 1 + max(left_count, right_count)


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        return max_depth(root)