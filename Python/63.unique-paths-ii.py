from typing import Dict, List, Tuple


class Solution:
    def uniquePathsWithObstacles(self, obstacle_grid: List[List[int]]) -> int:
        """
        A robot is located at the top-left corner of a m x n grid
        (marked 'Start' in the diagram below).

        The robot can only move either down or right at any point in time.
        The robot is trying to reach the bottom-right corner of the grid
        (marked 'Finish' in the diagram below).

        Now consider if some obstacles are added to the grids.
        How many unique paths would there be?

        >>> grid = [[0]]
        >>> Solution().uniquePathsWithObstacles(grid)
        1
        >>> grid = [[1]]
        >>> Solution().uniquePathsWithObstacles(grid)
        0
        >>> grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        >>> Solution().uniquePathsWithObstacles(grid)
        2
        >>> grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        >>> Solution().uniquePathsWithObstacles(grid)
        2

        :param obstacle_grid: the grid with obstacles
        :return: the number of unique paths
        """
        if len(obstacle_grid) == 0 or len(obstacle_grid[0]) == 0:
            return 0
        return self.dp_soln(obstacle_grid)

    def dp_soln(self, obstacle_grid: List[List[int]]) -> int:
        """
        The dynamic_programming_solution

        :param obstacle_grid: the grid with obstacles
        :return: the number of unique paths
        """
        memo = [[0] * len(obstacle_grid[0]) for _ in range(len(obstacle_grid))]
        memo[0][0] = 1 if obstacle_grid[0][0] == 0 else 0

        for i in range(len(obstacle_grid)):
            for j in range(len(obstacle_grid[0])):
                if obstacle_grid[i][j] == 1:
                    memo[i][j] = 0
                else:
                    if i - 1 >= 0:
                        memo[i][j] += memo[i - 1][j]
                    if j - 1 >= 0:
                        memo[i][j] += memo[i][j - 1]
        return memo[-1][-1]

    def recursive_soln(self, obstacle_grid: List[List[int]]) -> int:
        """
        The recursive solution

        :param obstacle_grid: the grid with obstacles
        :return: the number of unique paths
        """
        memo = {}
        m, n = len(obstacle_grid) - 1, len(obstacle_grid[0]) - 1

        return self._recursive_soln_helper(obstacle_grid, m, n, memo)

    def _recursive_soln_helper(self, obstacle_grid: List[List[int]],
                               m: int,
                               n: int,
                               memo: Dict[Tuple[int, int], int]) -> int:
        """
        Helper for recursive solution

        :param obstacle_grid: the grid with obstacles
        :param m: the row num
        :param n: the col num
        :param memo: the memo
        :return: the number of unique paths
        """
        if (m, n) in memo:
            return memo[(m, n)]
        if m < 0 or n < 0 or obstacle_grid[m][n] == 1:
            return 0
        if m == 0 and n == 0:
            return 1

        prev_up = self._recursive_soln_helper(obstacle_grid, m - 1, n, memo)
        prev_left = self._recursive_soln_helper(obstacle_grid, m, n - 1, memo)
        curr_res = prev_up + prev_left
        memo[(m, n)] = curr_res

        return curr_res
