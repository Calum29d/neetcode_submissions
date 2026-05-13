# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #I cant think of the way to do this with 2 pointers, so this would be O(n) time and space

        visited = set()
        curr = head

        while curr:
            if curr in visited:
                return True
            else:
                visited.add(curr)
            curr = curr.next
            
        return False

                
                


        