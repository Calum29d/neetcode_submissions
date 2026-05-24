# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.answer = None
        self.inOrder(root)

        return self.answer

    def inOrder(self, root):

        #base case
        if root is None:
            return None

        #traverse the left 
        self.inOrder(root.left)

        #process the node visited by decrementing from the num of nodes to vist
        self.k -= 1

        #once we have visited k nodes the current node will be the kth smallest node
        if self.k == 0:
            self.answer = root.val
        
        #traverse the right
        self.inOrder(root.right)


        
        

        