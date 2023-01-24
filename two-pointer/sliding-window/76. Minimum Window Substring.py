from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        need = [0] * 52
        freq = [0] * 52
        
        def addChar(c, count_table):
            char_idx = -1
            if c.isupper():
                char_idx = ord(c)-ord('A')
            else:
                char_idx = ord(c)-ord('a') + 26
            if char_idx >= 0:
                count_table[char_idx] += 1

        def removeChar(c, count_table):
            char_idx = -1
            if c.isupper():
                char_idx = ord(c)-ord('A')
            else:
                char_idx = ord(c)-ord('a') + 26
            if char_idx >= 0:
                count_table[char_idx] -= 1
        
        def has_all_chars_from_need():
            for cur_count, need_count in zip(freq, need):
                if cur_count < need_count:
                    return False
            
            return True
        
        
        for tc in t:
            addChar(tc, need)
        
        left, right = 0, 0 # [left, right)
        while right < len(s):
            # 移动右指针的时候寻找“可行解”
            addChar(s[right], freq)
            right += 1

            
            # 移动左指针，寻找“最优解”，直到不满足条件为止
            while left < right and has_all_chars_from_need():
                res = s[left:right] if (right-left < len(res) or res == "") else res
                removeChar(s[left], freq)
                left += 1
        
        return res
