class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        # 排除一些基本情况
        if k > n:
            return False
        total_sum = sum(nums)
        target, mod = divmod(total_sum, k)
        if mod:
            return False
        used = 0 # 使用位图技巧
        memo = {}

        def backtrack(k, bucket, nums, start, used, target):
            nonlocal memo
            # base case
            if k == 0:
                # 所有桶都被装满了，而且 nums 一定全部用完了
                return True
            if bucket == target:
                # 装满了当前桶，递归穷举下一个桶的选择
                # 让下一个桶从 nums[0] 开始选数字
                res = backtrack(k - 1, 0, nums, 0, used, target)
                # 缓存结果
                memo[used] = res
                return res
            if used in memo:
                # 避免冗余计算
                return memo[used]
            i = start
            while i < n:
                # 剪枝
                if used & (1 << i): # 判断第 i 位是否是 1
                    i += 1
                    # nums[i] 已经被装入别的桶中
                    continue
                if nums[i] + bucket > target:
                    i += 1
                    continue
                # 做选择
                used |= (1 << i) # 将第 i 位置为 1
                bucket += nums[i]
                # 递归穷举下一个数字是否装入当前桶
                if backtrack(k, bucket, nums, i + 1, used, target):
                    return True
                # 撤销选择
                used ^= (1 << i) # 将第 i 位置为 0
                bucket -= nums[i]
                i += 1
            return False

        # k 号桶初始什么都没装，从 nums[0] 开始做选择
        return backtrack(k, 0, nums, 0, used, target)

    def canPartitionKSubsetsTLE(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)
        n = len(nums)
        if total_sum % k != 0:
            return False

        target_group_sum = total_sum // k

        def traverse(i, cur_group_sum, k):
            nonlocal nums
            if cur_group_sum == target_group_sum:  # found a group!
                cur_group_sum = 0
                k -= 1
            if k == 0 and i == n:
                return True
            if i == n or k < 0 or cur_group_sum > target_group_sum:
                return False
            for j in range(i, n):
                nums[i], nums[j] = nums[j], nums[i]
                if traverse(i+1, cur_group_sum+nums[i], k):
                    return True
                nums[i], nums[j] = nums[j], nums[i]

            return False

        return traverse(0, 0, k)
