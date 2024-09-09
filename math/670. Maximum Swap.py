class Solution:
    def maximumSwap(self, num: int) -> int:
        num_str = list(str(num))
        last_seen = {}
        for i, c in enumerate(num_str):
            last_seen[int(c)] = i

        for i, c in enumerate(num_str):
            for d in range(9, int(c), -1):
                if d in last_seen and last_seen[d] > i: # if there's a bigger digit after current index i, can make swap
                    num_str[i], num_str[last_seen[d]] = num_str[last_seen[d]], num_str[i]
                    return int(''.join(num_str)) # return immediately since we can only make one swap
        return num # not found return original number
