class Solution:  # 520 ms, faster than 96.50%
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        For convinience, let's call the cell with value 0 as zero-cell, the cell has with value 1 as one-cell, the distance of the nearest 0 of a cell as distance.
        Firstly, we can see that the distance of all zero-cells are 0, so we skip zero-cells, we process one-cells only.
        In DP, we can only use prevous values if they're already computed.
        In this problem, a cell has at most 4 neighbors that are left, top, right, bottom. If we use dynamic programming to compute the distance of the current cell based on 4 neighbors simultaneously, it's impossible because we are not sure if distance of neighboring cells is already computed or not.
        That's why, we need to compute the distance one by one:
        Firstly, for a cell, we restrict it to only 2 directions which are left and top. Then we iterate cells from top to bottom, and from left to right, we calculate the distance of a cell based on its left and top neighbors.
        Secondly, for a cell, we restrict it only have 2 directions which are right and bottom. Then we iterate cells from bottom to top, and from right to left, we update the distance of a cell based on its right and bottom neighbors.
        """
        m, n = len(mat), len(mat[0])

        for r in range(m):
            for c in range(n):
                if mat[r][c] > 0:
                    top = mat[r-1][c] if r > 0 else float('inf')
                    left = mat[r][c-1] if c > 0 else float('inf')
                    mat[r][c] = min(top, left)+1
        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                if mat[r][c] > 0:
                    bottom = mat[r+1][c] if r < m-1 else float('inf')
                    right = mat[r][c+1] if c < n-1 else float('inf')
                    mat[r][c] = min(mat[r][c], bottom+1, right+1)
        
        return mat
