#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#
# https://leetcode.com/problems/subsets-ii/description/
#
# algorithms
# Medium (44.60%)
# Likes:    1225
# Dislikes: 56
# Total Accepted:    239K
# Total Submissions: 535.6K
# Testcase Example:  '[1,2,2]'
#
# Given a collection of integers that might contain duplicates, nums, return
# all possible subsets (the power set).
#
# Note: The solution set must not contain duplicate subsets.
#
# Example:
#
#
# Input: [1,2,2]
# Output:
# [
# ⁠ [2],
# ⁠ [1],
# ⁠ [1,2,2],
# ⁠ [2,2],
# ⁠ [1,2],
# ⁠ []
# ]
#
#
#

# @lc code=start
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        return self.backtrack_soln(nums)

    def backtrack_soln(self, nums: List[int]) -> List[List[int]]:
        """
        Backtracking Solution
        """
        sorted_nums = sorted(nums)
        res = []

        def backtrack_helper(curr_subset: List[int], start: int) -> None:
            res.append(curr_subset[:])
            for i in range(start, len(sorted_nums)):
                if i > start and sorted_nums[i] == sorted_nums[i - 1]:
                    continue
                curr_subset.append(sorted_nums[i])
                backtrack_helper(curr_subset, i + 1)
                curr_subset.pop()

        backtrack_helper([], 0)
        return res
# @lc code=end
