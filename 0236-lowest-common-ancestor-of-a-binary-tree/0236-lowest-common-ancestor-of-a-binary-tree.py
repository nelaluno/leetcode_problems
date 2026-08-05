# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # self.found = {"p": False, "q": False}
        
        def search(node, score_remain=2):
            node_score = 0
            if node.val in {p.val, q.val}:
                node_score = 1
                if score_remain == node_score:
                    return 2, None

            left_score, right_score = 0, 0
            if node.left:
                left_score, left_resp = search(node.left, score_remain)
                if left_resp:
                    return 2, left_resp
                else: 
                    node_score += left_score
                    if node_score == score_remain:
                        return 2, node

            if node.right:
                right_score, right_resp = search(node.right, score_remain)
                if right_resp:
                    return 2, right_resp
                else: 
                    node_score += right_score
                    if node_score == score_remain:
                        return 2, node

            return node_score, None

        return search(root, 2)[1]
        
            
