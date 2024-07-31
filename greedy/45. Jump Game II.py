class Solution:
    def jump(self, nums: List[int]) -> int:
        # use greedy, similar to BFS
        # use two pointers to record the window's left and right boundary
        # compute the boundary of next window from jumps within current window
        res = 0
        l, r = 0, 0

        while r < len(nums)-1:
            farthest = 0
            for i in range(l, r+1): # going through all jump distances within current window
                farthest = max(farthest, i+nums[i])
            l = r+1
            r = farthest
            res += 1

        return res
