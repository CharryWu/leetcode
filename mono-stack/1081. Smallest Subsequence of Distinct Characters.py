class Solution:
    def smallestSubsequence(self, s: str) -> str:
        """
        要求一、要去重。
        要求二、去重字符串中的字符顺序不能打乱 s 中字符出现的相对顺序。
        要求三、在所有符合上一条要求的去重字符串中，字典序最小的作为最终结果。
        要利用 stack 结构和一个 inStack 布尔数组来满足上述三个条件，具体思路如下：
        通过 inStack 这个布尔数组做到栈 stk 中不存在重复元素，满足要求一。
        我们顺序遍历字符串 s，通过「栈」这种顺序结构的 push/pop 操作记录结果字符串，保证了字符出现的顺序和 s 中出现的顺序一致，满足要求二。
        我们用类似单调栈的思路，配合计数器 count 不断 pop 掉不符合最小字典序的字符，保证了最终得到的结果字典序最小，满足要求三。
        """
        stack = []
        count = [0] * 26 # 当前尚未考虑过的字符集
        def getIdx(c):
            return ord(c)-ord('a')
        for c in s:
            count[getIdx(c)] += 1

        inStack = [False] * 26 # 控制每个字符在stack中只出现一次
        for c in s:
            count[getIdx(c)] -= 1 # 考虑当前的字符c，从count中移除
            if inStack[getIdx(c)]: # 如stack里已经有字符，则不用字符c
                continue
            # 否则将字符c加入到栈里面。同时考虑是否需要将stack尾部字符剔除（因为字典序可能不是最小的）
            while stack and stack[-1] > c:
                # 如果stack尾部字符是其在整个string的最后一个，不能删除
                if count[getIdx(stack[-1])] == 0:
                    break
                else: # 否则删除stack尾部的字符
                    inStack[getIdx(stack[-1])] = False
                    stack.pop()

            stack.append(c)
            inStack[getIdx(c)] = True
            
        # 遍历完string以后，stack就是我们想要的答案
        return ''.join(stack)