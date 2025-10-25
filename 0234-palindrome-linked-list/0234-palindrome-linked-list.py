# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #finding middle
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        #reverse the next half
        prev = None
        while slow:
            temp= slow.next
            slow.next=prev
            prev = slow
            slow = temp
      
        #match firs and second halfs
        node1 = head
        node2 = prev

        while node2:
            if node1.val != node2.val:
                return False
            node1=node1.next
            node2=node2.next
        return True
