class Diff:
    def __init__(self, arr):
        n = len(arr)
        self.n = n
        self.diff = [0] * n
        self.diff[0] = arr[0]
        for i in range(1, n):
                self.diff[i] = self.diff[i] - arr[i]

    def update(self, i, j, amount):
        self.diff[i] += amount
        if j+1 < self.n:
            self.diff[j+1] -= amount
    
    def getArr(self):
        arr = [0] * self.n
        arr[0] = self.diff[0]
        for i in range(1, self.n):
            arr[i] = self.diff[i] + arr[i-1]
        return arr
                
class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        diff = Diff([0]*length)
        for s, e, amount in updates:
            diff.update(s, e, amount)
        
        return diff.getArr()
