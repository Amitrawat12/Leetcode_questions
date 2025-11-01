# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        if not head or not head.next or k ==0:
            return head

        curr = head
        while(curr):
            curr=curr.next
            length+=1
        k = k%length
        s = head
        f = head

        for i in range(k):
            f=f.next
        while(f.next):
            f=f.next
            s=s.next
        
        f.next = head
        newhead = s.next
        s.next = None

        return newhead