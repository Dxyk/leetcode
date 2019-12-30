#
# @lc app=leetcode id=137 lang=python3
#
# [137] Single Number II
#
# https://leetcode.com/problems/single-number-ii/description/
#
# algorithms
# Medium (47.95%)
# Likes:    1117
# Dislikes: 294
# Total Accepted:    190.1K
# Total Submissions: 396K
# Testcase Example:  '[2,2,3,2]'
#
# Given a non-empty array of integers, every element appears three times except
# for one, which appears exactly once. Find that single one.
#
# Note:
#
# Your algorithm should have a linear runtime complexity. Could you implement
# it without using extra memory?
#
# Example 1:
#
#
# Input: [2,2,3,2]
# Output: 3
#
#
# Example 2:
#
#
# Input: [0,1,0,1,0,1,99]
# Output: 99
#
#

# @lc code=start
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return self.bit_manipulation_soln(nums)

    def bit_manipulation_soln(self, nums: List[int]) -> int:
        """
        Bit Manipulation solution
        """
        # TODO: understand this shit
        a = b = 0
        for c in nums:
            temp_a = (~a & b & c) | (a & ~b & ~c)
            b = (~a & ~b & c) | (~a & b & ~c)
            a = temp_a
        return a | b

    def math_soln(self, nums: List[int]) -> int:
        """
        Math solution

        Note that 3 * sum(set(nums)) - sum(nums) = 2 * res
        e.g. [a, a, a, b, b, b, c]
        3a + 3b + 3c - 3a - 3b - c = 2c

        Runtime: O(n)
        Space: O(n)
        """
        return (3 * sum(set(nums)) - sum(nums)) // 2

    def hashmap_soln(self, nums: List[int]) -> int:
        """
        Hashmap solution

        Runtime: O(n)
        Space: O(n)
        """
        nums_count = {}
        for num in nums:
            if num not in nums_count:
                nums_count[num] = 1
            else:
                nums_count[num] += 1
        for num in nums_count:
            if nums_count[num] == 1:
                return num
        return None
# @lc code=end


if __name__ == "__main__":
    print(Solution().singleNumber([2, 2, 3, 2]), 3)
    print(Solution().singleNumber([0, 1, 0, 1, 0, 1, 99]), 99)
