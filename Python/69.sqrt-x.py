#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#
# https://leetcode.com/problems/sqrtx/description/
#
# algorithms
# Easy (35.22%)
# Likes:    1892
# Dislikes: 2289
# Total Accepted:    698.5K
# Total Submissions: 2M
# Testcase Example:  '4'
#
# Given a non-negative integer x, compute and return the square root of x.
#
# Since the return type is an integer, the decimal digits are truncated, and
# only the integer part of the result is returned.
#
#
# Example 1:
#
#
# Input: x = 4
# Output: 2
#
#
# Example 2:
#
#
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since the decimal part
# is truncated, 2 is returned.
#
#
# Constraints:
#
#
# 0 <= x <= 2^31 - 1
#
#
#


# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        return self.binary_search_soln(x)

    def binary_search_soln(self, x: int) -> int:
        """
        Binary Search to search for floor sqrt of x

        Runtime: O(log(N))
        Space: O(1)

        :param x: the target x to take sqrt of
        :return: the floor int of sqrt(x)
        """
        if x == 1:
            return 1
        left, right = 0, x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            else:
                if mid * mid > x:
                    right = mid
                else:
                    left = mid

    def python_soln(self, x: int) -> int:
        """
        Basic Python solution using the `**` power operator

        Runtime: O(1)
        Space: O(1)

        :param x: the target x to take sqrt of
        :return: the floor int of sqrt(x)
        """
        x = str(x**0.5)
        x = x.split('.')
        return int(x[0])


# @lc code=end

if __name__ == "__main__":
    print(Solution().mySqrt(4))
    print(Solution().mySqrt(0))
