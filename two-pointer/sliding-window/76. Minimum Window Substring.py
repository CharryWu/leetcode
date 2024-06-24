from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Use sliding window, forward left pointer (shrink window) as long as condition is met
        (to obtain minimum window), forward right pointer if condition is not met

        Condition:
        """
        ns, nt = len(s), len(t)
        countT, window = Counter(t), Counter()

        have, need = 0, len(countT) # unique characters in string of T
        res, resLen = [-1, -1], float('inf')
        l = 0
        for r in range(ns):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]: # check if window satisfies condition of T
                have += 1

            while have == need: # met condition, forward left pointer (shrink window) until condition is not met
                if (r - l + 1) < resLen: # found new minimum length, update window length
                    res = [l, r]
                    resLen = r - l + 1

                window[s[l]] -= 1 # keep shrinking
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""

