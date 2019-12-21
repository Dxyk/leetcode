from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        """
        Given a positive integer n, generate a square matrix filled with elements from 1 to n^2 in spiral order.

        >>> Solution().generateMatrix(3)
        [[1, 2, 3], [8, 9, 4], [7, 6, 5]]

        :param n: a positive integer
        :return: a square matrix filled with elements from 1 to n^2 in spiral order
        """
        if n <= 0:
            return []
        return self.brute_force_soln(n)

    def inside_out_build_soln(self, n: int) -> List[List[int]]:
        """
        // Note: 200 iq. no need to remember this
        The brute force solution:
        Inside out build the matrix:
        add to the top row, and then rotate the matrix

        :param n: a positive integer
        :return: a square matrix filled with elements from 1 to n^2 in spiral order
        """
        res, lo = [], n ** 2 + 1
        while lo > 1:
            lo, hi = lo - len(res), lo
            res = [list(range(lo, hi))] + zip(*res[::-1])
        return res

    def brute_force_soln(self, n: int) -> List[List[int]]:
        """
        The brute force solution: Travel in clockwise direction and assign values

        [                   [
          [1, 2, 3]           [1, 2, 3]
          [4, 5, 6]           [8, 9, 4]
          [7, 8, 9]           [7, 6, 5]
        ]                   ]

        Note:
        - Direction changes for clockwise traveling:
            r_dir   c_dir
            0       1
            1       0
            0       -1
            -1      0
        - Direction only change when the next element in res is not None (0)

        :param n: a positive integer
        :return: a square matrix filled with elements from 1 to n^2 in spiral order
        """
        res = [x[:] for x in [[0] * n] * n]

        r, c, r_dir, c_dir = 0, 0, 0, 1

        for i in range(n ** 2):
            res[r][c] = i + 1

            if res[(r + r_dir) % n][(c + c_dir) % n]:
                r_dir, c_dir = c_dir, -r_dir
            r += r_dir
            c += c_dir

        return res
