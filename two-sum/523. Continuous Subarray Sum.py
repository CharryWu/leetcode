class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
        if s % k == 0 
        
        """
        n = len(nums)
        # initialize the hash map with index 0 for sum 0
        hash_map = {0: 0}
        s = 0
        for i in range(n):
            s += nums[i]
            # if the remainder s % k occurs for the first time
            mod = s % k
            if mod not in hash_map:
                hash_map[mod] = i + 1
            # if the subarray size is at least two
            # 注意这里用小于号。若有个区间和能被k整除
            # 那么区间末尾位置的 mod = s % k 上次在 hash_map 出现的位置一定是在区间开始元素的前一位
            elif hash_map[mod] < i:
                return True
        return False

