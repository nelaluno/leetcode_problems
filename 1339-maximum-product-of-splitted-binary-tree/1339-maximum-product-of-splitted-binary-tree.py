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
        left_only = node.left and not node.right
        right_only = not node.left and node.right

        if is_partial:#left_only or right_only:
            self.partials.add(partial_sum)

        # if it's leaf it can be partial subtree
        if not node.left and not node.right:
            self.partials.add(node.val)

        if node.left:
            tree_sum += self.get_tree_sum(node.left, partial_sum, is_partial=is_partial and left_only)

        if node.right:
            tree_sum += self.get_tree_sum(node.right, partial_sum, is_partial=is_partial and right_only)

        self.partials.add(tree_sum)
        # print(node.val, self.partials)
        return tree_sum

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.partials = set()
        tree_sum = self.get_tree_sum(root, is_partial=root.left and not root.right or not root.left and root.right)
        # print(self.partials)
        # print(tree_sum)
        
        max_product = 0
        for partial in self.partials:
            # print(partial, (tree_sum - partial))
            product = (partial * (tree_sum - partial))
            max_product = max(max_product, product)
            # print(product)
        return max_product % MOD