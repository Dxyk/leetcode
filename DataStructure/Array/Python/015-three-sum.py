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

        :param nums: the list of all integers
        :return: the list of all three sums that adds up to 0
        """
        result = []
        sorted_nums = sorted(nums)  # O(nlogn)

        for i in range(len(sorted_nums) - 2):
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue
            left_idx, right_idx = i + 1, len(sorted_nums) - 1
            while left_idx < right_idx:
                a, b, c = sorted_nums[i], sorted_nums[left_idx], sorted_nums[right_idx]
                s = a + b + c
                if s == 0:
                    result.append([a, b, c])
                    left_idx += 1
                    right_idx -= 1
                    while left_idx < right_idx and sorted_nums[left_idx] == sorted_nums[left_idx - 1]:
                        left_idx += 1
                    while left_idx < right_idx and sorted_nums[right_idx] == sorted_nums[right_idx - 1]:
                        right_idx -= 1
                elif s < 0:
                    left_idx += 1
                else:
                    right_idx -= 1
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
