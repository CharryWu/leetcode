from queue import PriorityQueue
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m, n = len(nums1), len(nums2)
        res = []
        pq = PriorityQueue()
        
        for i1 in range(m):
            pq.put((nums1[i1] + nums2[0], i1, 0))

        while not pq.empty() and k > 0:
            topSum, topi1, topi2 = pq.get() # min sum in current heapq
            k -= 1
            
            res.append((nums1[topi1], nums2[topi2]))

            nxti2 = topi2+1 # pivot on i, move on to the include next j in search
            if nxti2 < n:
                nxtSum = nums1[topi1] + nums2[nxti2]
                pq.put((nxtSum, topi1, nxti2))

        
        return res
