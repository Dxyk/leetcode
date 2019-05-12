from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        Given an array of integers nums sorted in ascending order, find the starting and ending
        position of a given target value.

        Your algorithm's runtime complexity must be in the order of O(log n).

        If the target is not found in the array, return [-1, -1].

        >>> Solution().searchRange([5,7,7,8,8,10], 8)
        [3, 4]
        >>> Solution().searchRange([5,7,7,8,8,10], 6)
        [-1, -1]

        :param nums: The array of numbers
        :param target: The target value to search for
        :return: the pair of start and end index of the target value. [-1, -1] if target not in nums
        """
        if not nums:
            return [-1, -1]
        return self.brute_force(nums, target)

    def brute_force(self, nums: List[int], target: int) -> List[int]:
        """
        T: O(n)
        The brute force solution

        :param nums: The array of numbers
        :param target: The target value to search for
        :return: the pair of start and end index of the target value. [-1, -1] if target not in nums
        """
        left, right = 0, -1
        while left < len(nums):
            if nums[left] == target:
                right = left
                while right < len(nums) - 1 and nums[right + 1] == target:
                    right += 1
                break
            else:
                left += 1
        return [left, right] if right != -1 else [-1, -1]


if __name__ == '__main__':
    Solution().searchRange([5, 7, 7, 8, 8, 10], 8)
