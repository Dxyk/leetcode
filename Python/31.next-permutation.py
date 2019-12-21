from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Implement next permutation, which rearranges numbers into the lexicographically next greater
        permutation of numbers.

        If such arrangement is not possible, it must rearrange it as the lowest possible order
        (ie, sorted in ascending order).

        Note: The replacement must be in-place and use only constant extra memory.

        n: len(nums)

        >>> lst = [1, 2, 3]; Solution().nextPermutation(lst); lst
        [1, 3, 2]
        >>> lst = [3, 2, 1]; Solution().nextPermutation(lst); lst
        [1, 2, 3]
        >>> lst = [1, 1, 5]; Solution().nextPermutation(lst); lst
        [1, 5, 1]
        >>> lst = [1, 2, 4, 3]; Solution().nextPermutation(lst); lst
        [1, 3, 2, 4]
        >>> lst = [4, 3, 1, 2, 5]; Solution().nextPermutation(lst); lst
        [4, 3, 1, 5, 2]
        >>> lst = [1, 3, 2]; Solution().nextPermutation(lst); lst
        [2, 1, 3]
        >>> lst = [1, 5, 4, 3]; Solution().nextPermutation(lst); lst
        [3, 1, 4, 5]

        :param nums: the list of numbers
        :return: None
        """
        if not nums:
            return
        return self.list_swap(nums)

    def list_swap(self, nums: List[int]) -> None:
        """
        T: O(n)

        For an array of numbers to be at its largest permutation, it must be in descending order.
        For an array of numbers to be at its smallest permutation, it must be in ascending order

        Case 1:
        Find the right most idx i such that nums[i] < nums[i + 1]. Then nums[i + 1:] is in
        descending order, so we rearrange nums[i:] to find a larger permutation.

        To rearrange nums[i:], find the nums[j] in nums[i + 1:] that is just larger than nums[i],
        and swap nums[i] with nums[j]. This way, the new nums[i:] is larger than the old nums[i:].

        However, this is not the next greater value. To rearrange the array to produce the minimum
        greater permutation, we need nums[i + 1:] to be in ascending order.
        Note:
        - nums[i + 1:] is in descending order
        - swapping nums[i] and nums[j] does not break the descending order because nums[j] is the
          next larger element of nums[i].

        Thus the new nums[i + 1:] is in descending order.

        Thus we just reverse nums[i + 1:]

        Case 2:
        If for all i < j, nums[i] >= nums[j], then there is no next larger combination, so we simply
        reverse the list.

        :param nums: the list of numbers
        :return: None
        """
        left = len(nums) - 2
        while left >= 0 and nums[left + 1] <= nums[left]:  # O(n)
            left -= 1
        if left >= 0:
            right = len(nums) - 1
            while right >= left and nums[right] <= nums[left]:  # O(n)
                right -= 1
            nums[left], nums[right] = nums[right], nums[left]
        self._reverse(nums, left + 1)

    def _reverse(self, nums: List[int], start: int) -> None:
        """
        T: O(n)
        Reverse a list of numbers in place starting at the start index

        :param nums: the list of numbers
        :param start: the starting index
        :return: None
        """
        left, right = start, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    def brute_force(self, nums: List[int]) -> None:
        """
        T: O(n!)
        The brute force solution

        :param nums: the list of numbers
        :return: None
        """
        import itertools
        import math

        orig_val, min_val = self._get_value(nums), math.inf
        min_perm = nums
        for perm in itertools.permutations(nums):  # O(n!)
            curr_val = self._get_value(list(perm))  # O(n)
            if curr_val > orig_val:
                if curr_val <= min_val:
                    min_val = curr_val
                    min_perm = list(perm)
        if min_perm == nums:
            min_perm.sort()
        for i in range(len(nums)):
            nums[i] = min_perm[i]

    def _get_value(self, nums: List[int]) -> int:
        """
        T: O(n)
        Helper method that gets the value of the given list

        :param nums: the list of numbers
        :return: the value of the list
        """
        curr_num = 0
        reversed_nums = nums[::-1]  # O(n)
        for i in range(len(reversed_nums)):  # O(n)
            curr_num += reversed_nums[i] * (10 ** i)
        return curr_num


if __name__ == '__main__':
    lst = [1, 3, 2]
    Solution().nextPermutation(lst)
    print(lst)
