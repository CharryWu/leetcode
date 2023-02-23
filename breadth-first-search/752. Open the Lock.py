from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        INITIAL = '0000'
        pwlen = len(INITIAL)
        # 从起点开始启动广度优先搜索
        queue = deque([INITIAL])
        visited = set([INITIAL]) # 记录已经穷举过的密码，防止走回头路
        deads = set(deadends) # 记录需要跳过的死亡密码

        def oneUp(s, i):
            return s[:i] + chr((ord(s[i])-ord('0')+1) % 10 + ord('0')) + s[i+1:]
        def oneDown(s, i):
            return s[:i] + chr((ord(s[i])-ord('0')-1) % 10 + ord('0')) + s[i+1:]
        res = 0
        while queue:
            sz = len(queue)
            # 将当前队列中的所有节点向周围扩散
            for k in range(sz):
                top = queue.popleft()
                if top in deads: # 判断是否到达终点
                    continue
                if top == target:
                    return res
                # 将一个节点的未遍历相邻节点加入队列
                for i in range(pwlen):
                    up, down = oneUp(top, i), oneDown(top, i)
                    if up not in visited:
                        queue.append(up)
                        visited.add(up)
                    if down not in visited:
                        queue.append(down)
                        visited.add(down)
            res += 1 # 在这里增加步数
        
        return -1 # 如果穷举完都没找到目标密码，那就是找不到了
