NUM_CHARS = 26
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        对于这道题的解法代码，基本上和最小覆盖子串一模一样，只需要改变几个地方：

        1、本题移动 left 缩小窗口的时机是窗口大小大于 t.size() 时，因为排列嘛，显然长度应该是一样的。

        2、当发现 valid == need.size() 时，就说明窗口中就是一个合法的排列，所以立即返回 true。

        至于如何处理窗口的扩大和缩小，和最小覆盖子串完全相同。
        """
        need = [0] * NUM_CHARS
        freq = [0] * NUM_CHARS
        
        def addChar(c, count_table):
            count_table[ord(c)-ord('a')] += 1

        def removeChar(c, count_table):
            count_table[ord(c)-ord('a')] -= 1
        
        
        
        for c1 in s1:
            addChar(c1, need)
        
        left, right = 0, 0 # [left, right)
        while right < len(s2):
            # 移动右指针的时候寻找“可行解”
            addChar(s2[right], freq)
            right += 1

            
            # 移动左指针，寻找“最优解”，直到不满足条件为止
            while right-left >= len(s1): # 本题移动 left 缩小窗口的时机是窗口大小大于 t.size() 时，因为排列嘛，显然长度应该是一样的。
                if right-left == len(s1) and need == freq:
                    return True # 当发现 valid == need.size() 时，就说明窗口中就是一个合法的排列，所以立即返回 true。
                removeChar(s2[left], freq)
                left += 1

        return False

# 由于这道题中 [left, right) 其实维护的是一个定长的窗口，窗口大小为 t.size()。因为定长窗口每次向前滑动时只会移出一个字符，所以可以把内层的 while 改成 if，效果是一样的
