# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def add_node(self, value, depth):
        curr_node = TreeNode(value)            
        if depth != 0:
            if self.curr_depth_nodes[depth-1].left:
                self.curr_depth_nodes[depth-1].right = curr_node
            else:
                self.curr_depth_nodes[depth-1].left = curr_node
            
        self.curr_depth_nodes[depth] = curr_node

    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        self.curr_depth_nodes = {}
        depth = 0
        num_processing = True
        value = 0
        for ind, char in enumerate(traversal):
          
            if char != "-":
                value = value*10 + int(char)
                num_processing = True
                if ind == len(traversal) -1:
                    self.add_node(value, depth) 
                continue

            if not num_processing:
                depth += 1
                continue

            self.add_node(value, depth)  
            depth = 1
            num_processing = False
            value = 0
                
        return self.curr_depth_nodes[0]