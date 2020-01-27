#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#
# https://leetcode.com/problems/product-of-array-except-self/description/
#
# algorithms
# Medium (57.78%)
# Likes:    3435
# Dislikes: 296
# Total Accepted:    372.3K
# Total Submissions: 639.4K
# Testcase Example:  '[1,2,3,4]'
#
# Given an array nums of n integers where n > 1,  return an array output such
# that output[i] is equal to the product of all the elements of nums except
# nums[i].
#
# Example:
#
#
# Input:  [1,2,3,4]
# Output: [24,12,8,6]
#
#
# Note: Please solve it without division and in O(n).
#
# Follow up:
# Could you solve it with constant space complexity? (The output array does not
# count as extra space for the purpose of space complexity analysis.)
#
#

from typing import List

# @lc code=start


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return self.left_right_improved_soln(nums)

    def left_right_improved_soln(self, nums: List[int]) -> List[int]:
        """
        Left Right Solution

        Same algorithm as left right solution, but build res from as left_prod.
        Keep right_prod as a number and calculate product with res in second
        pass

        Runtime: O(n)
        Space: O(1)
        """
        res = [1] * len(nums)
        for i in range(1, len(nums)):
            res[i] = nums[i - 1] * res[i - 1]

        right_prod = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] = res[i] * right_prod
            right_prod *= nums[i]

        return res

    def left_right_soln(self, nums: List[int]) -> List[int]:
        """
        Left Right Solution

        Note that the product of the list excluding the element at index i can
        be seen as the product of the list to the left of the element times the
        product of the elements to the right of the element.

        Runtime: O(n)
        Space: O(n)
        """
        left_prod = [1] * len(nums)
        right_prod = [1] * len(nums)
        res = [1] * len(nums)

        for i in range(1, len(nums)):
            left_prod[i] = nums[i - 1] * left_prod[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            right_prod[i] = nums[i + 1] * right_prod[i + 1]

        for i in range(len(nums)):
            res[i] = left_prod[i] * right_prod[i]
        return res

    def division_soln(self, nums: List[int]) -> List[int]:
        """
        Division Solution

        Runtime: O(n)
        Space: O(1)
        """
        res = []
        total_sum = 1
        for num in nums:
            total_sum *= num
        for num in nums:
            res.append(total_sum // num)
        return res
# @lc code=end


if __name__ == "__main__":
    print(Solution().productExceptSelf([1, 2, 3, 4]), [24, 12, 8, 6])
