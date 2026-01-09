# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict
def get_max_depth(node, depth=0):
    if not node.left and not node.right:
        return depth

    max_depth = depth
    if node.left:
        max_depth = get_max_depth(node.left, depth+1)
    if node.right:
        max_depth = max(max_depth, get_max_depth(node.right, depth+1))
    return max_depth
    
def solve(node, max_depth, depth=0):
    if node is None:
        return None
    
    if depth == max_depth:
        return node

    left_child = solve(node.left, max_depth, depth + 1)
    right_child = solve(node.right, max_depth, depth + 1)
    if left_child and right_child:
        return node
    return left_child or right_child


class Solution:
    def get_max_depth(self, node, depth=0):
        if not node.left and not node.right:
            return depth

        max_depth = depth
        if node.left:
            max_depth = self.get_max_depth(node.left, depth+1)
        if node.right:
            max_depth = max(max_depth, self.get_max_depth(node.left, depth+1))
        return max_depth

    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        max_depth = get_max_depth(root, depth=0)
        if max_depth == 0:
            return root

        return solve(root, max_depth)