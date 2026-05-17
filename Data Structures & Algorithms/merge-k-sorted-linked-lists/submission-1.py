# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #this methods is O(nlogk) time and O(1) space, not sure why the recommended complexity is O(n*k) because that makes the problem too easy
        
        if not lists:
            return None

        while len(lists) > 1:
            mergedLists = []

            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i + 1] if (i+1) < len(lists) else None
                mergedLists.append(self.mergeTwoLists(list1, list2))
            lists = mergedLists

        return lists[0]

        

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

        