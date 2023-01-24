class Solution:
    def reverseVowels(self, s: str) -> str:
        ss = list(s)
        n = len(ss)
        V = {'a','e','i','o','u', 'A', 'E', 'I', 'O', 'U'}
        i, j = 0, n-1
        
        while i < j:
            while i < n and ss[i] not in V:
                i += 1
            
            while j >= 0 and ss[j] not in V:
                j -= 1
            
            if i >= j:
                break
            
            ss[i], ss[j] = ss[j], ss[i]
            i += 1
            j -= 1
        return ''.join(ss)
