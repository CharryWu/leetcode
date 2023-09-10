from collections import deque

ENTER = 0
EXIT = 1

"""
Four rules:
1) If the door was not used in the previous second, then the person who wants to exit goes first.
2) If the door was used in the previous second for entering, the person who wants to enter goes first.
3) If the door was used in the previous second for exiting, the person who wants to exit goes first.
4) If multiple persons want to go in the same direction, the person with the smallest index goes first.
"""

class Solution:
    def timeTaken(self, arrivals: List[int], states: List[int]) -> List[int]:
        n = len(arrivals)
        enter_pool, exit_pool = deque(),deque()
        cur_time = 0
        prev_state = EXIT # Rule 1): door defaults to EXIT, the person who wants to exit goes first.
        i = 0
        answer = [0] * n
        while i < n or enter_pool or exit_pool:
            # Add all arrivals to enter or exit pool for every advancement in second of time
            while i < n and arrivals[i] <= cur_time:
                if states[i] == ENTER:
                    enter_pool.append(i)
                else:
                    exit_pool.append(i)
                i += 1

            # Use popleft() for Rule 4) If multiple persons want to go in the same direction, the person with the smallest index goes first.
            # Rule 2) If the door was used in the previous second for entering, the person who wants to enter goes first.
            if prev_state == EXIT:
                if exit_pool:
                    answer[exit_pool.popleft()] = cur_time
                elif enter_pool:
                    answer[enter_pool.popleft()] = cur_time
                    prev_state = ENTER
            # Rule 3) If the door was used in the previous second for exiting, the person who wants to exit goes first.
            else:
                if enter_pool:
                    answer[enter_pool.popleft()] = cur_time
                elif exit_pool:
                    answer[exit_pool.popleft()] = cur_time
                    prev_state = EXIT
                else:
                    prev_state = EXIT
            cur_time += 1
        return answer
