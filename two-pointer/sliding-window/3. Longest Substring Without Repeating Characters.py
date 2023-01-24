from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = Counter()
        
        left, right = 0, 0
        n = len(s)
        res = 0
        while right < n:
            rc = s[right]
            right += 1

            chars[rc] += 1 # 更新右字符频率

            while chars[rc] > 1:
                lc = s[left]
                chars[lc] -= 1
                left += 1
            res = max(right-left, res)
        
        return res

