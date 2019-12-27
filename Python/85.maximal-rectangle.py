#
# @lc app=leetcode id=85 lang=python3
#
# [85] Maximal Rectangle
#
# https://leetcode.com/problems/maximal-rectangle/description/
#
# algorithms
# Hard (35.40%)
# Likes:    1960
# Dislikes: 55
# Total Accepted:    146.6K
# Total Submissions: 413.8K
# Testcase Example:
#   '[["1","0","1","0","0"],
#     ["1","0","1","1","1"],
#     ["1","1","1","1","1"],
#     ["1","0","0","1","0"]]'
#
# Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle
# containing only 1's and return its area.
#
# Example:
#
#
# Input:
# [
# ⁠ ["1","0","1","0","0"],
# ⁠ ["1","0","1","1","1"],
# ⁠ ["1","1","1","1","1"],
# ⁠ ["1","0","0","1","0"]
# ]
# Output: 6
#
#
#

# @lc code=start
from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        return self.dp_soln(matrix)

    def stack_soln(self, matrix: List[List[str]]) -> int:
        """
        Stack solution

        See similar idea in 84.largest-rectangle-in-histogram.py
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        heights = [0] * (len(matrix[0]) + 1)
        res = 0
        for row in matrix:
            for i in range(len(row)):
                if row[i] == "1":
                    heights[i] += 1
                else:
                    heights[i] = 0
            stack = [-1]
            for i in range(len(row) + 1):
                while heights[i] < heights[stack[-1]]:
                    height = heights[stack.pop()]
                    width = i - stack[-1] - 1
                    res = max(height * width, res)
                stack.append(i)
        return res

    def dp_soln(self, matrix: List[List[str]]) -> int:
        """
        DP solution

        - height[i] records the current number of continuos '1' in column i;
        - left_max[i] records the left_max most index j which satisfies that
            for any index k from j to i, height[k] >= height[i];
        - right_max[i] records the right_max most index j which satisfies that
            for any index k from i to j, height[k] >= height[i];
        """
        if not matrix:
            return 0
        left_max = [0] * len(matrix[0])
        right_max = [len(matrix[0])] * len(matrix[0])
        height = [0] * len(matrix[0])

        res = 0
        for i in range(len(matrix)):
            cur_left = 0
            for j in range(len(matrix[i])):
                if matrix[i][j] == '1':
                    left_max[j] = max(left_max[j], cur_left)
                else:
                    left_max[j] = 0
                    cur_left = j + 1

            cur_right = len(matrix[i])
            for j in range(len(matrix[i]) - 1, -1, -1):
                if matrix[i][j] == '1':
                    right_max[j] = min(right_max[j], cur_right)
                else:
                    right_max[j] = len(matrix[i])
                    cur_right = j

            for j in range(len(matrix[i])):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0

            for j in range(len(matrix[i])):
                h = height[j]
                w = right_max[j] - left_max[j]
                res = max(res, w * h)
        return res
# @lc code=end


if __name__ == "__main__":
    m = [["1", "0", "1", "0", "0"],
         ["1", "0", "1", "1", "1"],
         ["1", "1", "1", "1", "1"],
         ["1", "0", "0", "1", "0"]
         ]
    print(Solution().maximalRectangle(m), 6)
