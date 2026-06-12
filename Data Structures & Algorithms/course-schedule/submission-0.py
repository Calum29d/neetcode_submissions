from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)
        visit = set()

        #make adjacency list/prerequisites
        for course, pre in prerequisites:
            preMap[course].append(pre)
        
        def dfs(course):
            #cycle detected cant finish all courses
            if course in visit:
                return False
            
            #no prerequisites so can complete
            if not preMap[course]:
                return True
            
            visit.add(course)
            #can we complete all prerequisites 
            for pre in preMap[course]:
                if not dfs(pre): return False

            visit.remove(course)
            #all prerequisites are completed so we can just empty the array so it doesnt get reused
            preMap[course] = []
            return True
        
        #go through every course
        for course in range(numCourses):
            if not dfs(course): return False
        return True


            

            





        