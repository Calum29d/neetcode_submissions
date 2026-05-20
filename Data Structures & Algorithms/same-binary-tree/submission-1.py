# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        #if both trees have hit the bottom then we know that both subtrees are equal
        if p is None and q is None:
            return True
        
        #if one of the trees hits the bottom at a different time then we know that they arent equal and if values arent equal then they're obviously not equal
        if p is None or q is None or p.val != q.val:
            return False

        #returns true if both comparisons return true
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))

        #O(n) time and O(h) space where n is num of nodes and h is the recursion stack which is the height of the trees 
        



        