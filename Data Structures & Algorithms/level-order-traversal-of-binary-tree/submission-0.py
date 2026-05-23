# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        queue = deque([root])
        res = []

        if root is None:
            return res

        while queue:
            levelNodes = []

            #loop for how many nodes are on the current level
            for i in range(len(queue)):
                node = queue.popleft()
                levelNodes.append(node.val)

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

            #add the current levels nodes to the result array
            res.append(levelNodes)
        
        return res

        #O(n) time and O(n) space where n is num of nodes in the tree


            


            
            
        