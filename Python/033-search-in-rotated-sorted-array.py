from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Suppose an array sorted in ascending order is rotated at some pivot unknown to you
        beforehand.
        You are given a target value to search.
        If found in the array return its index, otherwise return -1.

        (i.e., [0, 1, 2, 4, 5, 6, 7] might become [4, 5, 6, 7, 0, 1, 2]).

        You may assume no duplicate exists in the array.

        Your algorithm's runtime complexity must be in the order of O(log n).

        >>> Solution().search([4, 5, 6, 7, 0, 1, 2], 0)
        4
        >>> Solution().search([4, 5, 6, 7, 0, 1, 2], 3)
        -1
        >>> Solution().search([], 3)
        -1
        >>> Solution().search([2, 1], 1)
        1
        >>> Solution().search([5, 7, 9, 1, 3], 3)
        4
        >>> Solution().search([5, 7, 9, 1, 3], 2)
        -1
        >>> Solution().search([7, 8, 1, 2, 3, 4, 5, 6], 2)
        3

        :param nums: the array of numbers
        :param target: the target to search for
        :return: the index of target or -1 if the target does not exist in nums
        """
        if not nums:
            return -1
        return self.binary_search(nums, target)

    def binary_search(self, nums: List[int], target: int) -> int:
        """
        T: O(logn)

        :param nums: the array of numbers
        :param target: the target to search for
        :return: the index of target or -1 if the target does not exist in nums
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                # nums[left:mid] is in order
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # nums[left:mid] is not in order
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

    def brute_force(self, nums: List[int], target: int) -> int:
        """
        T: O(n)
        The brute force solution

        :param nums: the array of numbers
        :param target: the target to search for
        :return: the index of target or -1 if the target does not exist in nums
        """
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1


if __name__ == '__main__':
    print(Solution().search([7, 8, 1, 2, 3, 4, 5, 6], 2))
