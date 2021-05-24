#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#
# https://leetcode.com/problems/merge-sorted-array/description/
#
# algorithms
# Easy (40.81%)
# Likes:    3837
# Dislikes: 5388
# Total Accepted:    882.6K
# Total Submissions: 2.2M
# Testcase Example:  '[1,2,3,0,0,0]\n3\n[2,5,6]\n3'
#
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as
# one sorted array.
#
# The number of elements initialized in nums1 and nums2 are m and n
# respectively. You may assume that nums1 has a size equal to m + n such that
# it has enough space to hold additional elements from nums2.
#
#
# Example 1:
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Example 2:
# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
#
#
# Constraints:
#
#
# nums1.length == m + n
# nums2.length == n
# 0 <= m, n <= 200
# 1 <= m + n <= 200
# -10^9 <= nums1[i], nums2[i] <= 10^9
#
#
#
# Follow up: Can you come up with an algorithm that runs in O(m + n) time?
#

# @lc code=start
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int],
              n: int) -> None:
        """
        Given two sorted integer arrays nums1 and nums2,
        merge nums2 into nums1 as one sorted array.

        The number of elements initialized in nums1 and nums2 are
        m and n respectively.
        nums1 has a size equal to m + n such that it has enough
        space to hold additional elements from nums2.

        :param nums1: The first array of numbers
        :param m: The number of elements initialized in the first array
        :param nums2: The second array of numbers
        :param n: The number of elements initialized in the second array
        """
        if nums1 is None or nums2 is None or len(nums1) < m + n or len(
                nums2) < n:
            return None
        return self.two_pointer(nums1, m, nums2, n)

    def two_pointer(self, nums1: List[int], m: int, nums2: List[int],
                    n: int) -> None:
        """
        Two Pointer Solution
        Build nums1 from the end

        While neither pointers has reached the end
        - Set the position (pt1 + pt2 - 1) to the larger element
        - Decrement the corresponding pointer

        When one of the pointers has reached the end
        - If pt1 > 0
            - Do nothing since nums1 is already sorted
        - If pt2 > 0
            - Copy the entire nums2[:pt2] subarray over to nums1

        Runtime: O(m + n)
        Space: O(1)
        """
        pt1 = m
        pt2 = n
        while pt1 > 0 and pt2 > 0:
            if nums1[pt1 - 1] >= nums2[pt2 - 1]:
                nums1[pt1 + pt2 - 1] = nums1[pt1 - 1]
                pt1 -= 1
            else:
                nums1[pt1 + pt2 - 1] = nums2[pt2 - 1]
                pt2 -= 1
        if pt2 > 0:
            nums1[:pt2] = nums2[:pt2]


# @lc code=end

if __name__ == "__main__":
    # Test Case 1
    input1 = [1, 2, 3, 0, 0, 0]
    m = 3
    input2 = [2, 5, 6]
    n = 3
    expected = [1, 2, 2, 3, 5, 6]
    actual = Solution().merge(input1, m, input2, n)
    print("Test case 1")
    print(input1)
    print(expected)

    # Test Case 2
    input1 = [1]
    m = 1
    input2 = []
    n = 0
    expected = [1]
    actual = Solution().merge(input1, m, input2, n)
    print("Test case 2")
    print(input1)
    print(expected)
