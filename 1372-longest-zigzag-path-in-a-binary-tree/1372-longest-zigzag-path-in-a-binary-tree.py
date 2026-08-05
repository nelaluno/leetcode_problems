# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.result = 0

        def longest_zig_zag(node, turn_left=True, depth=0):
            if not node:
                return

            self.result = max(self.result, depth)
            if turn_left:
                longest_zig_zag(node.left, False, depth + 1)
                longest_zig_zag(node.right, True, 1)
            else:
                longest_zig_zag(node.right, True, depth + 1)
                longest_zig_zag(node.left, False, 1)


        longest_zig_zag(root)
        return self.result