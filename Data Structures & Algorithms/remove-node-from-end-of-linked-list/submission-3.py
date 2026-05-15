# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #if i reverse the list then increment up to the nth node then just change the pointer then reverse the list again
        #i think that should work

        #This solution was actually quite easy to think of, 
        #I think this is O(2n) time which is just O(n) time and O(1) space

        if head.next == None and n == 1:
            return None

        reversedList = self.reverseList(head)
        curr = reversedList
        prev = None
        count = 1

        #traverse through list up to the node before the one to remove
        while count != n:
            prev = curr
            curr = curr.next
            count += 1
        
        if prev == None:
            reversedList = curr.next
        else:
            prev.next = curr.next

        return self.reverseList(reversedList)
            
    #function to reverse the list       
    def reverseList(self, head):
            curr = head
            prev = None

            while curr:
                nextNode = curr.next
                curr.next = prev
                prev = curr
                curr = nextNode
            
            return prev



        