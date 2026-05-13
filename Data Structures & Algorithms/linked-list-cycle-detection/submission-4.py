# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #floyds tortoise and hare approach O(n) time O(1) space
        
        slow = head
        fast = head

        if head == None:
            return False

        while fast and fast.next:
            
            slow = slow.next #increment the slow 'tortoise' by 1
            fast = fast.next.next #increment the fast 'hare' by 2

            #if a cycle exisits they will have to eventually reach each other again in the same postion
            if slow == fast:
                return True
        return False
        