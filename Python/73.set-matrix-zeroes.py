#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#
# https://leetcode.com/problems/set-matrix-zeroes/description/
#
# algorithms
# Medium (44.47%)
# Likes:    3420
# Dislikes: 367
# Total Accepted:    426.5K
# Total Submissions: 952.7K
# Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'
#
# Given an m x n matrix. If an element is 0, set its entire row and column to
# 0. Do it in-place.
#
# Follow up:
#
#
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best
# solution.
# Could you devise a constant space solution?
#
#
#
# Example 1:
#
#
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
#
#
# Example 2:
#
#
# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
#
#
#
# Constraints:
#
#
# m == matrix.length
# n == matrix[0].length
# 1 <= m, n <= 200
# -2^31 <= matrix[i][j] <= 2^31 - 1
#
#
#

# @lc code=start
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if matrix and matrix[0]:
            return self.constant_space_soln(matrix)
        return

    def constant_space_soln(self, matrix: List[List[int]]) -> None:
        """
        Instead of using a separate array as bitmaps, use the first
        row or col of the original matrix as bitmaps.

        Algorithm:
        1. Keep track whether the first row or col contains 0
        2. Traverse the matrix. If an element is 0, set the
           corresponding first row and col to 0
        3. Traverse the matrix again. If the first row or col is 0,
           set the entire row or col to 0
        4. Set the first row or col to 0 if they originally contained 0

        NOTE:
        - Remember to keep track of the first row or col

        Runtime: O(mn)
        Space: O(1)

        :param matrix: The matrix to set zeroes
        """
        first_row_had_zero = False
        first_col_had_zero = False

        # mark first row and col to 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    if i == 0:
                        first_row_had_zero = True
                    if j == 0:
                        first_col_had_zero = True
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # set each matrix item except for first row and col
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # set first row and col to 0 if necessary
        if first_row_had_zero:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        if first_col_had_zero:
            for i in range(len(matrix)):
                matrix[i][0] = 0

        return

    def row_col_map_soln(self, matrix: List[List[int]]) -> None:
        """
        Use a row map and a column map to track the 0 bits

        Runtime: O(mn)
        Space: O(m + n)

        :param matrix: The matrix to set zeroes
        """
        # bitmap where
        # - 0 indicates the row/col has value of zero
        # - 1 indicates the row/col has value of non-zero
        row_map = [1 for _ in matrix]
        col_map = [1 for _ in matrix[0]]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    row_map[i] = 0
                    col_map[j] = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if row_map[i] == 0 or col_map[j] == 0:
                    matrix[i][j] = 0
        return

    def brute_force_soln(self, matrix: List[List[int]]) -> None:
        """
        Brute force solution:
        Use a bitmap to keep track of the 0 elements
        Loop through the matrix to set the bitmap
        Use the bitmap to set the necessary 0 elements

        Runtime: O(m^2 * n^2)
        Space: O(mn)

        :param matrix: The matrix to set zeroes
        """
        # a bitmap where
        # - 0 indicates the element has value of zero
        # - 1 indicates the element has value of non-zero
        bitmap = [[1 for _ in matrix[0]] for _ in matrix]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    # set row to 0
                    for x in range(len(matrix[i])):
                        bitmap[i][x] = 0
                    # set col to 0
                    for y in range(len(matrix)):
                        bitmap[y][j] = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if bitmap[i][j] == 0:
                    matrix[i][j] = 0
        return


# @lc code=end

if __name__ == "__main__":
    # Test Case 1
    target = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1],
    ]
    expected = [
        [1, 0, 1],
        [0, 0, 0],
        [1, 0, 1],
    ]
    actual = Solution().setZeroes(target)
    print("Test case 1")
    for row in target:
        print(row)
    print("=====")
    for row in expected:
        print(row)

    # Test Case 2
    target = [
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5],
    ]
    expected = [
        [0, 0, 0, 0],
        [0, 4, 5, 0],
        [0, 3, 1, 0],
    ]
    actual = Solution().setZeroes(target)
    print("Test case 2")
    for row in target:
        print(row)
    print("=====")
    for row in expected:
        print(row)
