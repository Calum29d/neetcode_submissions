# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = None
        
        return self.inOrder(root)
        


    def inOrder(self, root):

        #once we have gotten to the bottom of the tree we then go back up to start processing
        if root is None:
            return True
        
        #process the left subtrees, if its not a valid BST then return false
        if not self.inOrder(root.left):
            return False
        
        #now process the node to check if the bst is valid
        if self.prev != None and root.val <= self.prev:
            return False
        
        #update the prev nodes value
        self.prev = root.val

        #now check the right subtrees
        if not self.inOrder(root.right):
            return False

        return True

#O(n) time O(h) space



        
        
        
        