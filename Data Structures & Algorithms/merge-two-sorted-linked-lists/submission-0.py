# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        

        
        dummyNode = ListNode()
        curr = dummyNode
       
        while list1 and list2:
            #places which ever val is smaller inside the result list as its sorted asc and iterates onto the next node in the appropriate list
            if list1.val > list2.val: 
                curr.next = list2
                list2 = list2.next

            else:
                curr.next = list1
                list1 = list1.next
    
            curr = curr.next #iterate onto the next position in the result list

        #once the loop has ended check which list still has nodes to be added and then add the rest of the nodes on
        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2

        return dummyNode.next #have to do dummyNode.next as dummyNode has its own value as 0

                
  
        

            


