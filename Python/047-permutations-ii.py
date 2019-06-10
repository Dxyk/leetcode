from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        Given a collection of numbers that might contain duplicates,
        return all possible unique permutations.

        >>> Solution().permuteUnique([1, 1, 2])
        [[1, 1, 2], [1, 2, 1], [2, 1, 1]]

        :param nums: a list of numbers that might contain duplicates
        :return: a list of all permutations
        """
        if not nums:
            return []
        return self.dfs_recursive_soln(nums)

    def dfs_iterative_soln(self, nums: List[int]) -> List[List[int]]:
        """
        The DFS soln

        :param nums: a list of numbers that might contain duplicates
        :return: a list of all permutations
        """
        if not nums:
            return []
        # O(n*log(n))
        nums.sort()
        results = [[]]
        for num in nums:
            curr_results = []
            curr_seq_len = len(results[-1])
            for res in results:
                for i in range(curr_seq_len, -1, -1):
                    if i < curr_seq_len and res[i] == num:
                        break
                    curr_results.append(res[:i] + [num] + res[i:])
            results = curr_results
        return results

    def dfs_recursive_soln(self, nums: List[int]) -> List[List[int]]:
        """
        The DFS recursive soln

        :param nums: a list of numbers that might contain duplicates
        :return: a list of all permutations
        """
        res = []
        nums.sort()
        self.dfs_recursive(nums, [], res)
        return res

    def dfs_recursive(self, nums: List[int], path: List[int],
                      res: List[List[int]]) -> None:
        """
        The DFS recursive helper given the numbers are sorted

        :param nums: the list of numbers
        :param path: the current path
        :param res: the result
        :return: None
        """
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.dfs_recursive(nums[:i] + nums[i + 1:], path + [nums[i]], res)


if __name__ == '__main__':
    Solution().permuteUnique([1, 2, 1, 1, 1])
