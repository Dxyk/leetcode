from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Given a sorted array and a target value, return the index if the target is found.
        If not, return the index where it would be if it were inserted in order.

        You may assume no duplicates in the array.

        >>> Solution().searchInsert([1], 1)
        0
        >>> Solution().searchInsert([1, 3, 5, 6], 5)
        2
        >>> Solution().searchInsert([1, 3, 5, 6], 2)
        1
        >>> Solution().searchInsert([1, 3, 5, 6], 7)
        4
        >>> Solution().searchInsert([1, 3, 5, 6], 0)
        0
        >>> Solution().searchInsert([1, 3, 5], 4)
        2

        :param nums: the list of sorted numbers
        :param target: the target number to insert into nums
        :return: the index of the target if the target is in nums, else the idx where it would be
        """
        return self.binary_search(nums, target)

    def binary_search(self, nums: List[int], target: int) -> int:
        """
        T: O(n)
        Binary Search Soln

        :param nums: the list of sorted numbers
        :param target: the target number to insert into nums
        :return: the index of the target if the target is in nums, else the idx where it would be
        """
        if target < nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = mid - 1
                if right >= 0:
                    if target > nums[right]:
                        return right + 1
                else:
                    return 0
            else:
                left = mid + 1
                if left < len(nums):
                    if target < nums[left]:
                        return left
                else:
                    return len(nums)

    def brute_force(self, nums: List[int], target: int) -> int:
        """
        T: O(n)
        The brute force solution

        :param nums: the list of sorted numbers
        :param target: the target number to insert into nums
        :return: the index of the target if the target is in nums, else the idx where it would be
        """
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            if i < len(nums) - 1:
                if nums[i] < target < nums[i + 1]:
                    return i + 1
        if target < nums[0]:
            return 0
        else:
            return len(nums)


if __name__ == '__main__':
    print(Solution().searchInsert([1, 3, 5, 6], 5))
