INT_MIN = -2**31
INT_MAX = 2**31-1

class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        num = 0
        i = 0
        while i < n and s[i] == ' ':
            i += 1
        else:
            if i == n:
                return 0

        positive = s[i] == '+'
        negative = s[i] == '-'
        if positive:
            i += 1
        if negative:
            i += 1
        while i < n and ord('0') <= ord(s[i]) <= ord('9'):
            num = num * 10 + ord(s[i])-ord('0')
            i += 1

        num = -num if negative else num
        num = INT_MAX if num > INT_MAX else num
        num = INT_MIN if num < INT_MIN else num
        return num