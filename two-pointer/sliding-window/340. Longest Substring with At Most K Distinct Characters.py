class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        freq = {}
        
        def add(c):
            if c not in freq:
                freq[c] = 1
            else:
                freq[c] += 1

        def remove(c):
            if c in freq:
                freq[c] -= 1
                if freq[c] <= 0:
                    del freq[c]

        
        left, right = 0, 0
        res = 0
        while right < len(s):
            rc = s[right]
            right += 1
            add(rc)
            if len(freq) <= k:
                res = max(right-left, res)
            while len(freq) > k:
                lc = s[left]
                left += 1
                remove(lc)
        
        return res

