class Solution:
    def reverseWords(self, s: str) -> str:
        ss = [' '] + list(s) # 特殊case: 为首个单词添加前面添加空格，使首个单词能触发反转逻辑
        n = len(ss)
        
        cur = 0
        i, j = 0, 0
        
        while cur < n:
            if cur > 0 and ss[cur-1] == ' ': # 利用单词前空格判断是否在一个新词上
                i = j = cur
                while j < n-1 and ss[j+1] != ' ':
                    j += 1
                we = j
                
                while i < j:
                    ss[i], ss[j] = ss[j], ss[i]
                    i += 1
                    j -= 1
                
                cur = we + 1
            cur += 1
        
        return ''.join(ss[1:])
