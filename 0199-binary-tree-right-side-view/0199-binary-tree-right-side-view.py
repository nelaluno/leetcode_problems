# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.depth_view = {}

        def collect_view_points(node, depth):
            if depth not in self.depth_view:
                self.depth_view[depth] = node.val

            if node.right:
                collect_view_points(node.right, depth+1)
            
            if node.left:
                collect_view_points(node.left, depth+1)

        if not root:
            return []
        collect_view_points(root, 0)
        return [self.depth_view[i] for i in range(len(self.depth_view))]

            
            
            