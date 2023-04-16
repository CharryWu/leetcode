class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        tokens = s.split()
        n = len(tokens)
        i = 0
        num = 0
        prevnum = float('-inf')
        while i < n:
            if tokens[i].isnumeric():
                num = int(tokens[i])
                if num <= prevnum:
                    return False
                prevnum = num
            i += 1
        return True