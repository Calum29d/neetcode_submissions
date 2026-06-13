from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adjMap = defaultdict(list)
        for n1, n2 in edges:
            adjMap[n1].append(n2)
            adjMap[n2].append(n1)
        
        visited = set()
        count = 0

        def dfs(node):

            visited.add(node)

            #go to every connected node, once we have visited every one unwind
            for neighbor in adjMap[node]:
                if neighbor in visited:
                    continue
                else:
                    dfs(neighbor)
            
            

        
        #go through every node until we find one that we have not explored, means a new component then mark 
        #all nodes connected to that node as visited so we then start on the next unmarked component
        for node in range(n):
            if node not in visited:
                count += 1
                dfs(node)

        #Time : O(V + E) , Space : (V + E) where V is num of nodes/vertices and E is number of edges

        return count

        
            
            




        