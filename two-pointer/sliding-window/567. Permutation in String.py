class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)

        if n1 > n2:
            return False

        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(n1): # go through the first window of characters length n1 in both s1 and s2
            s1Count[ord(s1[i])-ord('a')] += 1
            s2Count[ord(s2[i])-ord('a')] += 1

        matches = 0 # go through the freq table and compute matches
        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0

        # sliding window
        l = 0
        for r in range(n1, n2):
            # s1Count stays same during loop, we will be adding or substracting s2Count based on
            #
            if matches == 26:
                return True

            index = ord(s2[r]) - ord("a")
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]: # new char s2[r] makes up a match
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]: # new char s2[r] introduces a mismatch
                matches -= 1
            # NOTE: can't directly use else condition for mismatch, because if duplicate characters
            # exist, using else will double count mismatch

            index = ord(s2[l]) - ord("a")
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]: # new char s2[l] makes up a match
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]: # new char s2[l] introduces a match
                matches -= 1
            l += 1
        return matches == 26
