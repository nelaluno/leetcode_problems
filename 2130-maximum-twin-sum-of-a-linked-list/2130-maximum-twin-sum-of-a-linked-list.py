# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverse(head):
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


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        mid_pointer = head
        end_pointer = head.next

        while end_pointer.next:
            mid_pointer = mid_pointer.next
            end_pointer = end_pointer.next.next

        mid_pointer.next, twin_head = None, mid_pointer.next
        twin_head = reverse(twin_head)

        max_sum = 0
        node, twin_node = head, twin_head
        while node and twin_node:
            max_sum = max(max_sum, node.val + twin_node.val)
            node = node.next
            twin_node = twin_node.next

        return max_sum
        