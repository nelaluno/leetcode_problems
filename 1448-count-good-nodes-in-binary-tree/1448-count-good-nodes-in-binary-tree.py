# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def count_good_nodes(node, max_node_val=float('-inf')):
    if node is None:
        return 0

    count = 0
    if node.val >= max_node_val:
        max_node_val = node.val
        count = 1
    count += count_good_nodes(node.left, max_node_val) + count_good_nodes(node.right, max_node_val) 
    return count


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return count_good_nodes(root)