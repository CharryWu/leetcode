class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        res = [[-1]*n for _ in range(m)]
        top, left, right, bottom = 0, 0, n-1, m-1
        k = 0
        cur = head
        i, j = 0, 0
        while cur and k < m*n:
            i, j = top, left
            while cur and j <= right:
                res[i][j] = cur.val
                cur = cur.next
                j += 1
                k += 1
            top += 1
            
            i, j = top, right
            while cur and i <= bottom:
                res[i][j] = cur.val
                cur = cur.next
                i += 1
                k += 1
            right -= 1

            i, j = bottom, right
            while cur and j >= left:
                res[i][j] = cur.val
                cur = cur.next
                j -= 1
                k += 1
            bottom -= 1

            i, j = bottom, left
            while cur and i >= top:
                res[i][j] = cur.val
                cur = cur.next
                i -= 1
                k += 1
            left += 1
        
        return res