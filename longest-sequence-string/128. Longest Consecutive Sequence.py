class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        for num in nums:
            s.add(num)
        
        res = 0
        for num in s:
            if num-1 in s:
                continue
            cur_num = num
            cur_len = 1

            while cur_num + 1 in s:
                cur_num += 1
                cur_len += 1
            
            res = max(res, cur_len)
        
        return res