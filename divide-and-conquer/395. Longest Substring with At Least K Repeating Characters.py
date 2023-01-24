class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        n = len(s)
        def getIdx(c):
            return ord(c) - ord('a')
        
        def dfs(start, end, k):
            nonlocal s
            if end-start < k: return 0 # 窗口太小，不满足条件直接退出
            # 对于每个窗口，重新进行字符频数分析
            freq = [0] * 26
            for i in range(start, end):
                freq[getIdx(s[i])] += 1
            
            # 找到下个二分的中点：当前区间第一个不满足频率k的字符
            for mid in range(start, end):
                if freq[getIdx(s[mid])] >= k:
                    continue
                mid_next = mid + 1
                # 同时跳过其之后紧接着的所有不满足字符，减少递归调用（剪枝）
                while mid_next < end and freq[getIdx(s[mid_next])] < k:
                    mid_next += 1
                return max(dfs(start, mid, k), dfs(mid_next, end, k)) # 只有在当前窗口出现频率小于k的数才需要进行递归，对 start~mid 左 mid_next~end 右区间进行调用
            return end-start # 如果当前区间字符都满足要求，就返回区间长度
        return dfs(0, n, k)
