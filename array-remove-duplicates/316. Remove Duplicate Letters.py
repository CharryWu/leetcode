class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
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
        count = [0] * 26
        def getIdx(c):
            return ord(c)-ord('a')
        for c in s:
            count[getIdx(c)] += 1
        
        inStack = [0] * 26
        for c in s:
            count[getIdx(c)] -= 1
            if inStack[getIdx(c)]:
                continue
            
            while stack and stack[-1] > c:
                if count[getIdx(stack[-1])] == 0:
                    break
                else:
                    inStack[getIdx(stack[-1])] = False
                    stack.pop()

            stack.append(c)
            inStack[getIdx(c)] = True
            
        sb = []
        while stack:
            sb.append(stack.pop())
        return ''.join(reversed(sb))