# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        new_head = head
        new_tail = head
        move = new_tail.next
        while move is not None:
            move.next, new_tail.next = new_head, move.next
            new_head = move
            move = new_tail.next

        return new_head