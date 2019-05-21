from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target.
        Return the sum of the three integers. You may assume that each input would have exactly one solution.

        >>> Solution().threeSumClosest([-1, 2, 1, -4], 1)
        2

        :param nums: the list of all integers
        :param target: the target sum
        :return: the closest sum to the target
        """
        if len(nums) < 3:
            return target
        return self.two_pointer_soln(nums, target)

    def two_pointer_soln(self, nums: List[int], target: int) -> int:
        """
        T: O(n^2)
        We fix the left most ptr (i) each time. Use two pointers (left, right) to narrow the interval down based on the sum of the two pointers and i.

        :param nums: the list of all integers
        :param target: the target sum
        :return: the closest sum to the target
        """
        import math

        closest = math.inf
        nums.sort()
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s - target > 0:
                    right -= 1
                elif s - target < 0:
                    left += 1
                else:
                    return target
                closest = s if abs(s - target) < abs(closest - target) else closest
        return closest

    def brute_force(self, nums: List[int], target: int) -> int:
        """
        T: O(n^3)
        need to loop for three times to find all three elements

        :param nums: the list of all integers
        :param target: the target sum
        :return: the closest sum to the target
        """
        import math

        closest = math.inf
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    s = nums[i] + nums[j] + nums[k]
                    closest = s if abs(s - target) < abs(closest - target) else closest
        return closest


def main():
    print(Solution().threeSumClosest([-1, 2, 1, -4], 1))


if __name__ == '__main__':
    main()
