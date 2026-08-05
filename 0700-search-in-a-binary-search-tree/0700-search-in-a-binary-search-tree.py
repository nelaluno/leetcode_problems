# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def search(node):
            if node.val == val:
                return node
            
            if node.left:
                left_resp = search(node.left)
                if left_resp:
                    return left_resp

            if node.right:
                right_resp = search(node.right)
                if right_resp:
                    return right_resp

            return None

        if not root:
            return None

        return search(root)
