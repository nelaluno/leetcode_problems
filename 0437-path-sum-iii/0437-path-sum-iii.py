# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.resp_count = 0
        self.prefix = defaultdict(int)
        self.prefix[0] = 1
        
        def collect_pathes(node, curr_sum):
            curr_sum += node.val
            self.resp_count += self.prefix.get(curr_sum - targetSum, 0)
            
            if not node.left and not node.right:
                return

            self.prefix[curr_sum] += 1
            
            if node.left:
                collect_pathes(node.left, curr_sum)
            if node.right:
                collect_pathes(node.right, curr_sum)

            self.prefix[curr_sum] -= 1

        if root:
            collect_pathes(root, 0)
        return self.resp_count
