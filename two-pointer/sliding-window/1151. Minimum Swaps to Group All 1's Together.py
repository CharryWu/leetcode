class Solution:
    def minSwaps(self, data: List[int]) -> int:
        need_count = sum(data)
        i = 0
        max_window_ones = 0
        window_count = 0

        for j, char in enumerate(data):
            if char == 1:
                window_count += 1
            if j-i+1 > need_count:
                if data[i] == 1:
                    window_count -= 1
                i += 1

            max_window_ones = max(max_window_ones, window_count)

        return need_count - max_window_ones
