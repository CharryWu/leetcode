class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        balance = 0
        add_left = 0
        for c in s:
            if c == '(':
                balance += 1
            elif c == ')':
                balance -= 1
            if balance < 0:
                add_left += 1
                balance += 1
        return balance + add_left
