from typing import *
from bisect import bisect_left, bisect_right

# def binSearch(arr, target, left, right):
#     while left <= right:
#         mid = (left+right) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] > target:
#             left = mid+1
#         else:
#             right = mid-1
#     return left

# https://www.fastprep.io/problems/amazon-get-num-teams
class Solution:
    def getNumTeams(self, skill: List[int], min_skill: int, max_skill: int) -> int:
        skill.sort()
        n = len(skill)
        res = 0
        for i in range(n):
            j1 = bisect_left(skill, min_skill-skill[i], i+1)
            j2 = bisect_right(skill, max_skill-skill[i], i+1)
            res += (j2-j1)
        return res


# print(Solution().getNumTeams([2, 3, 4, 5], 5, 7))
# print(Solution().getNumTeams([2, 5, 8, 10], 14, 19))
