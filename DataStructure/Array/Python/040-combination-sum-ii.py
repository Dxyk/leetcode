from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Given a collection of candidate numbers (candidates) and a target number (target),
        find all unique combinations in candidates where the candidate numbers sums to target.

        Each number in candidates may only be used once in the combination.

        Note:
        - All numbers (including target) will be positive integers.
        - The solution set must not contain duplicate combinations.

        >>> Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
        [[1, 7], [1, 2, 5], [2, 6], [1, 1, 6]]
        >>> Solution().combinationSum2([2, 5, 2, 1, 2], 5)
        [[1, 2, 2], [5]]

        :param candidates: the list of candidate numbers
        :param target: the target sum
        :return: all unique combinations of candidates to sum up to target
        """
        if not candidates or target <= 0:
            return []
        candidates.sort()
        results = []
        self.depth_first_search(candidates, 0, [], results, target)
        return results

    def depth_first_search(self, candidates: List[int], start: int, path: List[int],
                           result: List[List[int]], target: int) -> None:
        """
        The recursive depth first search solution

        :param candidates: the list of all candidates
        :param start: the starting index
        :param path: the current search path
        :param result: the result set
        :param target: the target value
        :return: None
        """
        if not target:
            result.append(path)
            return

        for i in range(start, len(candidates)):
            # because each recursive call we're incrementing start by 1, we skip i+1 if it's the
            # same as i, since we'll cover that in the recursive call in i. Preventing over-counting
            if i > start and candidates[i] == candidates[i - 1]:
                continue

            if candidates[i] > target:
                break

            # We change the start to `i + 1` because one element only could
            # be used once
            self.depth_first_search(candidates, i + 1, path + [candidates[i]],
                                    result, target - candidates[i])


if __name__ == '__main__':
    print(Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
