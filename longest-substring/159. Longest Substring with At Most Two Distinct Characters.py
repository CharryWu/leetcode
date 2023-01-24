class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
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
        n = len(s)
        res = 0
        while right < n:
            add(s[right])
            while len(freq) > 2:
                remove(s[left])
                left += 1
            res = max(right-left+1, res)
            right += 1
        
        return res
            
