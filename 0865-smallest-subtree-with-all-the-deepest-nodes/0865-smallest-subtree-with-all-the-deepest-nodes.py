# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def get_max_depth(node, depth=0):
#     if not node.left and not node.right:
#         return depth

#     max_depth = depth
#     if node.left:
#         max_depth = get_max_depth(node.left, depth+1)
#     if node.right:
#         max_depth = max(max_depth, get_max_depth(node.right, depth+1))
#     return max_depth
    
def solve(node, depth=0):    
    if not node.left and not node.right:
        return depth, node
    
    if node.left:
        left_max, left_child = solve(node.left, depth + 1)
    if node.right:
        right_max, right_child = solve(node.right, depth + 1)
    if node.left and node.right:
        if left_max == right_max:
            return left_max, node
        elif left_max > right_max:
            return left_max, left_child
        else:
            return right_max, right_child
    
    if node.left:
        return left_max, left_child
    return right_max, right_child


class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        max_depth, node = solve(root)
        return node