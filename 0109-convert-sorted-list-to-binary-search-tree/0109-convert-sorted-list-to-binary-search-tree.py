# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def list_to_BST(nums):
    n = len(nums)
    if n == 1:
        return TreeNode(nums[0])
    
    mid = n // 2 if n % 2 else n // 2 - 1
    node = TreeNode(nums[mid])
    if mid > 0:
        node.left = list_to_BST(nums[:mid])
    if mid+1 < n:
        node.right = list_to_BST(nums[mid+1:])
    return node


class Solution:
    def head_to_list(self, node):
        self.nums.append(node.val)
        if node.next:
            self.head_to_list(node.next)
    
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return head
        
        self.nums = []
        self.head_to_list(head)
        return list_to_BST(self.nums)