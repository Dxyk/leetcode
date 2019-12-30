#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#
# https://leetcode.com/problems/longest-consecutive-sequence/description/
#
# algorithms
# Hard (43.35%)
# Likes:    2450
# Dislikes: 140
# Total Accepted:    250.3K
# Total Submissions: 576.5K
# Testcase Example:  '[100,4,200,1,3,2]'
#
# Given an unsorted array of integers, find the length of the longest
# consecutive elements sequence.
#
# Your algorithm should run in O(n) complexity.
#
# Example:
#
#
# Input: [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
# Therefore its length is 4.
#
#
#

# @lc code=start
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        return self.set_soln(nums)

    def set_soln(self, nums):
        """
        Use HashSet and intelligent sequence building

        Runtime: O(n)
        Space: O(n)
        """
        res = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:  # O(1)
                curr = num
                curr_res = 1
                while curr + 1 in num_set:  # O(1)
                    curr += 1
                    curr_res += 1
                res = max(res, curr_res)

        return res

    def union_find_soln(self, nums: List[int]) -> int:
        """
        Union Find solution

        Runtime: O(n)
        Space: O(n)
        """
        nums = list(set(nums))
        idx_lookup = {v: i for i, v in enumerate(nums)}
        roots = [nums[i] for i in range(len(nums))]
        sizes = [1] * len(nums)

        def find(num: int) -> int:
            root = num
            num_idx = root_idx = idx_lookup.get(root)
            if num_idx is None:
                return None
            while root != roots[root_idx]:
                root = roots[root_idx]
                root_idx = idx_lookup[root]
            while num != root:
                temp = roots[num_idx]
                roots[num_idx] = root
                num = temp
                num_idx = idx_lookup[num]
            return root

        def union(num1: int, num2: int) -> None:
            root1 = find(num1)
            root2 = find(num2)
            root1_idx = idx_lookup[root1]
            root2_idx = idx_lookup[root2]
            if root1 == root2:
                return
            if sizes[root1_idx] < sizes[root2_idx]:
                roots[root1_idx] = root2
                sizes[root2_idx] += sizes[root1_idx]
            else:
                roots[root2_idx] = root1
                sizes[root1_idx] += sizes[root2_idx]
            return

        for num in nums:
            if find(num - 1) is not None:
                union(num - 1, num)
            if find(num + 1) is not None:
                union(num + 1, num)

        return 0 if len(sizes) == 0 else max(sizes)

    def sort_soln(self, nums: List[int]) -> int:
        """
        Sort solution

        Runtime: O(nlog(n))
        Space: O(n)
        """
        if len(nums) < 2:
            return len(nums)
        sorted_nums = sorted(nums)
        res = 0
        curr_res = 1
        for i in range(1, len(nums)):
            if sorted_nums[i] != sorted_nums[i - 1]:
                if sorted_nums[i] == sorted_nums[i - 1] + 1:
                    curr_res += 1
                else:
                    res = max(curr_res, res)
                    curr_res = 1
        return max(curr_res, res)

    def bf_soln(self, nums: List[int]) -> int:
        """
        Brute Force solution

        Runtime: O(n^3)
        Space: O(1)
        """
        res = 0
        for num in nums:
            curr = num
            curr_res = 1
            while curr + 1 in nums:
                curr += 1
                curr_res += 1
            res = max(res, curr_res)
        return res
# @lc code=end


if __name__ == "__main__":
    print(Solution().longestConsecutive([0]), 1)
    print(Solution().longestConsecutive([0, -1]), 2)
    print(Solution().longestConsecutive([0, 0, -1]), 2)
    print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]), 4)
