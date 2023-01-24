from collections import deque

# 单调队列的实现
class MonoQueue:
    def __init__(self):
        self.q = deque([])
    
    def push(self, n):
        # 将小于 n 的元素全部删除
        while len(self.q) > 0 and self.q[-1] < n:
            self.q.pop()
        self.q.append(n)
    
    def getMax(self):
        return self.q[0]
    
    def pop(self, n):
        if n == self.q[0]:
            self.q.popleft()

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = MonoQueue()
        res = []
        
        right = 0
        while right < len(nums):
            if right < k-1:
                # 先填满窗口的前 k - 1
                window.push(nums[right])
            else:
                window.push(nums[right]) # 从第k个开始填充res数组
                res.append(window.getMax())
                window.pop(nums[right-k+1])
            right += 1
        
        
        return res
