import sys
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(32):
            counter = 0
            mask = 1 << i
            for num in nums:
                has_bit = num & mask
                if has_bit != 0:
                    counter += 1
            if counter % 3 != 0:
                res = res | mask # set the bit 
        print(sys.getsizeof(res))
        print(res)
        # return ctypes.c_int32(res).value # python's 

print(Solution().singleNumber([-2,-2,1,1,4,1,4,4,-4,-2]))