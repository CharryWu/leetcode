    class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        temp = [0] * n # 用来存每次merge 的数。in place merge
        def merge(lo, mi, hi):
            for i in range(lo, hi+1):
                temp[i] = nums[i]
            
            p1, p2 = lo, mi+1 # p2 初始值为 mi+1
            for p in range(lo, hi+1):
                if p1 == mi+1: # 注意这里是 mi+1 不是 mi
                    nums[p] = temp[p2]
                    p2 += 1
                elif p2 == hi+1: # 注意这里是 hi+1 不是 hi
                    nums[p] = temp[p1]
                    p1 += 1
                elif temp[p1] <= temp[p2]:
                    nums[p] = temp[p1]
                    p1 += 1
                else:
                    nums[p] = temp[p2]
                    p2 += 1
            
        def mergeList(lo, hi):
            if lo == hi: # terminal condition: 待merge的只有一个元素
                return
            mid = (lo + hi) // 2
            mergeList(lo, mid)
            mergeList(mid+1, hi)
            merge(lo, mid, hi)
        
        mergeList(0, n-1)
        
        return nums