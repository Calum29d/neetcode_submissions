# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #keep track of max from above the node and if greater than node x then its not good
        if not root:
            return 0
        
        self.res = 0


        def dfs(node, aboveMax):
            
            # base case
            if not node:
                return
            
            if node.val >= aboveMax:
                self.res += 1
                aboveMax = node.val
            
            dfs(node.left, aboveMax)
            dfs(node.right, aboveMax)
        
        dfs(root, root.val)
        return self.res

        #O(n) time where n is num of nodes O(h) space where h is the height of the tree

            
            
            
            
            

            

            

            

        