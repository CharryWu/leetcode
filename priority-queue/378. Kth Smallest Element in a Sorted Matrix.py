from queue import PriorityQueue
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        pq = PriorityQueue()
        n = len(matrix)
        
        for i, row in enumerate(matrix):
            pq.put((row[0], i, 0))
        

        while not pq.empty():
            topVal, topi, topj = pq.get()
            nextj = topj+1
            if nextj < n:
                pq.put((matrix[topi][nextj], topi, nextj))
            k -= 1
            if k == 0:
                return topVal
        
        return -1
