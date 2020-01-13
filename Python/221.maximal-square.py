#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#
# https://leetcode.com/problems/maximal-square/description/
#
# algorithms
# Medium (34.82%)
# Likes:    1997
# Dislikes: 49
# Total Accepted:    175K
# Total Submissions: 500.4K
# Testcase Example:
#   '[["1","0","1","0","0"],
#    ["1","0","1","1","1"],
#    ["1","1","1","1","1"],
#    ["1","0","0","1","0"]]'
#
# Given a 2D binary matrix filled with 0's and 1's, find the largest square
# containing only 1's and return its area.
#
# Example:
#
#
# Input:
#
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
#
# Output: 4
#
#

# @lc code=start
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        return self.dp_improved_bottom_up(matrix)

    def dp_improved_bottom_up(self, matrix: List[List[str]]) -> int:
        """
        DP Bottom up solution with improved space efficiency

        Runtime: O(mn)
        Space: O(n)
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        res_len = 0
        prev = 0
        memo = [0] * (len(matrix[0]) + 1)
        for i in range(1, len(matrix) + 1):
            for j in range(1, len(matrix[0]) + 1):
                temp = memo[j]
                if matrix[i - 1][j - 1] == "1":
                    memo[j] = min(memo[j - 1], prev, memo[j]) + 1
                    res_len = max(memo[j], res_len)
                else:
                    memo[j] = 0
                prev = temp
        return res_len ** 2

    def dp_bottom_up(self, matrix: List[List[str]]) -> int:
        """
        DP Bottom up solution

        Runtime: O(mn)
        Space: O(mn)
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        res_len = 0
        memo = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        for i in range(1, len(matrix) + 1):
            for j in range(1, len(matrix[0]) + 1):
                if matrix[i - 1][j - 1] == "1":
                    memo[i][j] = min(memo[i - 1][j],
                                     memo[i][j - 1],
                                     memo[i - 1][j - 1]) + 1
                    res_len = max(memo[i][j], res_len)
        return res_len ** 2

    def dp_recursive(self, matrix: List[List[str]]) -> int:
        """
        DP Recursive solution

        Subproblem Structure:
        Let m = num rows, n = num cols
        P(i, j) := max area's length using the element at matrix[i][j]
        P(i, j) =
        - 0 if matrix[i][j] == "0"
        - min(P(i - 1, j), P(i, j - 1), P(i - 1, j - 1)) + 1
                if matrix[i][j] == "1"
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        res_len = [0]

        def helper(i: int, j: int) -> int:
            if i < 0 or j < 0:
                return 0
            if i == 0 or j == 0:
                return 1 if matrix[i][j] == "1" else 0
            top_res = helper(i, j - 1)
            left_res = helper(i - 1, j)
            top_left_res = helper(i - 1, j - 1)
            if matrix[i][j] == "1":
                res = min(top_res, left_res, top_left_res) + 1
            else:
                res = 0
            res_len[0] = max(res, res_len[0])
            return res

        helper(len(matrix) - 1, len(matrix[0]) - 1)

        return res_len[0] ** 2
# @lc code=end


if __name__ == "__main__":
    m = [["1", "0", "1", "0", "0"],
         ["1", "0", "1", "1", "1"],
         ["1", "1", "1", "1", "1"],
         ["1", "0", "0", "1", "0"]]
    print(Solution().maximalSquare(m), 4)
