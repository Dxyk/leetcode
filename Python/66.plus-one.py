from typing import List
#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#
# https://leetcode.com/problems/plus-one/description/
#
# algorithms
# Easy (42.28%)
# Likes:    2208
# Dislikes: 3081
# Total Accepted:    802.2K
# Total Submissions: 1.9M
# Testcase Example:  '[1,2,3]'
#
# Given a non-empty array of decimal digits representing a non-negative
# integer, increment one to the integer.
#
# The digits are stored such that the most significant digit is at the head of
# the list, and each element in the array contains a single digit.
#
# You may assume the integer does not contain any leading zero, except the
# number 0 itself.
#
#
# Example 1:
#
#
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
#
#
# Example 2:
#
#
# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
#
#
# Example 3:
#
#
# Input: digits = [0]
# Output: [1]
#
#
#
# Constraints:
#
#
# 1 <= digits.length <= 100
# 0 <= digits[i] <= 9
#
#
#

# @lc code=start


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        Increments the integer represented by the list by 1 and return the new list

        :param digits: a list represented integer
        :return: the list represented integer incremented by 1
        """
        return self.soln(digits)

    def soln(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        digits[i] += 1
        while i > 0 and digits[i] == 10:
            digits[i] = 0
            i -= 1
            digits[i] += 1
        if digits[i] == 10:
            digits[i] = 0
            digits.insert(0, 1)
        return digits


# @lc code=end
