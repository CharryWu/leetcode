class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left, right = 0, 0
        seen = set()
        
        while right < len(nums):
            rnum = nums[right]
            right += 1
            
            if rnum in seen:
                return True
            seen.add(rnum)
            
            if right - left > k:
                lnum = nums[left]
                seen.remove(lnum)
                left += 1
        return False
