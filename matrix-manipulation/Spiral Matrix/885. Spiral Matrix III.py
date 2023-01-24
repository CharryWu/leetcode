
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        ans = [(rStart, cStart)]
        """
        # 模拟G字形前进 walk simulation：假设当前步长为x。每个G都是向东走 x, 向下走x，向上走x+1，向西走x+1。
        再进入下个外围的G的时候步长就是x+2了
        Examining the lengths of our walk in each direction, we find the following pattern: 1, 1, 2, 2, 3, 3, 4, 4, ... 
        That is, we walk 1 unit east, then 1 unit south, then 2 units west, then 2 units north, then 3 units east, etc. 
        Because our walk is self-similar, this pattern repeats in the way we expect.
        """
        if rows * cols == 1:
            return ans
        
        # 模拟G字形前进 walk simulation
        curRow, curCol = rStart, cStart
        # For walk length k = 1, 3, 5 ...
        # 假设当前步长为x，再进入下个外围的G的时候步长就是x+2了
        for k in range(1, 2*(rows+cols), 2):
            for dx, dy, dk in (
                (0, 1, k), # east
                (1, 0, k), # south
                (0, -1, k+1), # west
                (-1, 0, k+1) # north
            ):
                for _ in range(dk):
                    curRow += dx
                    curCol += dy
                    # 只有当前位置在矩阵里面的时候才将其添加进入结果
                    if 0 <= curRow < rows and 0 <= curCol < cols:
                        ans.append((curRow, curCol))
                        if len(ans) == rows*cols:
                            return ans