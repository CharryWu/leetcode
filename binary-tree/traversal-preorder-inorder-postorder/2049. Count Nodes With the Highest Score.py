from collections import defaultdict
class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        # 表节点 x 的左子节点为 tree[x][0]，节点 x 的右子节点为 tree[x][1]
        # 若 tree[x][0] 或 tree[x][1] 等于 -1 则代表空指针
        adjlist = [[-1]*2 for _ in range(n)] # 将 parents 数组转化成常规二叉树（邻接表形式）
        # 根据 parents 数组构建二叉树（跳过 parents[0] 根节点）
        for i in range(1, n): # 根据 parents 数组构建二叉树（跳过 parents[0] 根节点）
            parent_i = parents[i]
            if adjlist[parent_i][0] == -1:
                adjlist[parent_i][0] = i
            else:
                adjlist[parent_i][1] = i

        scoreToCount = defaultdict(int)
        def countNode(node):
            """
            根据 parents 数组构建二叉树（跳过 parents[0] 根节点）
            """
            if node == -1:
                return 0
            
            leftCount = countNode(adjlist[node][0])
            rightCount = countNode(adjlist[node][1])

            otherCount = n-leftCount-rightCount-1 # 后序位置，计算每个节点的「分数」
            score = max(leftCount, 1) * max(rightCount, 1) * max(otherCount, 1)
            scoreToCount[score] += 1 # 给分数 score 计数
            return leftCount + rightCount + 1

        maxScore = 0 # 计算最大分数出现的次数
        countNode(0)
        for score in scoreToCount.keys():
            maxScore = max(maxScore, score)
        return scoreToCount[maxScore]
