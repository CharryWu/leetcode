MAP = {
    '1': [],
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z'],
}

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        n = len(digits)
        if n == 0:
            return []
        def backtrack(i, path):
            nonlocal res
            if i == n:
                res.append(''.join(path))
                return
            
            for ch in MAP[digits[i]]:
                path.append(ch)
                backtrack(i+1, path)
                path.pop()
        
        backtrack(0, [])
        return res