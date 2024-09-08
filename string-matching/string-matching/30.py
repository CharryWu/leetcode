from collections import Counter
from typing import List

# Solution with illustration https://leetcode.com/problems/substring-with-concatenation-of-all-words/solutions/1753357/clear-solution-easy-to-understand-with-diagrams-o-n-x-w-approach/
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """
        Let wordlen = len(words[0])
        Time O(len(s) * wordlen)
        Use two hashmaps + two pointers
        - `need` one hashmap to count all frequencies of each word in words
        - `window` one to count current each substring's frequency in current window s[left:left+wordlen*len(words)]
        - `matched_substrs` count how many words in window has been matched

        We consider all such windows starting from 0, 1, 2, 3, ... wordlen-1, each time moving left/right pointer by wordlen.
        This problem effectively is a combination of wordlen sliding window problems.
         i  ---> i+w ---> i+2w ----> i+3w ----> i+4w
         (i+1)  ---> (i+1)+w ---> (i+1)+2w ----> (i+1)+3w ----> (i+1)+4w
         (i+2)  ---> (i+2)+w ---> (i+2)+2w ----> (i+2)+3w ----> (i+2)+4w
         (i+3)  ---> (i+3)+w ---> (i+3)+2w ----> (i+3)+3w ----> (i+3)+4w

        If there's a mismatch at right pointer, we move left pointer by wordlen because
        any window that includes the mismatch is invalid window. Also we need to reset counter to zero

        If advancing right pointer causes excess of substring in current window, we shrink the window size by wordlen and
        update substring count in `window` hashmap accordingly
        """
        need = Counter() # substr => frequency in `words`
        for word in words:
            need[word] += 1

        res = []
        wordlen = len(words[0])

        for k in range(wordlen):
            window = Counter() # window substr => frequency in s[left:right], right == i + wordlen*len(words)
            left = k
            matched_substrs = 0 # sum of all frequencies in `window`. matched_substrs == sum(window.values())
            for right in range(left, len(s), wordlen):
                if right + wordlen > len(s): # out of bounds, cannot form window
                    break
                nextsubstr = s[right:right+wordlen]
                if nextsubstr in need: # matched
                    window[nextsubstr] += 1
                    matched_substrs += 1
                    if window[nextsubstr] > need[nextsubstr]: # matched, but excess, need move left pointer till no excess
                        while window[nextsubstr] > need[nextsubstr]:
                            oldsubstr = s[left:left+wordlen]
                            window[oldsubstr] -= 1
                            matched_substrs -= 1
                            left += wordlen
                    if matched_substrs == len(words): # yay! we found a permutation of words
                        res.append(left)
                        window[s[left:left+wordlen]] -= 1
                        matched_substrs -= 1
                        left += wordlen
                else: # mismatch, reset counter, and move left
                    window.clear()
                    matched_substrs = 0
                    left = right + wordlen

        return res
