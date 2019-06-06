from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        You are given an n x n 2D matrix representing an image.

        Rotate the image by 90 degrees (clockwise).

        Note:
        You have to rotate the image in-place, which means you have to modify the input 2D matrix
        directly. DO NOT allocate another 2D matrix and do the rotation.

        1 2 3       7 4 1
        4 5 6   =>  8 5 2
        7 8 9       9 6 3

        >>> Solution().rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        >>> Solution().rotate([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]])
        [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]

        :param matrix: A n * n 2D matrix
        :return: None
        """
        if not matrix:
            return
        return self.my_soln(matrix)

    def my_soln(self, matrix: List[List[int]]) -> None:
        """
        First reverse symmetry, then reverse left right
        1 2 3       1 4 7       7 4 1
        4 5 6   =>  2 5 8   =>  8 5 2
        7 8 9       3 6 9       9 6 3

        :param matrix: A n * n 2D matrix
        :return: None
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            for j in range(n // 2):
                # list[~i] = list[len(list) - 1 - i]
                matrix[i][j], matrix[i][~j] = matrix[i][~j], matrix[i][j]
        return matrix

    def brute_force_rotation(self, matrix: List[List[int]]) -> None:
        """
        for every iteration, substitute the top left -> top right -> bottom right -> bottom left

        :param matrix: A n * n 2D matrix
        :return: None
        """
        n = len(matrix)
        for i in range(n // 2):
            for j in range(i, n - i - 1):
                temp = matrix[i][j]
                matrix[i][j] = matrix[~j][i]
                matrix[~j][i] = matrix[~i][~j]
                matrix[~i][~j] = matrix[j][~i]
                matrix[j][~i] = temp
        return matrix


if __name__ == '__main__':
    print(Solution().rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))