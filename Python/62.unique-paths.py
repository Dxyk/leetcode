from typing import Dict, Tuple, List, Optional


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        A robot is located at the top-left corner of a m x n grid
        (marked 'Start' in the diagram below).
        diagram: https://leetcode.com/problems/unique-paths/

        The robot can only move either down or right at any point in time.
        The robot is trying to reach the bottom-right corner of the grid
        (marked 'Finish' in the diagram below).

        How many possible unique paths are there?

        >>> Solution().uniquePaths(1, 5)
        1
        >>> Solution().uniquePaths(5, 1)
        1
        >>> Solution().uniquePaths(2, 2)
        2
        >>> Solution().uniquePaths(3, 2)
        3
        >>> Solution().uniquePaths(7, 3)
        28

        :param m: num columns
        :param n: num rows
        :return: num possible unique paths to traverse from top left to bottom right
        """
        if m == 0 or n == 0:
            return 0
        else:
            return self.dp_bottom_up_soln(m, n)

    def dp_bottom_up_soln(self, m: int, n: int) -> int:
        """
        The bottom up solution:
        generate the memo from (1, 1) to (m, n).
        memo[(m, n)] = memo[(m - 1, n)] + memo[(m, n - 1)]

        :param m: num columns
        :param n: num rows
        :return: num possible unique paths to traverse from top left to bottom right
        """
        memo = [[0] * m for _ in range(n)]

        for i in range(m):
            memo[0][i] = 1
        for i in range(n):
            memo[i][0] = 1

        for i in range(1, n):
            for j in range(1, m):
                memo[i][j] = memo[i - 1][j] + memo[i][j - 1]

        return memo[-1][-1]

    def dp_memoization_soln(self, m: int, n: int) -> int:
        """
        The memoized solution:
        keep track of each calculated sub-rectangle

        :param m: num columns
        :param n: num rows
        :return: num possible unique paths to traverse from top left to bottom right
        """
        return self.dp_memoization_soln_helper(m, n, {})

    def dp_memoization_soln_helper(self, m: int, n: int, memo: Dict[Tuple[int, int], int]) -> int:
        """
        A helper method for memoization solution.
        Use a Dict memo to remember the unique paths given the dimension of the rectangle

        :param m: num columns
        :param n: num rows
        :param memo: a memo that remembers the possible paths given the dimension of rectangle
        :return: num possible unique paths to traverse from top left to bottom right
        """
        # we make m the small one to reduce duplicate
        if m > n:
            m, n = n, m

        if (m, n) in memo:
            return memo[(m, n)]
        else:
            if m <= 1 or n <= 1:
                memo[(m, n)] = 1
                res = 1
            else:
                horizontal = self.dp_memoization_soln_helper(m, n - 1, memo)
                vertical = self.dp_memoization_soln_helper(m - 1, n, memo)
                res = horizontal + vertical
            memo[(m, n)] = res
            return res

    def recursive_soln(self, m: int, n: int) -> int:
        """
        The recursive solution:
        First exhaust horizontal options, then vertical ones.
        Treat each sub-rectangle as a sub-question

        :param m: num columns
        :param n: num rows
        :return: num possible unique paths to traverse from top left to bottom right
        """
        if m <= 1 or n <= 1:
            res = 1
        else:
            horizontal = self.recursive_soln(m, n - 1)
            vertical = self.recursive_soln(m - 1, n)
            res = horizontal + vertical
        return res
