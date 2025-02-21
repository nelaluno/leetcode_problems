# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tree_recover(node, val=0):
    node.val = val
    if node.left:
        tree_recover(node.left, 2*val + 1)
    if node.right:
        tree_recover(node.right, 2*val + 2)

def find(node, target):
    if len(target) == 1 and target[0] == node.val:
        return True
        
    if node.left and target[-2] % 2:
        return find(node.left, target[:-1])
    elif node.right and not target[-2] % 2:
        return find(node.right, target[:-1])
    else:
        return False
    
class FindElements:
    root = None
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        tree_recover(self.root)

    def find(self, target: int) -> bool:
        target_steps = [target]
        while target:
            if target % 2:
                target -= 1
            else:
                target -= 2

            target = target // 2
            target_steps.append(target)

        return find(self.root, target_steps)


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)