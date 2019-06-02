from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Given a collection of distinct integers, return all possible permutations.

        >>> Solution().permute([1, 2, 3])
        [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

        :param nums: A collection of distinct integers
        :return: All possible permutations
        """
        if not nums:
            return []
        return self.dfs_stack_soln(nums)

    def dfs_recursive_soln(self, nums: List[int]) -> List[List[int]]:
        """
        T: O()
        The dfs recursive soln

        :param nums: A collection of distinct integers
        :return: All possible permutations
        """
        res = []
        self.dfs_recursive(nums, [], res)
        return res

    def dfs_recursive(self, nums: List[int], path: List[int], res: List[List[int]]) -> None:
        """
        Recursively add paths to res

        :param nums: The numbers
        :param path: The current path
        :param res: the list of results
        :return: None
        """
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            self.dfs_recursive(nums[:i] + nums[i + 1:], path + [nums[i]], res)

    def dfs_stack_soln(self, nums: List[int]) -> List[List[int]]:
        """
        T: O()
        The dfs stack soln

        :param nums: A collection of distinct integers
        :return: All possible permutations
        """
        res = []
        stack = [[i] for i in range(len(nums))]
        while stack:
            curr_indices = stack.pop()
            if len(curr_indices) == len(nums):
                res.append([nums[i] for i in curr_indices])
            else:
                for i in range(len(nums)):
                    if i not in curr_indices:
                        stack.append(curr_indices + [i])
        return res

    def swap_soln(self, nums: List[int]) -> List[List[int]]:
        """
        Swap unique pairs of numbers

        :param nums: A collection of distinct integers
        :return: All possible permutations
        """
        ans = [nums[:]]
        for i in range(1, len(nums)):
            for k in range(len(ans)):
                for j in range(i):
                    ans.append(ans[k][:])
                    ans[-1][j], ans[-1][i] = ans[-1][i], ans[-1][j]
        return ans


if __name__ == '__main__':
    Solution().permute([1, 2, 3])
