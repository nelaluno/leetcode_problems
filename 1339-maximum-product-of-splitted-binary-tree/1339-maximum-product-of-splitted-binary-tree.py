# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

MOD = 10 ** 9 + 7
class Solution:
    def get_tree_sum(self, node: Optional[TreeNode], partial_sum=0, is_partial=False) -> int:
        tree_sum = node.val
        partial_sum += node.val

        if is_partial:
            self.partials.add(partial_sum)

        # if it's leaf it can be partial subtree
        if not node.left and not node.right:
            self.partials.add(node.val)

        if node.left:
            tree_sum += self.get_tree_sum(node.left, partial_sum, is_partial=is_partial and not node.right)

        if node.right:
            tree_sum += self.get_tree_sum(node.right, partial_sum, is_partial=is_partial and not node.left)

        self.partials.add(tree_sum)
        return tree_sum

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.partials = set()
        tree_sum = self.get_tree_sum(root, is_partial=root.left and not root.right or not root.left and root.right)
        
        max_product = 0
        for partial in self.partials:
            max_product = max(max_product, (partial * (tree_sum - partial)))
        return max_product % MOD