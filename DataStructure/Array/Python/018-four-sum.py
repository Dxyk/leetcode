from typing import Dict, List, Tuple


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target?
        Find all unique quadruplets in the array which gives the sum of target.

        Note:
        The solution set must not contain duplicate quadruplets.

        >>> s = Solution().fourSum([1, 0, -1, 0, -2, 2], 0)
        >>> Solution().sort_results(s)
        [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
        >>> s = Solution().fourSum([-3, -2, -1, 0, 0, 1, 2, 3], 0)
        >>> Solution().sort_results(s)
        [[-3, -2, 2, 3], [-3, -1, 1, 3], [-3, 0, 0, 3], [-3, 0, 1, 2], [-2, -1, 0, 3], [-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
        >>> s = Solution().fourSum([0, 0, 0, 0], 0)
        >>> Solution().sort_results(s)
        [[0, 0, 0, 0]]
        >>> s = Solution().fourSum([-1, -5, -5, -3, 2, 5, 0, 4], -7)
        >>> Solution().sort_results(s)
        [[-5, -5, -1, 4], [-5, -3, -1, 2]]

        :param nums: the array of integers
        :param target: the target sum
        :return: the unique quadruplets that sum up to the target
        """
        if len(nums) < 4:
            return []
        return self.my_soln2(nums, target)

    def induction_soln(self, nums: List[int], target: int) -> List[List[int]]:
        """
        T: O(n^2)

        :param nums: the array of integers
        :param target: the target sum
        :return: the unique quadruplets that sum up to the target
        """
        nums.sort()
        results = []
        self.find_n_sum(nums, target, 4, 0, len(nums) - 1, [], results)
        return results

    def find_n_sum(self, nums: List[int], target: int, N: int, left, right, result: List[int], results: List[List[int]]) -> None:
        """
        T: O()
        find the solution to n sum question (inductive)

        :param nums: the array of integers
        :param target: the target sum
        :param N: N sum question
        :param left: the left index to start with
        :param right: the right index to end with
        :param result: the previous result
        :param results: the list of all possible results
        """
        if right - left + 1 < N or N < 2 or nums[left] * N > target or nums[right] * N < target:  # early termination
            return
        if N == 2:  # two pointers solve sorted 2-sum problem
            while left < right:
                s = nums[left] + nums[right]
                if s == target:
                    results.append(result + [nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif s < target:
                    left += 1
                else:
                    right -= 1
        else:  # recursively reduce N
            for i in range(left, right + 1):
                if i == left or (i > left and nums[i - 1] != nums[i]):
                    self.find_n_sum(nums, target - nums[i], N - 1, i + 1, right, result + [nums[i]], results)

    def solution1(self, nums: List[int], target: int) -> List[List[int]]:
        """
        TODO: T: O(n^2) ??

        :param nums: the array of integers
        :param target: the target sum
        :return: the unique quadruplets that sum up to the target
        """
        # use set to avoid dups
        results_set = set()
        results_list = []

        # 1. store all possible 2 combination's sums to a dict. T: O(n^2)
        # a dict storing all possible sums of all possible pairs
        sum_to_dix: Dict[int, List[Tuple[int, int]]] = dict()
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                curr_sum = nums[i] + nums[j]
                if curr_sum in sum_to_dix:
                    sum_to_dix[curr_sum].append((i, j))
                else:
                    sum_to_dix[curr_sum] = [(i, j)]

        # 2. for each sum in the dict, find the corresponding sum in the dict that adds up to target.
        # TODO: T: O(??)
        for sum1 in sum_to_dix:
            sum2 = target - sum1
            if sum2 in sum_to_dix:
                idxs1 = sum_to_dix[sum1]
                idxs2 = sum_to_dix[sum2]
                for (i1, j1) in idxs1:
                    for (i2, j2) in idxs2:
                        if i1 != i2 and i1 != j2 and j1 != i2 and j1 != j2:
                            res = [nums[i1], nums[j1], nums[i2], nums[j2]]
                            res.sort()
                            results_set.add(tuple(res))  # lists are unhashable so cannot be added to the set

        # 3. turn each tuple in the set to a list and return the list form of the set
        for res_tup in results_set:
            results_list.append(list(res_tup))
        return results_list

    def my_soln2(self, nums: List[int], target: int) -> List[List[int]]:
        """
        T: O(n^3)
        two passes + two pointer + some constraints to make runtime faster

        :param nums: the array of integers
        :param target: the target sum
        :return: the unique quadruplets that sum up to the target
        """
        results = []
        nums.sort()
        for i in range(len(nums) - 3):
            # if the smallest value * 4 is already greater than target, there ain't no way we can get a soln
            if nums[i] * 4 > target:
                break
            if i > 0 and nums[i] == nums[i - 1]:  # already exhausted all possible solutions for this number, skip and avoid dup
                continue

            target2 = target - nums[i]
            for j in range(i + 1, len(nums) - 2):
                if nums[j] * 3 > target2:
                    break
                if j > i + 1 and nums[j] == nums[j - 1]:  # already exhausted all possible solutions for this number, skip and avoid dup
                    continue
                left, right = j + 1, len(nums) - 1
                target3 = target2 - nums[j]
                if nums[left] * 2 > target3 or nums[right] * 2 < target3:
                    # if left * 2 is greater than target, there ain't no way we can get the sum smaller
                    # if right * 2 is smaller than target, there ain't no way we can get the sum larger
                    # NOTE: we do not break here because the next j may be different thus target3 will change
                    continue
                while left < right:
                    s = nums[i] + nums[j] + nums[left] + nums[right]
                    if s < target:
                        left += 1
                    elif s > target:
                        right -= 1
                    else:
                        results.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
        return results

    def my_soln(self, nums: List[int], target: int) -> List[List[int]]:
        """
        T: O(n^3)
        two passes + two pointer

        :param nums: the array of integers
        :param target: the target sum
        :return: the unique quadruplets that sum up to the target
        """
        results = []
        nums.sort()
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:  # already exhausted all possible solutions for this number, skip and avoid dup
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:  # already exhausted all possible solutions for this number, skip and avoid dup
                    continue
                left, right = j + 1, len(nums) - 1
                while left < right:
                    s = nums[i] + nums[j] + nums[left] + nums[right]
                    if s < target:
                        left += 1
                    elif s > target:
                        right -= 1
                    else:
                        results.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
        return results

    def brute_force(self, nums: List[int], target: int) -> List[List[int]]:
        """
        T: O(n^4)

        :param nums: the array of integers
        :param target: the target sum
        :return: the unique quadruplets that sum up to the target
        """
        results = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    for l in range(k + 1, len(nums)):
                        if nums[i] + nums[j] + nums[k] + nums[l] == target:
                            results.append([nums[i], nums[j], nums[k], nums[l]])
        return results

    def sort_results(self, results: List[List[int]]) -> List[List[int]]:
        """
        Sort the results

        :param results: the initial results
        :return: the sorted results
        """
        for result in results:
            result.sort()
        results.sort(key=lambda x: (x[0], x[1], x[2], x[3]))
        return results


def main():
    print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))


if __name__ == '__main__':
    main()
