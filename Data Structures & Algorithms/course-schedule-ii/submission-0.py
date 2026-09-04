class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = defaultdict(list) # node : [list of prerequisites]
        curPath, addedCourses = set(), set()
        res = []

        for node, pre in prerequisites:
            adjList[node].append(pre)
        

        def dfs(course):
            # base case
            if course in curPath: # cycle detected
                return False
            
            if course in addedCourses: # already added node to res
                return True
            
            curPath.add(course)

            for pre in adjList[course]:
                if not dfs(pre):
                    return False
            
            res.append(course)
            curPath.remove(course)
            addedCourses.add(course)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        return res
            
            
            

        