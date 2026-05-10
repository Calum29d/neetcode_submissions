# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head == None:
            return None

        curr = head
        prev = None #make prev = to null because 0 is going to be the tail of the list

        while curr:
            nextNode = curr.next #store the next node
            curr.next = prev #this is the reverse line, makes the pointer point to the previous node 'flipping' the arrow
            prev = curr #store the current node to be used in next iteration
            curr = nextNode #advance to the next node
            
        return prev #prev is now the 'head' of the list


        
        




        