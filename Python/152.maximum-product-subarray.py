#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#
# https://leetcode.com/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (30.50%)
# Likes:    2944
# Dislikes: 128
# Total Accepted:    270.4K
# Total Submissions: 885K
# Testcase Example:  '[2,3,-2,4]'
#
# Given an integer array nums, find the contiguous subarray within an array
# (containing at least one number) which has the largest product.
#
# Example 1:
#
#
# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
#
#
# Example 2:
#
#
# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
#
#

# @lc code=start
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        return self.dp_bottom_up_soln(nums)

    def dp_bottom_up_soln(self, nums: List[int]) -> int:
        """
        DP bottom up solution

        Runtime: O(n)
        Space: O(1)
        """
        res = nums[0]
        curr_max = res
        curr_min = res
        for i in range(1, len(nums)):
            curr = nums[i]
            if curr < 0:
                curr_max, curr_min = curr_min, curr_max
            curr_max = max(curr, curr_max * curr)
            curr_min = min(curr, curr_min * curr)
            res = max(curr_max, res)
        return res

    def dp_memoized_1d_soln(self, nums: List[int]) -> int:
        """
        DP memoized solution

        Space: MLE
        """
        # 1d memo that stores [curr_max, curr_min]
        memo = [None] * len(nums)

        def helper(i: int) -> int:
            if i < 0 or i > len(nums):
                return [-float("inf"), float("inf")]
            if memo[i] is None:
                if i == 0:
                    res = [nums[i]] * 2
                else:
                    curr_max, curr_min = helper(i - 1)
                    if nums[i] < 0:
                        curr_max, curr_min = curr_min, curr_max
                    curr_max = max(nums[i], curr_max * nums[i])
                    curr_min = min(nums[i], curr_min * nums[i])
                    res = [curr_max, curr_min]
                memo[i] = res
            return memo[i]

        helper(len(nums) - 1)
        return max([curr[0] for curr in memo])

    def dp_memoized_2d_soln(self, nums: List[int]) -> int:
        """
        DP memoized solution

        Space: MLE
        """
        product_memo = [[None] * len(nums) for _ in range(len(nums))]

        def get_product(i: int, j: int) -> int:
            if i > j or i < 0 or j > len(nums):
                return [-float("inf")] * 3
            if product_memo[i][j] is None:
                if i == j:
                    res = [nums[i], -float("inf"), -float("inf")]
                else:
                    no_left_max = max(get_product(i + 1, j))
                    no_right_max = max(get_product(i, j - 1))
                    curr = nums[i] * get_product(i + 1, j)[0]
                    res = [curr, no_left_max, no_right_max]
                product_memo[i][j] = res
            return product_memo[i][j]

        return max(get_product(0, len(nums) - 1))

    def dp_recursive_soln(self, nums: List[int]) -> int:
        """
        DP recursive solution

        Subproblem Structure:
        Let P(i, j) := the maximum product of subarray from idx i to j
        Then P(i, j) =
            nums[i] if i == j
            max(P(i + 1, j), P(i, j - 1)) otherwise

        Runtime: TLE
        """
        def helper(i: int, j: int) -> int:
            if i == j:
                return nums[i]
            else:
                curr_product = 1
                for k in range(i, j + 1):
                    curr_product *= nums[k]
                return max(curr_product, helper(i + 1, j), helper(i, j - 1))
        return helper(0, len(nums) - 1)
# @lc code=end


if __name__ == "__main__":
    print(Solution().maxProduct([-2, -3, 1, -4]), 12)
    print(Solution().maxProduct([-2, 3, 1, -4]), 24)
    print(Solution().maxProduct([2, 3, -1, 4]), 6)
    print(Solution().maxProduct([-2, 0, -1]), 0)
    print(Solution().maxProduct([-2]), -2)
    print(Solution().maxProduct([0, -2]), 0)
    print(Solution().maxProduct([0, 2]), 2)
