# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #this is the iterative solution, its slightly more efficent because it doesnt have the recursive call stack
        #so its O(h) time and O(1) space
        curr = root

        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right 
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                return curr
        