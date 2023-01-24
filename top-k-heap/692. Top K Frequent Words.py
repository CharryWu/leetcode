import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = {}
        for word in words:
            if word not in freq:
                freq[word] = 1
            else:
                freq[word] += 1
        h = []
        for key in freq:
            heapq.heappush(h, (-freq[key], key))

        res = []
        for i in range(k):
            f, w = heapq.heappop(h)
            res.append(w)
        return res
