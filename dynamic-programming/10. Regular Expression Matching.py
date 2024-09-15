# https://leetcode.com/problems/valid-number/solutions/23728/a-simple-solution-in-python-based-on-dfa/
# define an NFA
class Solution():
    def isMatch(self, s: str, p: str) -> bool:
        """
        1, If p.charAt(j) == s.charAt(i) :  dp[i][j] = dp[i-1][j-1]; s[i] matches p[j], remove both p[j] AND s[i]
        2, If p[j] == '.' : dp[i][j] = dp[i-1][j-1]; Same as above, '.' Matches any single character in s, s[i] matches p[j] == '.', remove both p[j] == '.' AND s[i]
        3, If p.charAt(j) == '*': '*' matches any number of previous character p[j-1] in s
        here are two sub conditions:
                    1   if p[j-1] != s[i] : dp[i][j] = dp[i][j-2]  // p[j-1] cannot match s[i], "*" can only counts as empty for best match, remove p[j] == '*' and p[j-1], but don't remove anything from s, so p[j-2] will be compared to s[i] for match
                    2   if p[j-1] == s[i] or p[j-1] == '.':
                                    dp[i][j] = dp[i-1][j]  // in this case, * counts as multiple s[i-1], only consume s: consume s[i], but don't consume p so that "p[j-1]*" will still be used to compare to s[i-1], s[i-2], ...
                                or dp[i][j] = dp[i][j-1]   // in this case, * counts as single, only consume p: remove p[j] == '*' so that p[j-1] will be compared to s[i] for exact match
                                or dp[i][j] = dp[i][j-2]   // in this case, * counts as empty, only consume p:  remove p[j] == '*' and p[j-1], but don't remove anything from s, so p[j-2] will be compared to s[i] for match
        """
        m, n = len(s), len(p)
        dp = [[0] * (n+1) for _ in range(m+1)] # whether s[:i+1] matches p[:j+1] (first i characters from s matches first j characters from p)
        dp[0][0] = True # empty string always match

        for j in range(n):
            if p[j] == '*' and dp[0][j-1]:
                dp[0][j+1] = True

        # we're setting let i_prime = i+1, j_prime = j+1, each iteration we're setting dp[i_prime][j_prime]
        for i in range(m):
            for j in range(n):
                if p[j] == '.' or p[j] == s[i]:
                    dp[i+1][j+1] = dp[i][j]
                if p[j] == '*': # considering "p[j-1]*"
                    if p[j-1] != s[i] and p[j-1] != '.': # "p[j-1]*" doesn't match anything in s[i], s[i-1]..., therefore we have to remove it entirely (treat as empty string)
                        dp[i+1][j+1] = dp[i+1][j-1]
                    else: # if p[j-1] == s[i] or p[j-1] == '.':  "p[j-1]*" could match zero, one, or multiple characters that ends at s[i]
                        dp[i+1][j+1] = dp[i+1][j] or dp[i][j+1] or dp[i+1][j-1]
        return dp[m][n]
