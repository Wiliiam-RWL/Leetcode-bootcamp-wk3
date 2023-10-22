from collections import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        res = [[0] * len(grid[0]) for i in range(len(grid))]
        res[0][0] = grid[0][0]
        for i in range(1, len(grid)):
            res[i][0] = res[i - 1][0] + grid[i][0]
        for i in range(1, len(grid[0])):
            res[0][i] = res[0][i - 1] + grid[0][i]
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                res[i][j] = min(res[i - 1][j], res[i][j - 1]) + grid[i][j]
        return res[len(grid) - 1][len(grid[0]) - 1]
