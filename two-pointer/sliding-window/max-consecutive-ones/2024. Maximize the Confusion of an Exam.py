class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        left, right = 0, 0
        res = 0
        windowT, windowF = 0, 0
        res = 0
        def isWindowConfusing():
            return right-left-windowT <= k or right-left-windowF <= k
        
        while right < len(answerKey):
            rc = answerKey[right]
            right += 1
            
            if rc == 'T':
                windowT += 1
            else:
                windowF += 1
            if isWindowConfusing():
                res = max(res, right-left)
                
            while not isWindowConfusing():
                lc = answerKey[left]
                left += 1
                if lc == 'T':
                    windowT -= 1
                else:
                    windowF -= 1
        
        return res
