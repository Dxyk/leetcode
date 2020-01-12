#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (51.34%)
# Likes:    2756
# Dislikes: 207
# Total Accepted:    497.3K
# Total Submissions: 963.7K
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# Find the kth largest element in an unsorted array. Note that it is the kth
# largest element in the sorted order, not the kth distinct element.
#
# Example 1:
#
#
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
#
#
# Example 2:
#
#
# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
#
# Note:
# You may assume k is always valid, 1 ≤ k ≤ array's length.
#
#

from typing import List


# @lc code=start


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.partition_soln(nums, k)

    def partition_soln(self, nums: List[int], k: int) -> int:
        """
        Partition solution

        Runtime: O(n)
        Space: O(n)
        """
        def partition(left, right):
            pivot = nums[right]
            lo = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[i], nums[lo] = nums[lo], nums[i]
                    lo += 1
            nums[lo], nums[right] = nums[right], nums[lo]
            return lo
        pos = partition(0, len(nums) - 1)
        if pos > len(nums) - k:
            return self.partition_soln(nums[:pos], k - (len(nums) - pos))
        elif pos < len(nums) - k:
            return self.partition_soln(nums[pos+1:], k)
        else:
            return nums[pos]

    def priority_queue_soln(self, nums: List[int], k: int) -> int:
        """
        Heap solution

        Runtime: O((n+k)log(k))
        Space: O(n)
        """
        import heapq
        heap = []
        for num in nums:  # O(nlogn)
            heapq.heappush(heap, num)
        for _ in range(len(nums)-k):  # O(klogn)
            heapq.heappop(heap)
        return heapq.heappop(heap)

    def sort_soln(self, nums: List[int], k: int) -> int:
        """
        Sort solution

        Runtime: O(nlogn)
        Space: O(n)
        """
        sorted_nums = sorted(nums, reverse=True)
        return sorted_nums[k - 1]


# @lc code=end


if __name__ == "__main__":
    print(Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2), 5)
    print(Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4)
