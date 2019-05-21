from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        :param nums: the list of all integers
        :return: the list of all three sums that adds up to 0

        Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
        Find all unique triplets in the array which gives the sum of zero.

        Note:
        The solution set must not contain duplicate triplets.

        >>> Solution().check_result([[-1, 0, 1], [-1, -1, 2]], Solution().threeSum([-1, 0, 1, 2, -1, -4]))
        True
        >>> Solution().check_result([[-2,0,2],[-2,1,1]], Solution().threeSum([-2,0,1,1,2]))
        True
        >>> Solution().check_result([[-5,1,4],[-4,0,4],[-4,1,3],[-2,-2,4],[-2,1,1],[0,0,0]], Solution().threeSum([-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]))
        True
        """
        if len(nums) < 3:
            return []
        return self.two_pointer_soln(nums)

    def two_pointer_soln(self, nums: List[int]) -> List[List[int]]:
        """
        T: O(n^2)
        We fix the left most ptr (i) each time. Use two pointers (left, right) to narrow the interval down based on the sum of the two pointers and i.
        Note: there may be multiple solutions corresponding to each i.
        Note: we skip the same numbers to avoid duplicated results

        :param nums: the list of all integers
        :return: the list of all three sums that adds up to 0
        """
        result = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s < 0:
                    left += 1
                elif s > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return result

    def brute_force(self, nums: List[int]) -> List[List[int]]:
        """
        T: O(n^3)
        need to loop for three times to find all three elements

        :param nums: the list of all integers
        :return: the list of all three sums that adds up to 0
        """
        result = []
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    a, b, c = nums[i], nums[j], nums[k]
                    if a + b + c == 0 and not self._already_exists(result, [a, b, c]):
                        result.append([a, b, c])
        return result

    def _already_exists(self, results: List[List[int]], new_result: List[int]) -> bool:
        """
        T: O(nlogn)
        Helper function that determines if the new result already exists in the existing results

        :param results: the list of existing three sums
        :param new_result: the new three sums candidate
        :return: true if the new candidate already exists in the results
        """
        sorted_new_result = sorted(new_result)  # O(nlogn)
        for result in results:
            if sorted(result) == sorted_new_result:
                return True
        return False

    def check_result(self, expected: List[List[int]], actual: List[List[int]]) -> bool:
        """
        Check the results to see if two lists contain the same resulting three sums

        :param actual: the actual list
        :param expected: the expected list
        :return: true if the two lists contain the same elements
        """
        correct = True
        extra, missing = [], []

        for expected_result in expected:
            if not self._already_exists(actual, expected_result):
                missing.append(expected_result)
                correct = False

        for actual_result in actual:
            if not self._already_exists(expected, actual_result):
                extra.append(actual_result)
                correct = False

        if not correct:
            print("expected:", expected)
            print("actual:", actual)
            print("missing:", missing)
            print("extra:", extra)
        return correct


def main():
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))


if __name__ == '__main__':
    main()
