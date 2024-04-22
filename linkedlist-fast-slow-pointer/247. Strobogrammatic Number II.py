class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:

        def dfs(n, m):
            if n == 0:
                return [""]
            if n == 1:
                return ['1', '0', '8']

            l = dfs(n-2, m)
            res = []

            for i in range(len(l)):
                s = l[i]

                if n != m: # 两头不能出现0,只能中间某个位置出现0
                    res.append('0'+s+'0')
                res.append('1'+s+'1')
                res.append('6'+s+'9')
                res.append('9'+s+'6')
                res.append('8'+s+'8')
            return res

        return dfs(n,n)
