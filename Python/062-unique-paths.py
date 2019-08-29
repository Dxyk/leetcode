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
            return self.recursive_soln(m, n)

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
            return 1
        else:
            return self.recursive_soln(m - 1, n) + self.recursive_soln(m, n - 1)
