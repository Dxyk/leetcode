from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Given a sorted array nums, remove the duplicates in-place such that
        each element appear only once and return the new length.

        Do not allocate extra space for another array,
        you must do this by modifying the input array in-place with O(1) extra memory.

        NOTE: This question is poorly worded. What they want is for you to make the list such that
        [0, 1, 2, 3, X, X, X, X] or [0, 1, 2, 3] where X are all the duplicated ones

        >>> Solution().removeDuplicates([1, 1, 2])
        2
        >>> Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4])
        5

        :param nums: the original array
        :return: the number of elements in the array without duplicate
        """
        if not nums:
            return 0
        return self.two_pointer(nums)

    def interestion_soln(self, nums: List[int]) -> int:
        """
        T: O(n)
        An interesting soln

        :param nums: the original array
        :return: the number of elements in the array without duplicate
        """
        tail = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[tail]:
                tail += 1
                nums[tail] = nums[i]
        return tail + 1

    def two_pointer(self, nums: List[int]) -> int:
        """
        T: O(n)
        The two pointer solution

        :param nums: the original array
        :return: the number of elements in the array without duplicate
        """
        left = 0
        right = 1
        total = 1
        while right < len(nums):  # loop invariant: nums[:left + 1] is always sorted unique
            if nums[left] != nums[right]:
                left += 1
                nums[left], nums[right] = nums[right], nums[left]
                total += 1
            right += 1
        return total

    def brute_force(self, nums: List[int]) -> int:
        """
        T: O(n)
        The brute force solution

        :param nums: the original array
        :return: the number of elements in the array without duplicate
        """
        prev = None
        total = 0
        while total < len(nums):
            if nums[total] == prev:
                nums.pop(total)
            else:
                prev = nums[total]
                total += 1
        return total
