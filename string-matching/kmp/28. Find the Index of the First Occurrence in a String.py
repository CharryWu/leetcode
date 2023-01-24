class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        M, N = len(needle), len(haystack)
        def computeLPSArray(pat):
            lps = [0] * M
            prevl = 0 # length of the previous longest prefix suffix
            i = 1 # lps[0] is always 0
            while i < M:
                if pat[i] == pat[prevl]:
                    prevl += 1
                    lps[i] = prevl
                    i += 1
                else:
                    if prevl != 0:
                        prevl = lps[prevl-1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps

        # create lps[] that will hold the longest prefix suffix
        # values for pattern
        j = 0 # index for needle[]
        lps = computeLPSArray(needle)
        i = 0 # index for haystack[]
        while (N-i) >= (M-j):
            if needle[j] == haystack[i]:
                i += 1
                j += 1
            if j == M:
                return i-j
            elif i < N and needle[j] != haystack[i]:
                # Do not match lps[0..lps[j-1]] characters,
                # they will match anyway
                if j != 0:
                    j = lps[j-1]
                else:
                    i += 1
        return -1
