# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def collect_leafs(node):
    if node.left is None and node.right is None:
        yield node.val
        
    if node.left:
        yield from collect_leafs(node.left)
        
    if node.right:
        yield from collect_leafs(node.right)
    


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leafs1 = collect_leafs(root1)
        leafs2 = collect_leafs(root2)
        
        while True:
            leaf1 = next(leafs1, None)
            leaf2 = next(leafs2, None)

            if leaf1 is None and leaf2 is None:
                return True
            
            if leaf1 != leaf2:
                return False
