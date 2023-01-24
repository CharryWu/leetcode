import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
            
        h = []
        for key in freq:
            heapq.heappush(h, (-freq[key], key))
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(h)[1])
        return res
