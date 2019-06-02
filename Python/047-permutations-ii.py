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

    def dfs_recursive_soln(self, nums: List[int]) -> List[List[int]]:
        """
        The DFS soln

        :param nums: a list of numbers that might contain duplicates
        :return: a list of all permutations
        """
        if not nums:
            return []
        nums.sort()
        ret = [[]]
        for num in nums:
            new_ret = []
            curr_seq_len = len(ret[-1])
            for seq in ret:
                for i in range(curr_seq_len, -1, -1):
                    if i < curr_seq_len and seq[i] == num:
                        break
                    new_ret.append(seq[:i] + [num] + seq[i:])
            ret = new_ret
        return ret

    def dfs(self, nums: List[int], visited: List[bool], path: List[int],
            res: List[List[int]]) -> None:
        """
        The DFS backtracking
        :param nums:
        :param visited:
        :param path:
        :param res:
        :return:
        """
        if len(nums) == len(path):
            res.append(path)
            return
        for i in range(len(nums)):
            if not visited[i]:
                if i > 0 and not visited[i - 1] and nums[i] == nums[i - 1]:
                    continue
                visited[i] = True
                self.dfs(nums, visited, path + [nums[i]], res)
                visited[i] = False


if __name__ == '__main__':
    Solution().permuteUnique([1, 1, 2])
