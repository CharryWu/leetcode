class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n # 注意这里 k 有可能 > n
        counter = 0 # 用counter 控制循环次数，如果 n / k 不为整数的话，防止多余迭代导致错误结果
        
        start, prev = 0, 0
        while counter < n:
            current, prev = start, nums[start]
            # 每次外部循环更新将所有 start + xk 更新, x = 1, 2, 3...
            while True:
                next_idx = (current + k) % n
                prev, nums[next_idx], current = nums[next_idx], prev, next_idx
                counter += 1
                if current == start:
                    break
            
            start += 1 # 每次将
        
        