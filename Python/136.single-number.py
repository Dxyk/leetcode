#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#
# https://leetcode.com/problems/single-number/description/
#
# algorithms
# Easy (62.26%)
# Likes:    3219
# Dislikes: 125
# Total Accepted:    588.6K
# Total Submissions: 944.4K
# Testcase Example:  '[2,2,1]'
#
# Given a non-empty array of integers, every element appears twice except for
# one. Find that single one.
#
# Note:
#
# Your algorithm should have a linear runtime complexity. Could you implement
# it without using extra memory?
#
# Example 1:
#
#
# Input: [2,2,1]
# Output: 1
#
#
# Example 2:
#
#
# Input: [4,1,2,1,2]
# Output: 4
#
#
#

# @lc code=start
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return self.bit_manipulation_soln(nums)

    def bit_manipulation_soln(self, nums: List[int]) -> int:
        """
        Bit manipulation

        using XOR property:
        - A ^ 0 = A
        - A ^ A = 0
        """
        res = 0
        for num in nums:
            res ^= num
        return res

    def math_soln(self, nums: List[int]) -> int:
        """
        Math solution

        Note that 2 * (a + b + c) - sum(a + a + b + b + c) = c
        """
        return 2 * sum(set(nums)) - sum(nums)

    def hashmap_soln(self, nums: List[int]) -> int:
        """
        Hashmap solution

        Use a hashmap to store the index of the number. If the number is in the
        map, remove it from the hashmap

        Runtime: O(n)
        Space: O(n)
        """
        nums_map = {}
        for num in nums:
            try:
                nums_map.pop(num)
            except KeyError:
                nums_map[num] = 1
        return nums_map.popitem()[0]

    def brute_force(self, nums: List[int]) -> int:
        """
        Brute Force solution

        Copy all the numbers to a new list and remove if duplicates exist.
        There will be one element left in the list.

        Runtime: O(n^2)
        Space: O(n)
        """
        nums_cpy = []
        for num in nums:
            if num in nums_cpy:
                nums_cpy.remove(num)
            else:
                nums_cpy.append(num)
        return nums_cpy[0]
# @lc code=end


if __name__ == "__main__":
    print(Solution().singleNumber([2, 2, 1]), 1)
    print(Solution().singleNumber([4, 1, 2, 1, 2]), 4)
