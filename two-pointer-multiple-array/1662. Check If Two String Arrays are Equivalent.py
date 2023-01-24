class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        p1, p2 = 0, 0
        w1, w2 = 0, 0
        m, n = len(word1), len(word2)
            
        while w1 < m and w2 < n:
            if word1[w1][p1] != word2[w2][p2]:
                return False
            if p1+1 >= len(word1[w1]):
                w1 += 1
                p1 = 0
            else:
                p1 += 1
            
            if p2+1 >= len(word2[w2]):
                w2 += 1
                p2 = 0
            else:
                p2 += 1
        
        return w1 == m and w2 == n