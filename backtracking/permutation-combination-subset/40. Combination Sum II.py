class Solution:
    def __init__(self):
        self.res = []
        # 记录回溯的路径
        self.track = []
        # 记录 track 中的元素之和
        self.trackSum = 0

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        # 先排序，让相同的元素靠在一起
        candidates.sort()
        self.backtrack(candidates, 0, target)
        return self.res

    # 回溯算法主函数
    def backtrack(self, nums: List[int], start: int, target: int):
        # base case，达到目标和，找到符合条件的组合
        if self.trackSum == target:
            self.res.append(self.track[:])
            return
        # base case，超过目标和，直接结束
        if self.trackSum > target:
            return

        # 回溯算法标准框架
        for i in range(start, len(nums)):
            # 剪枝逻辑，值相同的树枝，只遍历第一条
            if i > start and nums[i] == nums[i - 1]:
                continue
            # 做选择
            self.track.append(nums[i])
            self.trackSum += nums[i]
            # 递归遍历下一层回溯树
            self.backtrack(nums, i + 1, target)
            # 撤销选择
            self.track.pop()
            self.trackSum -= nums[i]
