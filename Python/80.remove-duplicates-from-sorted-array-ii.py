#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/
#
# algorithms
# Medium (46.25%)
# Likes:    1856
# Dislikes: 791
# Total Accepted:    328.3K
# Total Submissions: 705.3K
# Testcase Example:  '[1,1,1,2,2,3]'
#
# Given a sorted array nums, remove the duplicates in-place such that
# duplicates appeared at most twice and return the new length.
#
# Do not allocate extra space for another array; you must do this by modifying
# the input array in-place with O(1) extra memory.
#
# Clarification:
#
# Confused why the returned value is an integer, but your answer is an array?
#
# Note that the input array is passed in by reference, which means a
# modification to the input array will be known to the caller.
#
# Internally you can think of this:
#
#
# // nums is passed in by reference. (i.e., without making a copy)
# int len = removeDuplicates(nums);
#
# // any modification to nums in your function would be known by the caller.
# // using the length returned by your function, it prints the first len
# elements.
# for (int i = 0; i < len; i++) {
# print(nums[i]);
# }
#
#
#
# Example 1:
#
#
# Input: nums = [1,1,1,2,2,3]
# Output: 5, nums = [1,1,2,2,3]
# Explanation: Your function should return length = 5, with the first five
# elements of nums being 1, 1, 2, 2 and 3 respectively. It doesn't matter what
# you leave beyond the returned length.
#
#
# Example 2:
#
#
# Input: nums = [0,0,1,1,1,1,2,3,3]
# Output: 7, nums = [0,0,1,1,2,3,3]
# Explanation: Your function should return length = 7, with the first seven
# elements of nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively. It
# doesn't matter what values are set beyond the returned length.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 3 * 10^4
# -10^4 <= nums[i] <= 10^4
# nums is sorted in ascending order.
#
#
#

# @lc code=start
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        return self.two_pointer_overwrite_soln(nums)

    def two_pointer_overwrite_soln(self, nums: List[int]) -> int:
        """
        Two Pointer Solution by overwriting the duplicated items with
        later items

        Use a left pointer to track the last valid item in the result and
        return this pointer's index
        Use a right pointer that is always 2 steps ahead the left pointer to
        iterate the original list
        For each iteration
        - Base case: left < 2
            - do nothing
            - increment both pointers
        - Compare the right item with the item that is 2 idx to the left of the
          left pointer
            - If the two are different
                - overwrite the left item with right item
                - increment both pointers
            - If the two are the same
                - Increment only the right pointer
                - The left pointer will be overwritten in later iterations
        Overwrite the left item with the right item if the right item and
        the item at 2 index to the left of the left pointer are different

        Runtime: O(n)
        Space: O(1)

        :param nums: The sorted list of numbers to remove 2+ duplicates from
        :return: The number of elements in the result list
        """
        left, right = 0, 0
        while right < len(nums):
            if left < 2:
                left += 1
                right += 1
            elif nums[left - 2] < nums[right]:
                nums[left] = nums[right]
                left += 1
                right += 1
            else:
                right += 1
        return left



    def two_pointer_pop_soln(self, nums: List[int]) -> int:
        """
        Two Pointer Solution by removing duplicated items

        Use a left pointer to track the first appearance of an element
        Use a right pointer to track the last appearance of an element
        Remove the element at the right pointer if the two pointers are too far apart

        NOTE
        - this solution works, but is NOT what the question is looking for,
          since it did not utilize the hint.
        - The question wants the solution to reorder the list, instead of
          removing elements from it

        Runtime: O(n)
        Space: O(1)

        :param nums: The sorted list of numbers to remove 2+ duplicates from
        :return: The number of elements in the result list
        """
        left, right = 0, 1
        while right < len(nums):
            if nums[right] == nums[left]:
                if right - left < 2:
                    right += 1
                else:
                    nums.pop(right)
            else:
                left = right
                right += 1
        return right


# @lc code=end

if __name__ == "__main__":
    # Test Case 1
    target = [1, 1, 1, 2, 2, 3]
    expected = 5
    expected_2 = [1, 1, 2, 2, 3]
    actual = Solution().removeDuplicates(target)
    print("Test case 1")
    print(actual)
    print(expected)
    print(target)
    print(expected_2)

    # Test Case 2
    target = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    expected = 7
    expected_2 = [0, 0, 1, 1, 2, 3, 3]
    actual = Solution().removeDuplicates(target)
    print("Test case 2")
    print(actual)
    print(expected)
    print(target)
    print(expected_2)
