BASE = 1337
def mypow(a: int, k: int) -> int:
    # 计算 a 的 k 次方然后与 base 求模的结果
    # 对因子求模
    a %= BASE
    res = 1
    for _ in range(k):
        # 这里有乘法，是潜在的溢出点
        res = (res * a) % BASE
    return res
"""
a^[1,5,6,4] = a^4 * a^[1,5,6,0] = a^4 * (a^[1,5,6]) ^ 10
"""
class Solution:

    def superPow(self, a: int, b: List[int]) -> int:
        if not b:
            return 1
        last = b.pop()

        part1 = mypow(a, last)
        part2 = mypow(self.superPow(a, b), 10)
        # 每次乘法都要求模
        return (part1 * part2) % BASE