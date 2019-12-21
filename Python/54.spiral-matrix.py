from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in
        spiral order.

        >>> Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        [1, 2, 3, 6, 9, 8, 7, 4, 5]
        >>> Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
        [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

        :param matrix: the matrix
        :return: spiral traversal of the matrix
        """
        if not matrix:
            return []
        return self.matrix_rotation_soln(matrix)

    def pythonic_matrix_rotation_soln(self, matrix: List[List[int]]) -> List[int]:
        """
        T: O(n^3)
        Same as matrix_rotation_soln but a more pythonic one-liner way
        Ofc this is not to be understood

        :param matrix: the matrix
        :return: spiral traversal of the matrix
        """
        return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])

    def matrix_rotation_soln(self, matrix: List[List[int]]) -> List[int]:
        """
        T: O(n^3)
        Each iteration we pop the first row and then rotate the matrix in the reverse direction
        of the traversal

        :param matrix: the matrix
        :return: spiral traversal of the matrix
        """

        def rotate_matrix(orig_matrix: List[List[int]]) -> List[List[int]]:
            """
            return the rotated matrix

            :param orig_matrix: the original matrix
            :return: the rotated matrix
            """
            if not orig_matrix or not orig_matrix[0]:
                return [[]]

            if len(matrix) == 1 and len(matrix[0]) == 1:
                return matrix

            new_rows, new_cols = len(orig_matrix[0]), len(orig_matrix)
            rotated_matrix = [[0] * new_cols for _ in range(new_rows)]  # [num cols * num rows]
            for i in range(new_rows - 1, -1, -1):
                for j in range(new_cols):
                    rotated_matrix[new_rows - i - 1][j] = orig_matrix[j][i]
            return rotated_matrix

        res = []
        while matrix and matrix[0]:
            res.extend(matrix[0])
            matrix.pop(0)
            matrix = rotate_matrix(matrix)
        return res


if __name__ == '__main__':
    print(Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
