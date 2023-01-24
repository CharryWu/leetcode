class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        num_dots = 0
        res = []
        def isValidSection(start, end):
            if end > start and s[start] == '0':
                return False

            # 加速判断，减少中间变量生成
            if end-start < 2:
                return True
            elif end-start == 2:
                return int(s[start:end+1]) <= 255
            else:
                return False

        def dfs(path, i):
            if i >= n:
                return
            nonlocal num_dots
            if num_dots == 3:
                if isValidSection(i, n-1):
                    res.append(path+s[i:n])
                return
            
            num_dots += 1

            # single number section is always valid
            dfs(path+s[i]+'.', i+1)

            if isValidSection(i, i+1):
                dfs(path+s[i:i+2]+'.', i+2)
            if isValidSection(i, i+2):
                dfs(path+s[i:i+3]+'.', i+3)
            
            num_dots -= 1

        dfs("", 0)
        return res
