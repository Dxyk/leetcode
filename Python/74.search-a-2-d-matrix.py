#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#
# https://leetcode.com/problems/search-a-2d-matrix/description/
#
# algorithms
# Medium (37.98%)
# Likes:    3231
# Dislikes: 195
# Total Accepted:    447K
# Total Submissions: 1.2M
# Testcase Example:  '[[1,3,5,7],[10,11,16,20],[23,30,34,60]]\n3'
#
# Write an efficient algorithm that searches for a value in an m x n matrix.
# This matrix has the following properties:
#
#
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the
# previous row.
#
#
#
# Example 1:
#
#
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
#
#
# Example 2:
#
#
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
#
#
#
# Constraints:
#
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -10^4 <= matrix[i][j], target <= 10^4
#
#
#

# @lc code=start
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix and matrix[0]:
            return self.binary_search_soln(matrix, target)
        return False

    def binary_search_soln(self, matrix: List[List[int]], target: int) -> bool:
        """
        Binary Search Solution
        Treat the matrix as an array, and perform binary search on it

        Runtime: O(log(m * n)))
        Space: O(1)

        :param matrix: The matrix to query from
        :param target: The target value to query for
        :return: True if the target is in the matrix, False otherwise
        """
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1

        while left <= right:
            mid = (left + right) // 2
            curr_num = matrix[mid // cols][mid % cols]

            if curr_num == target:
                return True
            elif curr_num < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

    def divide_and_find_soln(self, matrix: List[List[int]],
                             target: int) -> bool:
        """
        Divide and Find solution
        1. Find the largest row that is smaller than or equal to the target
        2. Look for item in the row

        Runtime: O(m + n)
        Space: O(1)

        :param matrix: The matrix to query from
        :param target: The target value to query for
        :return: True if the target is in the matrix, False otherwise
        """
        row_idx = 0
        while row_idx < len(matrix) and matrix[row_idx][0] <= target:
            row_idx += 1
        row_idx -= 1
        for item in matrix[row_idx]:
            if item == target:
                return True
        return False

    def brute_force(self, matrix: List[List[int]], target: int) -> bool:
        """
        Brute force solution
        Loop through the matrix and try to find the target

        Runtime: O(mn)
        Space: O(1)

        :param matrix: The matrix to query from
        :param target: The target value to query for
        :return: True if the target is in the matrix, False otherwise
        """
        for row in matrix:
            for item in row:
                if item == target:
                    return True
        return False


# @lc code=end

if __name__ == "__main__":
    # Test Case 1
    arg = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    expected = True
    actual = Solution().searchMatrix(arg, 3)
    print("Test case 1")
    print(actual)
    print(expected)

    # Test Case 2
    arg = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    expected = False
    actual = Solution().searchMatrix(arg, 13)
    print("Test case 2")
    print(actual)
    print(expected)
