class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        寻找回文串的问题核心思想是：从中间开始向两边扩散来判断回文串，对于最长回文子串，就是这个意思：

        找回文串的关键技巧是传入两个指针 l 和 r 向两边扩散，因为这样实现可以同时处理回文串长度为奇数和偶数的情况。

        for 0 <= i < len(s):
            # 找到以 s[i] 为中心的回文串
            palindrome(s, i, i)
            # 找到以 s[i] 和 s[i+1] 为中心的回文串
            palindrome(s, i, i + 1)
            更新答案
        """
        n = len(s)
        if n == 1:
            return s
        res = s[0]
        maxL, maxR = 0, 0
        def findPalindrome(l, r):
            while l-1 >= 0 and r+1 <= n-1 and s[l-1] == s[r+1]:
                l -= 1
                r += 1
            return l, r
        
        for i in range(n):
            oddL, oddR = findPalindrome(i, i)
            if oddR - oddL >= maxR - maxL:
                maxL, maxR = oddL, oddR
            if i+1 < n and s[i] == s[i+1]:
                evenL, evenR = findPalindrome(i, i+1)
                if evenR - evenL >= maxR - maxL:
                    maxL, maxR = evenL, evenR
        
        return s[maxL:maxR+1]