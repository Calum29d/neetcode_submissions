# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, start, end): # reverse section of the list
        prev, cur = None, start

        while cur != end:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #find the current group
        count, cur = 0, head
        while cur and count < k:
            cur = cur.next
            count += 1
    
        if count < k:
            return head
        
        newHead = self.reverse(head, cur)# reverse the list up to cur
        head.next = self.reverseKGroup(cur, k)
        return newHead

    #O(n) time O(n/k) space


    
    

        
        