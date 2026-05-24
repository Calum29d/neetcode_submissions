# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #base case for when the subtree is created
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0]) #gets the root for the current subtree
        mid = inorder.index(preorder[0]) #finds the index of the root in preorder array
        #everything to the left of the root in preorder is in the left subtree, on right, right subtree

        
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root

        #O(n^2) time O(n) space, would never have figured this out myself
        