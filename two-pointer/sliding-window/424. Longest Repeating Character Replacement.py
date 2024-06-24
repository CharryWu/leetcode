class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0]*26
        res = 0
        i = 0
        maxf = 0

        for j, c in enumerate(s):
            count[ord(c)-ord('A')] += 1
            # maxf = max(maxf, count[ord(c)-ord('A')])

            # if window invalid, move left pointer until window valid
            while (j-i+1)- max(count) > k:
                count[ord(s[i])-ord('A')] -= 1
                i += 1
            res = max(res, j-i+1)
        return res

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0]*26
        res = 0
        i = 0
        maxf = 0

        for j, c in enumerate(s):
            count[ord(c)-ord('A')] += 1
            maxf = max(maxf, count[ord(c)-ord('A')])

            # if window invalid, move left pointer until window valid
            # maxf only gets incremented never decremented, because the result depends on maxf only
            # The window size can either grow by one, or stay the same

            # If <=k replaced chars, we accept new char at right into our window. Left stays the same, so the window grows by one
            # Else s[right] does not keep <=k replaced chars, so we shrink the window by increasing left. But we take right into our window anyway, thus being -1 + 1 = 0
            # So the window can only grow when there are <=k replaced chars.
            # Hence the max will only increase if there are <=k replaced chars.
            # So essentially after each iteration, the window size will remain max long, or increase to max+1 long.
            while (j-i+1)- maxf > k:
                count[ord(s[i])-ord('A')] -= 1
                i += 1
            res = max(res, j-i+1)
        return res
