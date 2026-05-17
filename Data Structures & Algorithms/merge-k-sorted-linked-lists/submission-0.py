# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if len(lists) < 2:
            return None

        for i in range(1,len(lists)):
            lists[i] = self.mergeTwoLists(lists[i], lists[i-1])

        return lists[i]

        

    def mergeTwoLists(self, list1, list2):

        dummyNode = ListNode()
        curr = dummyNode

        while list1 and list2:

            if list1.val > list2.val:
                curr.next = list2
                list2 = list2.next
            else:
                curr.next = list1
                list1 = list1.next
            
            curr = curr.next
            
        if list1:
            curr.next = list1
        else:
            curr.next = list2
        
        return dummyNode.next

        