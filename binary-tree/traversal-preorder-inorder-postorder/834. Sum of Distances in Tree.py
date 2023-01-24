import collections
class Solution:
    def sumOfDistancesInTree(self, N, edges):
        dic1 = collections.defaultdict(list)
        for n1, n2 in edges: # construct graph first
            dic1[n1].append(n2)
            dic1[n2].append(n1)
        
        # eachItem subtreeDist[n]=[a, b] means subtree rooted at n has totally a nodes, 
        # and sum of distance in the subtree for n is b
        subtreeDist = [[0, 0] for _ in range(N)]
        ans = [0]*N
        
        def sumSubtreeDist(n, visited):
            cnt, ret = 0, 0
            visited.add(n)
            for child in dic1[n]:
                if child in visited:
                    continue
                childcnt, childdist = sumSubtreeDist(child, visited)
                cnt += childcnt
                ret += (childcnt + childdist)
            subtreeDist[n][0] = cnt+1
            subtreeDist[n][1] = ret
            return cnt+1, ret
            
        # recursively calculate the sumDist for all subtrees 
        # 0 can be replaced with any other number in [0, N-1]
        # and the chosen root has its correct sum distance in the whole tree
        sumSubtreeDist(0, set())

        # visit and calculates the sum distance in the whole tree
        def visit(n, pre, visited):
            curSubTreeCount, curSubTreeDist = subtreeDist[n]
            if pre == -1:
                ans[n] = curSubTreeDist
            else:
                ans[n] = ans[pre]-2*curSubTreeCount+N
            visited.add(n)
            for child in dic1[n]:
                if child not in visited:
                    visit(child, n, visited)
                
        visit(0, -1, set())
        return ans