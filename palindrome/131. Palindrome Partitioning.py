class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []
        res = []
        n = len(s)

        def isPalindrome(i, j):
            """
            Check if s[i:j] is valid palindrome
            Note j could be equal to n
            """
            lo, hi = i, j-1
            while lo < hi:
                if s[lo] != s[hi]:
                    return False
                lo += 1
                hi -= 1
            return True

        def recur(i, path):
            if i == n:
                res.append(list(path))

            for j in range(i+1, n+1):
                if not isPalindrome(i, j):
                    continue
                path.append(s[i:j])
                recur(j, path)
                path.pop()
        recur(0, [])
        return res