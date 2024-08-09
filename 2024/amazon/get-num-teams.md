https://www.fastprep.io/problems/amazon-get-num-teams


Reference: https://stackoverflow.com/questions/72990065/two-sum-but-sum-is-in-a-range
This problem is essentially a two-sum problem, but the target is a range.
To solve this problem, we first sort the input array. For each number `skill[i]`, we want to find a `skill[j]` where `j > i` and `min_skill <= skill[i]+skill[j] <= max_skill`. We can use binary search to find the positions `j1` of lower bound and and `j2` of upper bound number, the difference `j2-j1+1` are the number of skill[j] that can make up the pair. Going through the array and summing up all gives the final answer.

```python3
from bisect import bisect_left, bisect_right

class Solution:
    def getNumTeams(self, skill: List[int], min_skill: int, max_skill: int) -> int:
        skill.sort()
        n = len(skill)
        res = 0
        for i in range(n):
            j1 = bisect_left(skill, min_skill-skill[i], i+1)
            j2 = bisect_right(skill, max_skill-skill[i], i+1)
            res += (j2-j1) # since bisect_left and bisect_right are used, we don't need +1.
            # If target exists, j2 - j1 gives correct # of occurrences of target
            #  If target doesn't exist, j2 - j1 == 0
        return res

```
