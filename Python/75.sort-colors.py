#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#
# https://leetcode.com/problems/sort-colors/description/
#
# algorithms
# Medium (44.04%)
# Likes:    2249
# Dislikes: 183
# Total Accepted:    387.9K
# Total Submissions: 880.6K
# Testcase Example:  '[2,0,2,1,1,0]'
#
# Given an array with n objects colored red, white or blue, sort them in-place
# so that objects of the same color are adjacent, with the colors in the order
# red, white and blue.
#
# Here, we will use the integers 0, 1, and 2 to represent the color red, white,
# and blue respectively.
#
# Note: You are not suppose to use the library's sort function for this
# problem.
#
# Example:
#
#
# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
#
# Follow up:
#
#
# A rather straight forward solution is a two-pass algorithm using counting
# sort.
# First, iterate the array counting number of 0's, 1's, and 2's, then overwrite
# array with total number of 0's, then 1's and followed by 2's.
# Could you come up with a one-pass algorithm using only constant space?
#
#
#

# @lc code=start

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        self.two_pass(nums)
        return

    def one_pass(self, nums: List[int]) -> None:
        idx1, idx2, idx0 = 0, len(nums)-1, 0
        while idx1 <= idx2:
            if nums[idx1] == 0:
                nums[idx1], nums[idx0] = nums[idx0], nums[idx1]
                idx1 += 1
                idx0 += 1
            elif nums[idx1] == 2:
                nums[idx1], nums[idx2] = nums[idx2], nums[idx1]
                idx2 -= 1
            else:
                idx1 += 1
        return

    def two_pass(self, nums: List[int]) -> None:
        """
        First count numbers of 0, 1, 2s
        Then rewrite the array according to the counts

        Runtime: O(n)
        """
        count_dict = {k: 0 for k in [0, 1, 2]}
        for num in nums:
            count_dict[num] += 1
        c0, c1, c2 = count_dict[0], count_dict[1], count_dict[2]
        nums[:c0] = [0] * c0
        nums[c0: c0 + c1] = [1] * c1
        nums[c0 + c1:] = [2] * c2
        return

    def built_in(self, nums: List[int]) -> None:
        """
        built in sort method
        """
        nums.sort()
        return

# @lc code=end


if __name__ == "__main__":
    a = [2, 0, 2, 1, 1, 0]
    b = [0, 0, 1, 1, 2, 2]
    Solution().sortColors(a)
    print(a == b)
