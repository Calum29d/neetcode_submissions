# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummyNode = ListNode(0,head)
        left = dummyNode #dummy node is used so the left pointer reaches the node before the one to be removed
        right = head

        #puts the right pointer into the nth position in the list
        for i in range(n):
            right = right.next
        
        #when the right pointer reaches the end of the list the left pointer will be at the node before the one to be removed
        while right:
            left = left.next
            right = right.next

        left.next = left.next.next

        return dummyNode.next
        
        

        