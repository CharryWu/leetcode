from collections import Counter

class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        c = Counter(s)
        numodd = 0
        keyodd = ''
        for key, val in c.items():
            if val % 2 == 1:
                numodd += 1
                keyodd = key

        if numodd > 1:
            return []

        mid = keyodd
        for key in c: # reduce every char count to half
            c[key] //= 2

        half = list(c.elements())
        print(half)

        def backtrack(end, tmp):
            if len(tmp) == end:
                cur = ''.join(tmp)
                ans.append(cur + mid + cur[::-1])
            else:
                for i in range(end):
                    if visited[i] or (i>0 and half[i] == half[i-1] and not visited[i-1]):
                        continue
                    visited[i] = True
                    tmp.append(half[i])
                    backtrack(end, tmp)
                    visited[i] = False
                    tmp.pop()
                    
        ans = []
        visited = [False] * len(half)
        backtrack(len(half), [])
        return ans