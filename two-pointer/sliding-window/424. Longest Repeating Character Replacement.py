class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        counts = [0] * 26

        def add(c):
            counts[ord(c)-ord('A')] += 1
        def remove(c):
            counts[ord(c)-ord('A')] -= 1
        
        def check_at_least_one_valid(l, r):
            for i, count in enumerate(counts):
                if r-l-count <= k:
                    return True
            return False
        
        res = 0
        while right < len(s):
            rc = s[right]
            right += 1
            add(rc)
            
            if check_at_least_one_valid(left, right):
                res = max(res, right-left)
                
            while not check_at_least_one_valid(left, right):
                lc = s[left]
                left += 1
                remove(lc)
        return res
