class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        left, right = 0, n-1
        idx = -1
        while left <= right:
            mid = (left+right) // 2
            if x == arr[mid]:
                idx = mid
                break
            elif x < arr[mid]:
                right = mid-1
            elif x > arr[mid]:
                left = mid+1
        
        lo, hi = idx, idx+1
        if idx == -1:
            lo, hi = left-1, left
        
        res = []
        while k > 0:
            if hi == n:
                res.append(arr[lo])
                lo -= 1
                k -= 1
                continue
            elif lo < 0:
                res.append(arr[hi])
                hi += 1
                k -= 1
                continue
            
            if abs(arr[lo]-x) < abs(arr[hi]-x):
                res.append(arr[lo])
                lo -= 1
            elif abs(arr[lo]-x) > abs(arr[hi]-x):
                res.append(arr[hi])
                hi += 1
            elif abs(arr[lo]-x) == abs(arr[hi]-x):
                res.append(arr[lo])
                lo -= 1
            k -= 1
        return sorted(res)