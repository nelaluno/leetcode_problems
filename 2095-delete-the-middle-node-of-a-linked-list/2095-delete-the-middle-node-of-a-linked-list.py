# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        node = head
        while node.next is not None:
            count += 1
            node = node.next

        if count == 0:
            return None

        if count % 2:
            middle = count // 2
        else:
            middle = count // 2 - 1

        i = 0
        node = head
        while i != middle:
            i += 1
            node = node.next

        node.next = node.next.next
        return head
        