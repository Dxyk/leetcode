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
        return self.recursive_soln(grid)

    def recursive_soln(self, grid: List[List[int]]) -> int:
        """
        we calculate the minimum cost for each element in the matrix and return the last one

        :param grid: the grid of numbers
        :return: the minimum sum from top left to bottom right
        """
        m, n = len(grid), len(grid[0])
        cost = [[-1] * n for _ in range(m)]
        cost[-1][-1] = grid[-1][-1]
        return self._recursive_helper(0, 0, grid, cost)

    def _recursive_helper(self, x: int, y: int,
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
        right_cost = self._recursive_helper(x, y + 1, grid, cost)
        down_cost = self._recursive_helper(x + 1, y, grid, cost)
        return min(right_cost, down_cost) + grid[x][y]
