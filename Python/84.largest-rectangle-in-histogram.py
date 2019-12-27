#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#
# https://leetcode.com/problems/largest-rectangle-in-histogram/description/
#
# algorithms
# Hard (32.94%)
# Likes:    2612
# Dislikes: 65
# Total Accepted:    212.7K
# Total Submissions: 645.1K
# Testcase Example:  '[2,1,5,6,2,3]'
#
# Given n non-negative integers representing the histogram's bar height where
# the width of each bar is 1, find the area of largest rectangle in the
# histogram.
#
#
#
#
# Above is a histogram where width of each bar is 1, given height =
# [2,1,5,6,2,3].
#
#
#
#
# The largest rectangle is shown in the shaded area, which has area = 10
# unit.
#
#
#
# Example:
#
#
# Input: [2,1,5,6,2,3]
# Output: 10
#
#
#

# @lc code=start
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        return self.stack_soln(heights)

    def stack_soln(self, heights: List[int]) -> int:
        """
        Stack Solution
        """
        heights.append(0)
        stack = [-1]
        res = 0

        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                curr_height = heights[stack.pop()]
                width = i - stack[-1] - 1
                res = max(curr_height * width, res)
            stack.append(i)

        heights.pop()  # leave input unchanged
        return res

    def dp_soln(self, heights: List[int]) -> int:
        """
        DP solution

        Save the indices of the heights that is no lower than the current 
        height in the lists max_left and max_right

        Runtime: O(n^2) for building the max left and max right lists
        """
        if len(heights) == 0:
            return 0

        max_left = [-1] * len(heights)
        max_right = [-1] * len(heights)

        for i in range(len(heights)):
            j = i - 1
            while j >= 0 and heights[j] >= heights[i]:
                j = max_left[j]
            max_left[i] = j

        for i in range(len(heights) - 1, -1, -1):
            j = i + 1
            while j < len(heights) and heights[j] >= heights[i]:
                j = max_right[j]
            max_right[i] = j

        res = 0
        for i, curr_height in enumerate(heights):
            width = max_right[i] - max_left[i] - 1
            res = max(curr_height * width, res)

        return res
# @lc code=end


if __name__ == "__main__":
    # print(Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]), 10)
    # print(Solution().largestRectangleArea([2, 0, 2]), 2)
    print(Solution().largestRectangleArea([1, 1]), 2)
