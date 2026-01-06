# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_lvl = 1
        max_lvl_sum = root.val
        cur_lvl = 1
        
        level = [root]
        while True:
            new_level = []
            cur_sum = 0
            
            for node in level:
                cur_sum += node.val
                if node.left:
                    new_level.append(node.left)
                if node.right:
                    new_level.append(node.right)

            if cur_sum > max_lvl_sum:
                max_lvl_sum = cur_sum
                max_lvl = cur_lvl

            if not new_level:
                break
            
            level = new_level
            cur_lvl += 1

        return max_lvl