import heapq
from collections import Counter, deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Time complexity: O(len(tasks)*n)
        # use maxheap and queue, maxheap stores available task to be executed with largest remaining count at the root
        # queue stores the task that's in cool off period, can only be taken out to heap once time >= availableTime
        count = Counter(tasks)
        maxheap = [-cnt for cnt in count.values()]
        heapq.heapify(maxheap)

        q = deque() # pairs of [-cnt, availableTime]
        time = 0

        while maxheap or q: # have more task to process
            time += 1

            if maxheap:
                # process the task at heap root (with largest remaining count)
                cnt = 1 + heapq.heappop(maxheap) # cnt is negative, so + 1 is -1 if it's positive
                if cnt < 0: # while task has any remaining count, add to waiting queue again
                    q.append((cnt, time+n)) # next available time is time + n

            if q and q[0][1] == time:
                heapq.heappush(maxheap, q.popleft()[0])

        return time
