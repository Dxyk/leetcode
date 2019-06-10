from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no
        two queens attack each other.

        Given an integer n, return all distinct solutions to the n-queens puzzle.

        Each solution contains a distinct board configuration of the n-queens' placement,
        where 'Q' and '.' both indicate a queen and an empty space respectively.

        >>> Solution().solveNQueens(4)
        [['.Q..', '...Q', 'Q...', '..Q.'], ['..Q.', 'Q...', '...Q', '.Q..']]

        :param n: the number of queens
        :return: the solution
        """

if __name__ == '__main__':
    Solution().solveNQueens(4)