#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
# https://leetcode.com/problems/subsets/description/
#
# algorithms
# Medium (56.75%)
# Likes:    2665
# Dislikes: 62
# Total Accepted:    456.3K
# Total Submissions: 803.6K
# Testcase Example:  '[1,2,3]'
#
# Given a set of distinct integers, nums, return all possible subsets (the
# power set).
#
# Note: The solution set must not contain duplicate subsets.
#
# Example:
#
#
# Input: nums = [1,2,3]
# Output:
# [
# ⁠ [3],
#  [1],
#  [2],
#  [1,2,3],
#  [1,3],
#  [2,3],
#  [1,2],
#  []
# ]
#
#

# @lc code=start
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.backtrack_soln(nums)

    def backtrack_soln(self, nums: List[int]) -> List[List[int]]:
        """
        Backtracking solution
        """
        res = []

        def backtrack_helper(curr_subset: List[int], start: int) -> None:
            res.append(curr_subset[:])
            for i in range(start, len(nums)):
                curr_subset.append(nums[i])
                backtrack_helper(curr_subset, i + 1)
                curr_subset.pop()
            return

        backtrack_helper([], 0)
        return res
# @lc code=end


if __name__ == "__main__":
    print(Solution().backtrack_soln([1, 2, 3]))
