from typing import List, Union


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        Given a m x n grid filled with non-negative numbers,
        find a path from top left to bottom right which minimizes the
        sum of all numbers along its path.

        Note: You can only move either down or right at any point in time.

        >>> Solution().minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) # 1→3→1→1→1
        7

        :param grid: the grid of numbers
        :return: the minimum sum from top left to bottom right
        """
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        return self.dp_1_soln(grid)

    def dp_1_soln(self, grid: List[List[int]]) -> int:
        """
        The dp solution with O(1) space by using the grid to store the cost

        :param grid: the grid of numbers
        :return: the minimum sum from top left to bottom right
        """
        m, n = len(grid), len(grid[0])
        for i in range(m):
            grid[i][0] = grid[i][0] + grid[i - 1][0] if i > 0 else grid[i][0]
            for j in range(1, n):
                left, up = grid[i][j - 1], grid[i - 1][j]
                grid[i][j] = min(left, up) + grid[i][j] if i > 0 else left + grid[i][j]
        return grid[-1][-1]

    def dp_n_soln(self, grid: List[List[int]]) -> int:
        """
        The dp solution with O(N) space

        :param grid: the grid of numbers
        :return: the minimum sum from top left to bottom right
        """
        m, n = len(grid), len(grid[0])
        cost = [float('inf')] * n
        for i in range(m):
            cost[0] = grid[i][0] + cost[0] if i > 0 else grid[i][0]
            for j in range(1, n):
                cost[j] = min(cost[j - 1], cost[j]) + grid[i][j]
        return int(cost[-1])

    def dp_mn_soln(self, grid: List[List[int]]) -> int:
        """
        The dp solution with O(MN) space

        :param grid: the grid of numbers
        :return: the minimum sum from top left to bottom right
        """
        m, n = len(grid), len(grid[0])
        cost = [[-1] * n for _ in range(m)]
        cost[-1][-1] = grid[-1][-1]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    cost[i][j] = grid[-1][-1]
                else:
                    right = down = float('inf')
                    if i != m - 1:
                        down = cost[i + 1][j]
                    if j != n - 1:
                        right = cost[i][j + 1]
                    cost[i][j] = min(right, down) + grid[i][j]
        return cost[0][0]

    def memoized_soln(self, grid: List[List[int]]) -> int:
        """
        we calculate the minimum cost for each element in the matrix and return the first one

        :param grid: the grid of numbers
        :return: the minimum sum from top left to bottom right
        """
        m, n = len(grid), len(grid[0])
        cost = [[-1] * n for _ in range(m)]
        cost[-1][-1] = grid[-1][-1]
        return self._memoized_helper(0, 0, grid, cost)

    def _memoized_helper(self, x: int, y: int,
                         grid: List[List[int]],
                         cost: List[List[int]]) -> Union[int, float]:
        """
        Helper for recursive helper

        :param x: the target x idx
        :param y: the target y idx
        :param grid: the grid matrix
        :param cost: the cost matrix
        :return: the cost at cost[x][y]
        """
        m, n = len(grid), len(grid[0])
        if x >= m or y >= n:
            return float('inf')
        if cost[x][y] != -1:
            return cost[x][y]
        right_cost = self._memoized_helper(x, y + 1, grid, cost)
        down_cost = self._memoized_helper(x + 1, y, grid, cost)
        return min(right_cost, down_cost) + grid[x][y]
