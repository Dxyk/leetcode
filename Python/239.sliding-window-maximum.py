#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#
# https://leetcode.com/problems/sliding-window-maximum/description/
#
# algorithms
# Hard (40.21%)
# Likes:    2490
# Dislikes: 145
# Total Accepted:    216.2K
# Total Submissions: 533.4K
# Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
#
# Given an array nums, there is a sliding window of size k which is moving from
# the very left of the array to the very right. You can only see the k numbers
# in the window. Each time the sliding window moves right by one position.
# Return the max sliding window.
#
# Example:
#
#
# Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
# Output: [3,3,5,5,6,7]
# Explanation:
#
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
# ⁠1 [3  -1  -3] 5  3  6  7       3
# ⁠1  3 [-1  -3  5] 3  6  7       5
# ⁠1  3  -1 [-3  5  3] 6  7       5
# ⁠1  3  -1  -3 [5  3  6] 7       6
# ⁠1  3  -1  -3  5 [3  6  7]      7
#
#
# Note:
# You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty
# array.
#
# Follow up:
# Could you solve it in linear time?
#

from typing import List

# @lc code=start

from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        return self.dequeue_soln(nums, k)

    def dequeue_soln(self, nums: List[int], k: int) -> List[int]:
        """
        Dequeue solution

        Runtime: O(nk)
        Space: O(1)
        """
        if len(nums) == 0:
            return []
        if k == 0:
            return nums
        dq = deque()
        result = []

        # find and append the maximum idx
        for i in range(k):
            while len(dq) != 0:
                if nums[i] > nums[dq[-1]]:
                    dq.pop()
                else:
                    break

            dq.append(i)

        for i in range(k, len(nums)):
            result.append(nums[dq[0]])
            if dq[0] < i - k + 1:
                dq.popleft()
            while len(dq) != 0:
                if nums[i] > nums[dq[-1]]:
                    dq.pop()
                else:
                    break
            dq.append(i)

        result.append(nums[dq[0]])

        return result

    def bf_soln(self, nums: List[int], k: int) -> List[int]:
        """
        BF solution

        Loop through the list and find each max in the window

        Runtime: O(nk)
        Space: O(1)
        """
        if len(nums) == 0 or len(nums) < k:
            return []
        res = []
        for i in range(k, len(nums) + 1):
            res.append(max(nums[i - k: i]))
        return res
# @lc code=end


if __name__ == "__main__":
    print(Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
    print([3, 3, 5, 5, 6, 7])
