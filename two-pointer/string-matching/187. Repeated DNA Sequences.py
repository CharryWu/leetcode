def encode(c):
    if c == 'A':
        return 0
    elif c == 'C':
        return 1
    elif c == 'G':
        return 2
    else:
        return 3

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        """
        我们不要每次都去一个字符一个字符地比较子串和模式串
        而是维护一个滑动窗口，运用滑动哈希算法一边滑动一边计算窗口中字符串的哈希值
        拿这个哈希值去和模式串的哈希值比较，这样就可以避免截取子串，从而把匹配算法降低为 O(N)

        用四进制代表 ACGT，优化算法时间复杂度。
        如果不用进制编码，每次取substring 都是 O(L) 复杂度，总时间复杂度为 O(NL)，L为数字长度位数
        """
        seen = set()
        res = set() # 记录重复出现的字符串结果。这里用set去重
        snum = list(map(encode, s)) # 先把字符串转化成四进制的数字数组
        
        window_hash = 0 # 4 character system 四进制
        # 数字位数
        L = 10
        # 进制
        R = 4
        # 最高位乘数。用来将左指针的数移除当前窗口（左指针指向的即是窗口编码最高位）
        RL = R ** (L - 1)
        
        left, right = 0, 0
        while right < len(s):
            rnum = snum[right]
            right += 1
            
            window_hash = window_hash * R + rnum
            

            if right-left == L:
                if window_hash in seen:
                    res.add(s[left:right])
                else:
                    seen.add(window_hash)
                lnum = snum[left]
                left += 1
                window_hash -= lnum * RL
        return list(res)

"""
滑动窗口算法本身的时间复杂度是 O(N)，再看看窗口滑动的过程中的操作耗时，给 res 添加子串的过程用到了 substring 方法需要 O(L) 的复杂度，但一般情况下 substring 方法不会调用很多次，只有极端情况（比如字符串全都是相同的字符）下才会每次滑动窗口时都调用 substring 方法。
这个算法一般情况下的平均时间复杂度是 O(N)，极端情况下的时间复杂度会退化成 O(NL)。
"""
