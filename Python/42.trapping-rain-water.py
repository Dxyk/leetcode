#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
# https://leetcode.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (46.02%)
# Likes:    5139
# Dislikes: 95
# Total Accepted:    397.2K
# Total Submissions: 863.1K
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it is able to trap after raining.
#
#
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In
# this case, 6 units of rain water (blue section) are being trapped. Thanks
# Marcos for contributing this image!
#
# Example:
#
#
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
#
#

# @lc code=start
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        return self.two_pointer_soln(height)

    def two_pointer_soln(self, height: List[int]) -> int:
        """
        Two pointer solution

        Runtime: O(n)
        Space: O(1)
        """
        res = 0
        left, right = 0, len(height) - 1
        left_max = right_max = 0
        while left < right:
            curr_left, curr_right = height[left], height[right]
            if curr_left < curr_right:
                if curr_left > left_max:
                    left_max = curr_left
                else:
                    res += left_max - curr_left
                left += 1
            else:
                if curr_right > right_max:
                    right_max = curr_right
                else:
                    res += right_max - curr_right
                right -= 1
        return res

    def stack_soln(self, height: List[int]) -> int:
        """
        Stack solution

        By using a stack, only 1 loop is needed

        Runtime: O(n)
        Space: O(n)
        """
        res = 0
        stack = []
        for i, curr_height in enumerate(height):
            while len(stack) > 0 and height[stack[-1]] < curr_height:
                left_bottom_height = height[stack.pop()]
                if len(stack) == 0:
                    break
                left_upper_idx = stack[-1]
                left_upper_height = height[left_upper_idx]
                diff = min(left_upper_height, curr_height) - left_bottom_height
                width = i - left_upper_idx - 1
                res += width * diff
            stack.append(i)
        return res

    def dp_soln(self, height: List[int]) -> int:
        """
        DP solution

        Store the max_left, max_right idx so that we don't need
        to recompute them every iteration compared to bf soln

        Runtime: O(n)
        Space: O(n)
        """
        if len(height) == 0:
            return 0

        res = 0
        max_lefts = [0] * len(height)
        max_rights = [0] * len(height)

        max_lefts[0] = height[0]
        for i in range(1, len(height)):
            max_lefts[i] = max(height[i], max_lefts[i - 1])

        max_rights[-1] = height[-1]
        for i in range(len(height) - 2, -1, -1):
            max_rights[i] = max(height[i], max_rights[i + 1])

        for i in range(len(height)):
            max_left, max_right = max_lefts[i], max_rights[i]
            res += max(min(max_left, max_right) - height[i], 0)

        return res

    def brute_force(self, height: List[int]) -> int:
        """
        brute force solution

        Runtime: O(n^2)
        Space: O(1)
        """
        if len(height) == 0:
            return 0

        res = 0
        for i in range(len(height)):
            max_left = max_right = 0
            for j in range(i):
                max_left = max(height[j], max_left)
            for j in range(i + 1, len(height)):
                max_right = max(height[j], max_right)
            res += max(min(max_left, max_right) - height[i], 0)
        return res

# @lc code=end


if __name__ == "__main__":
    print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6)
