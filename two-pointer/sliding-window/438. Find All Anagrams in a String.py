NUM_CHARS = 26
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        plen = len(p)
        res = []
        need = [0] * NUM_CHARS
        freq = [0] * NUM_CHARS
        
        def addChar(c, count_table):
            count_table[ord(c)-ord('a')] += 1

        def removeChar(c, count_table):
            count_table[ord(c)-ord('a')] -= 1
        
        
        
        for cp in p:
            addChar(cp, need)
        
        left, right = 0, 0 # [left, right)
        while right < len(s):
            # 移动右指针的时候寻找“可行解”
            addChar(s[right], freq)
            right += 1

            
            # 移动左指针，寻找“最优解”，直到不满足条件为止
            if right-left >= plen: # 本题移动 left 缩小窗口的时机是窗口大小大于 t.size() 时，因为排列嘛，显然长度应该是一样的。
                if right-left == plen and need == freq:
                    res.append(left) # 当发现 valid == need.size() 时，就说明窗口中就是一个合法的排列，所以立即返回 true。
                removeChar(s[left], freq)
                left += 1

        return res
