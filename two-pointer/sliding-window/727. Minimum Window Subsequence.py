class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        """
        Idea: 用三个指针，双指针 left, right 指向 s1，一个指针 s2_ptr 指向 s2
        每次循环向右移动 right，比较 s1[right] == s2[s2_ptr]
            - 如果为真，同时向右移动 right, s2_ptr，直到 s2_ptr 到达 s2 结尾。
            - 此时 s1[left:right] 窗口包含一个完整 s2 序列，但窗口前面可能有多余字符，我们需要找到最小窗口的起始下标（>= left)
            - 将 right 赋值给 left，反向向左移动 s2_ptr 和 left 直到 s2_ptr 刚好到达 s2 起始（消耗掉 s2 中所有字符）
            - 此时的 s1[left:right] 就是以right 为结尾的最小窗口，将其与全局长度比较并更新全局长度
        """
        n, m = len(s1), len(s2)
        right = 0
        s2_ptr = 0
        matched = ""
        min_len = float('inf')

        while right < n:
            while right < n and s2_ptr < m:
                if s1[right] == s2[s2_ptr]:
                    s2_ptr += 1
                right += 1

            if right == n and s2_ptr < m: # haven't found match since last found
                break

            # POSTCOND: right points to next char of window end
            # window end = right-1, try to find left such that s1[left:right] is a valid window contain all s2
            left = right-1
            s2_ptr -= 1
            while s2_ptr >= 0:
                if s1[left] == s2[s2_ptr]:
                    s2_ptr -= 1
                left -= 1

            # POSTCOND: The above while loop consumed all chars of s2,
            # s1[left:right] is a valid window, and is the shortest window ending at right-1
            left += 1
            s2_ptr = 0
            if right-left < min_len:
                matched = s1[left:right]
                min_len = min(min_len, right-left)

        return matched
