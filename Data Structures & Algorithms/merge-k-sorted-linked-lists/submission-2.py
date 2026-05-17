# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq 

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #this is the minHeap solution, never used them before but O(nlogK) space is O(k) as we create a heap with up to k elements 

        heap = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummyNode = ListNode()
        curr = dummyNode

        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = node
            node = node.next
            if node:
                heapq.heappush(heap,(node.val, i, node))
            
        return dummyNode.next


        