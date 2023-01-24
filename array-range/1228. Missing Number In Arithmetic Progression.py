class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        n = len(arr)
        diff1 = arr[1]-arr[0]
        diff2 = arr[2]-arr[1]
        diff = diff1
        if abs(diff2) < abs(diff1):
            diff = diff2
            return arr[0]+diff2
        
        i = 0
        while i < n-1:
            if arr[i+1]-arr[i] != diff:
                return arr[i] + diff
            i += 1
        
        return arr[n-1]