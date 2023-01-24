"""
这道题说 matrix 从上到下递增，从左到右递增，显然左上角是最小元素，右下角是最大元素。我们如果想高效在 matrix 中搜索一个元素，肯定需要从某个角开始，比如说从左上角开始，然后每次只能向右或向下移动，不要走回头路。
但实际上不用这么麻烦，我们不要从左上角开始，而是从右上角开始，规定只能向左或向下移动。

你注意，如果向左移动，元素在减小，如果向下移动，元素在增大，这样的话我们就可以根据当前位置的元素和 target 的相对大小来判断应该往哪移动，不断接近从而找到 target 的位置。

当然，如果你想从左下角开始，规定只能向右或向上移动也可以，具体看代码吧。

"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n-1 # 初始化在右上角
        while i < m and j >= 0:
            if target == matrix[i][j]:
                return True
            if target > matrix[i][j]: # 需要大一点，往下移动
                i += 1
            else: # 需要小一点，往左移动
                j -= 1
        return False # while 循环中没有找到，则 target 不存在