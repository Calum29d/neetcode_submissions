# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def preOrder(node):
            if not node:
                res.append("N")
                return
            
            res.append(str(node.val))
            preOrder(node.left)
            preOrder(node.right)
        
        preOrder(root)
        return ','.join(res) #convert the array into a string with a delimiter


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        
        vals = iter(data.split(',')) #convert the string back into an iterable array

        def preOrder():
            val = next(vals) #get the current nodes value

            if val == "N":
                return None

            node = TreeNode(int(val))
            node.left = preOrder()
            node.right = preOrder()

            return node

        return preOrder()

#O(n) time and i think O(n) space maybe O(h) worst case

