from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        Given an array of integers nums sorted in ascending order, find the starting and ending
        position of a given target value.

        Your algorithm's runtime complexity must be in the order of O(log n).

        If the target is not found in the array, return [-1, -1].

        >>> Solution().searchRange([], 1)
        [-1, -1]
        >>> Solution().searchRange([1], 1)
        [0, 0]
        >>> Solution().searchRange([1], 0)
        [-1, -1]
        >>> Solution().searchRange([2, 2], 3)
        [-1, -1]
        >>> Solution().searchRange([1, 2, 3], 3)
        [2, 2]
        >>> Solution().searchRange([1, 1, 1, 1, 1], 1)
        [0, 4]
        >>> Solution().searchRange([5, 7, 7, 8, 8, 10], 8)
        [3, 4]
        >>> Solution().searchRange([5, 7, 7, 8, 8, 10], 6)
        [-1, -1]

        :param nums: The array of numbers
        :param target: The target value to search for
        :return: the pair of start and end index of the target value. [-1, -1] if target not in nums
        """
        if not nums:
            return [-1, -1]
        return self.binary_search_soln(nums, target)

    def binary_search_soln(self, nums: List[int], target: int) -> List[int]:
        """
        T: O(log(n))
        The brute force solution

        :param nums: The array of numbers
        :param target: The target value to search for
        :return: the pair of start and end index of the target value. [-1, -1] if target not in nums
        """
        idx = self.binary_search(nums, target)
        if idx == -1:
            return [-1, -1]
        else:
            left = right = idx
            while left > 0 and nums[left - 1] == target:
                new_left = self.binary_search(nums[: left], target)
                if new_left != -1:
                    left = new_left
                else:
                    break
            while right < len(nums) - 1 and nums[right + 1] == target:
                new_right = self.binary_search(nums[right:], target)
                if new_right != -1:
                    right += new_right
                else:
                    break
            return [left, right]

    def binary_search(self, nums: List[int], target: int) -> int:
        """
        T: O(log(n))
        
        :param nums: The array of numbers
        :param target: The target value to search for
        :return: the index of the target value
        """
        if not nums or (len(nums) == 1 and nums[0] != target):
            return -1
        mid = len(nums) // 2
        if nums[mid] == target:
            return mid
        else:
            if target < nums[mid]:
                return self.binary_search(nums[: mid], target)
            else:
                idx = self.binary_search(nums[mid + 1:], target)
                return mid + idx + 1 if idx != -1 else -1

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
    print(Solution().searchRange([1, 2, 3], 3))
