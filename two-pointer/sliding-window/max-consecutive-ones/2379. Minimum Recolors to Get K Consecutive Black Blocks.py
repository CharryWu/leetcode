class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left, right = 0, 0
        res = float('inf')
        window_white = 0
        
        while right < len(blocks):
            rc = blocks[right]
            right += 1
            
            if rc == 'W':
                window_white += 1
                
            while right-left >= k:
                res = min(res, window_white)
                if blocks[left] == 'W':
                    window_white -= 1
                left += 1
            
        return res
