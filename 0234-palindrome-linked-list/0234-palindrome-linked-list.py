# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #finding middle
        slow = fast = head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        #reverse second
        prev = None
        while slow:
            temp = slow.next
            slow.next=prev
            prev = slow
            slow = temp
        
        #checking first and second half
        firstnode = head
        secondnode = prev
        while secondnode:
            if firstnode.val != secondnode.val:
                return False
            firstnode = firstnode.next
            secondnode = secondnode.next
        return True