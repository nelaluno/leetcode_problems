# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.resp_count = 0
        
        def collect_pathes(node, path_sums):
            new_path_sum = path_sums[-1] + node.val

            for path_sum in path_sums:
                if new_path_sum - path_sum == targetSum:
                    self.resp_count += 1

            if not node.left and not node.right:
                return
            
            path_sums.append(new_path_sum)
            if node.left:
                collect_pathes(node.left, path_sums[:])
            if node.right:
                collect_pathes(node.right, path_sums[:])

        if root:
            collect_pathes(root, [0])
        return self.resp_count
