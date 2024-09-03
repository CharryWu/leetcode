class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.strip('/')
        path = path.split('/')
        res = []
        for p in path:
            if p == '' or p == '.':
                continue
            elif p == '..':
                if len(res) > 0:
                    res.pop()
            else:
                res.append(p)
        return '/' + '/'.join(res)
