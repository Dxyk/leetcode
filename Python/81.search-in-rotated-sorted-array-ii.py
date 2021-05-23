#
# @lc app=leetcode id=81 lang=python3
#
# [81] Search in Rotated Sorted Array II
#
# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
#
# algorithms
# Medium (33.62%)
# Likes:    2115
# Dislikes: 585
# Total Accepted:    304.8K
# Total Submissions: 902.7K
# Testcase Example:  '[2,5,6,0,0,1,2]\n0'
#
# There is an integer array nums sorted in non-decreasing order (not
# necessarily with distinct values).
#
# Before being passed to your function, nums is rotated at an unknown pivot
# index k (0 <= k < nums.length) such that the resulting array is [nums[k],
# nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For
# example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become
# [4,5,6,6,7,0,1,2,4,4].
#
# Given the array nums after the rotation and an integer target, return true if
# target is in nums, or false if it is not in nums.
#
#
# Example 1:
# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true
# Example 2:
# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false
#
#
# Constraints:
#
#
# 1 <= nums.length <= 5000
# -10^4 <= nums[i] <= 10^4
# nums is guaranteed to be rotated at some pivot.
# -10^4 <= target <= 10^4
#
#
#
# Follow up: This problem is the same as Search in Rotated Sorted Array, where
# nums may contain duplicates. Would this affect the runtime complexity? How
# and why?
#

# @lc code=start
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        """
        :param nums: The rotated array
        :param target: The target to verify
        :return: True if the target exists in the array, False otherwise
        """
        return self.binary_search(nums, target)

    def binary_search(self, nums: List[int], target: int) -> bool:
        """
        Binary Search Solution

        1. check if nums[mid] == target
        2. check if the left part of the list is sorted (nums[left] <= nums[mid])
            i. if target in range of left sorted, search on the left half
            ii. else, search on the right half
        3. if left is not sorted, then the right half is sorted
            i. if target in range of right sorted, search on the right half
            ii. else, search on the left half

        Runtime: O(log(n)) / O(n) worst case
        Space: O(1)
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return True

            if nums[left] == nums[mid] and nums[right] == nums[mid]:
                # deal with duplicated case by moving both pointers in by 1
                left += 1
                right -= 1

            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False

    def brute_force(self, nums: List[int], target: int) -> bool:
        """
        Brute Force Solution
        Loops through all elements in the array to check if
        the target exists

        Runtime: O(n)
        Space: O(1)
        """
        for item in nums:
            if item == target:
                return True
        return False


# @lc code=end

if __name__ == "__main__":
    # Test Case 1
    input1 = [2, 5, 6, 0, 0, 1, 2]
    input2 = 0
    expected = True
    actual = Solution().search(input1, input2)
    print("Test case 1")
    print(actual)
    print(expected)

    # Test Case 2
    input1 = [2, 5, 6, 0, 0, 1, 2]
    input2 = 3
    expected = False
    actual = Solution().search(input1, input2)
    print("Test case 2")
    print(actual)
    print(expected)
