#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#
# https://leetcode.com/problems/majority-element/description/
#
# algorithms
# Easy (55.16%)
# Likes:    2284
# Dislikes: 192
# Total Accepted:    481.8K
# Total Submissions: 871.2K
# Testcase Example:  '[3,2,3]'
#
# Given an array of size n, find the majority element. The majority element is
# the element that appears more than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty and the majority element always
# exist in the array.
#
# Example 1:
#
#
# Input: [3,2,3]
# Output: 3
#
# Example 2:
#
#
# Input: [2,2,1,1,1,2,2]
# Output: 2
#
#
#

# @lc code=start
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return self.boyer_moore_voting_soln(nums)

    def boyer_moore_voting_soln(self, nums: List[int]) -> int:
        """
        Boyer-Moore Voting solution

        Idea:
        Set candidate as +1, non-candidate as -1.
        Whenever count becomes 0, switch candidate greedily
        """
        candidate = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == candidate:
                count += 1
            else:
                count -= 1
                if count == 0:
                    candidate = nums[i]
                    count = 1
        return candidate

    def divide_conquer_soln(self, nums: List[int]) -> int:
        """
        Divide and Conquer solution

        Runtime: O(nlogn)
        Space: O(logn)
        """
        def helper(left: int, right: int) -> int:
            if left == right:
                return nums[left]
            mid = (right - left) // 2 + left
            left_maj = helper(left, mid)
            right_maj = helper(mid + 1, right)
            if left_maj == right_maj:
                return left_maj
            left_count = sum([1 for i in range(left, right + 1)
                              if nums[i] == left_maj])
            right_count = sum([1 for i in range(left, right + 1)
                               if nums[i] == right_maj])
            if left_count > right_count:
                return left_maj
            else:
                return right_maj
        return helper(0, len(nums) - 1)

    def randomized_soln(self, nums: List[int]) -> int:
        """
        Randomized solution

        Runtime: O(INF) # average runtime O(1)
        Space: O(1)
        """
        import random
        majority_count = len(nums)//2
        while True:
            candidate = random.choice(nums)
            count = 0
            for num in nums:
                if num == candidate:
                    count += 1
            if count > majority_count:
                return candidate

    def sort_soln(self, nums: List[int]) -> int:
        """
        Sorting solution

        Runtime: O(nlogn)
        Space: O(1)
        """
        sorted_nums = sorted(nums)
        majority_count = len(nums) // 2
        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] != sorted_nums[i - 1]:
                curr_count = 0
            else:
                curr_count += 1
                if curr_count > majority_count:
                    return sorted_nums[i]
        return -1

    def hashmap_soln(self, nums: List[int]) -> int:
        """
        Hashmap solution

        Runtime: O(n)
        Space: O(n)
        """
        majority_count = len(nums) // 2
        counts = dict()
        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
        for num, count in counts.items():
            if count > majority_count:
                return num
# @lc code=end


if __name__ == "__main__":
    print(Solution().majorityElement([3, 2, 3]), 3)
    print(Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]), 2)
