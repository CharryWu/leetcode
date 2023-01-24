# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/discuss/2432235/Python%3A-sliding-window
from collections import Counter
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        """
        Simple sliding window will not work as we cannot quickly figure out conditions for expanding/shrinking.
        aaabb, k=3 Should we include b? maybe we should include bb? Maybe we should shrink aaa and work only with bb?
        
        This is brute-force approach on all unique chars counts!
        """
        n = len(s)
        
        char_freq = Counter(s)
        
        res = 0

        for max_allowed_unique_chars in range(1, len(char_freq.keys()) + 1):
            char_freq = {}
            window_unique_chars = 0
            left, right = 0, 0
            while right < n:
                rc = s[right]
                right += 1
				# add new char to the window
                if rc not in char_freq:
                    window_unique_chars += 1
                    char_freq[rc] = 1
                else:
                    char_freq[rc] += 1

				# are all char_freqs >= k?
                if all(v >= k for v in char_freq.values()):
                    res = max(res, right-left)
                
                while window_unique_chars > max_allowed_unique_chars:
                    lc = s[left]
					# remove chars until we get window_unique_chars == max_allowed_unique_chars
                    char_freq[lc] -= 1
                    
                    if char_freq[lc] == 0:
                        del char_freq[lc]
                        window_unique_chars -= 1
                    
                    left += 1

        
        return res
