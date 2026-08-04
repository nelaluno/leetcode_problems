# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return 
        
        end_node = head
        middle_node = head
        prev = head
        while end_node and end_node.next:
            prev = middle_node
            middle_node = prev.next
            end_node = end_node.next.next

        prev.next = middle_node.next
        return head
        
