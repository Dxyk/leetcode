from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Given an array nums and a value val, remove all instances of that value in-place and
        return the new length.

        Do not allocate extra space for another array, you must do this by modifying the input array
        in-place with O(1) extra memory.

        The order of elements can be changed. It doesn't matter what you leave beyond the new length

        >>> Solution().removeElement([3, 2, 2, 3], 3)
        2
        >>> Solution().removeElement([0,1,2,2,3,0,4,2], 2)
        5

        :param nums: the original array
        :param val: the value to remove from the array
        :return: the length of the array with val removed
        """
        return self.two_pointer_end_to_center(nums, val)

    def two_pointer_end_to_center(self, nums: List[int], val: int) -> int:
        """
        T: O(n)
        Two pointer solution
        Two pointers go from both end and meet in the middle
        maintain the loop invariant: nums[:left+1] does not contain val

        :param nums: the original array
        :param val: the value to remove from the array
        :return: the length of the array with val removed
        """
        left, right = 0, len(nums)
        while left < right:
            if nums[left] == val:
                nums[left] = nums[right - 1]
                right -= 1
            else:
                left += 1
        return right

    def two_pointer_left_to_right(self, nums: List[int], val: int) -> int:
        """
        T: O(n)
        Two pointer solution
        Both pointers go from left to right, maintaining the loop invariant that
        nums[:left+1] does not contain val

        :param nums: the original array
        :param val: the value to remove from the array
        :return: the length of the array with val removed
        """
        left = 0
        right = 0
        while right < len(nums):  # loop invariant: nums[:left + 1] never contains val
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
            right += 1
        return left

    def python_built_in(self, nums: List[int], val: int) -> int:
        """
        T: O(n)
        Python built in function

        :param nums: the original array
        :param val: the value to remove from the array
        :return: the length of the array with val removed
        """
        while val in nums:
            nums.remove(val)
        return len(nums)

    def brute_force(self, nums: List[int], val: int) -> int:
        """
        T: O(n)
        The brute force solution

        :param nums: the original array
        :param val: the value to remove from the array
        :return: the length of the array with val removed
        """
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
        return i
