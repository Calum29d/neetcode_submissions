from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #Valid Graph = connected, Acyclic and for n vertices there is n - 1 edges

        #we know its not a valid graph is num of vertices - 1 does not equal num of edges
        if n - 1 != len(edges):
            return False
        
        #make adjList for undirected list
        adjMap = defaultdict(list)
        for node1, node2 in edges:
            adjMap[node1].append(node2)
            adjMap[node2].append(node1)

        visit = set()

        def dfs(node, prevNode):
            #if cycle exists
            if node in visit:
                return False

            #visit the node
            visit.add(node)

            for neighbor in adjMap[node]:
                #dont go back to the prev node
                if neighbor == prevNode:
                    continue
                if not dfs(neighbor, node): return False
            
            return True

        dfs(0, None)

        #check if the graph is connected
        if len(visit) != n:
            return False
        
        return True
        
                
            



        


