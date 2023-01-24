ROMAN_MAP = {
     'I': 1,
     'V': 5,
     'X': 10,
     'L': 50,
     'C': 100,
     'D': 500,
     'M': 1000,
}

class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        n = len(s)
        i = 0
        
        while i < n:
            curnum = ROMAN_MAP[s[i]]
            if i < n-1:
                nextnum = ROMAN_MAP[s[i+1]]
                if curnum < nextnum:
                    res += (nextnum - curnum)
                    i += 2
                    continue
            
            res += curnum
            i += 1
        
        return res