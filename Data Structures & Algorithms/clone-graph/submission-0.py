"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if node is None:
            return None
            
        oldToNew = {}

        def dfs(node):
            #if the node has alreayd been cloned then we return that node to be appended as a neighbor
            if node in oldToNew:
                return oldToNew[node]

            #if it hasnt then we clone the node and create the reference in the hashmap
            nodeCopy = Node(node.val)
            oldToNew[node] = nodeCopy

            #loop for each neighbor
            for neighbor in node.neighbors:
                #add the neighbor to neighbors
                nodeCopy.neighbors.append(dfs(neighbor))
            
            return nodeCopy
        
        return dfs(node)

