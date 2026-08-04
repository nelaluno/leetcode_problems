# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
                
        even_head = head.next
        even_tail = head.next
        odd_tail = head
        while even_tail and even_tail.next:
            new_odd_tail = even_tail.next
            odd_tail.next = new_odd_tail
            if new_odd_tail:
                new_odd_tail.next, even_tail.next = even_head, new_odd_tail.next
            
            even_tail = even_tail.next
            odd_tail = new_odd_tail
            
        return head
        
            
