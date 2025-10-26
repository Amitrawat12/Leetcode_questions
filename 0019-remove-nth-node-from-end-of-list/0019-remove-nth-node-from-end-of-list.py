# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sentinal = ListNode(0)
        sentinal.next = head

        length=0
        current = head
        while current:
            length += 1
            current = current.next

        prev = sentinal
        for i in range(length-n):
            prev=prev.next

        prev.next=prev.next.next
        return sentinal.next
