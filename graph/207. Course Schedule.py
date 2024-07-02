from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # visitSet
        visiting = set() # all courses along curr DFS path

        def dfs(course):
            """
            Return if course can be completed
            """
            if course in visiting: # detect loop
                return False
            if len(preMap[course]) == 0:
                return True # can be completed without any prereq

            visiting.add(course)
            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            preMap[course] = [] # shortcut: return True if ever visited
            visiting.remove(course)
            return True

        for c in range(numCourses): # iterate through every course
            if not dfs(c):
                return False
        return True
