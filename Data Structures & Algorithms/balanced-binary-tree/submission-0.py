# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isBalanced = True

        def dfs(root):
            # base case
            if not root:
                return 0

            # get the height of the left and right subtrees
            left = dfs(root.left)
            right =  dfs(root.right)

            # if difference not valid then not balanced
            if abs(left - right) > 1:
                self.isBalanced = False
            
            # add the edge and get the greater height 
            return 1 + max(left, right)
        
        dfs(root)
        return self.isBalanced

        #O(n) time O(h) space
            

        