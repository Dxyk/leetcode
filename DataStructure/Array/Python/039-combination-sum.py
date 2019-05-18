from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Given a set of candidate numbers (candidates) (without duplicates) and
        a target number (target), find all unique combinations in candidates where
        the candidate numbers sums to target.

        The same repeated number may be chosen from candidates unlimited number of times.

        Note:
        - All numbers (including target) will be positive integers.
        - The solution set must not contain duplicate combinations.

        >>> Solution().combinationSum([2, 3, 6, 7], 7)
        [[7], [2, 2, 3]]
        >>> Solution().combinationSum([2, 3, 5], 8)
        [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

        :param candidates: the list of candidate numbers
        :param target: the target sum
        :return: all unique combinations of candidates to sum up to target
        """
        if not candidates or target <= 0:
            return []
        return self.depth_first_search(candidates, target)

    def depth_first_search(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        T: O()
        The depth first search solution

        :param candidates: the list of candidate numbers
        :param target: the target sum
        :return: all unique combinations of candidates to sum up to target
        """
        stack = []
        results = []
        for candidate in candidates:
            stack.append([candidate])
        while stack:
            curr_combination = stack.pop()
            curr_sum = sum(curr_combination)
            if curr_sum == target:
                results.append(curr_combination)
            elif curr_sum < target:
                for candidate in candidates:
                    if candidate <= curr_combination[-1]:
                        stack.append(curr_combination + [candidate])
        return results




if __name__ == '__main__':
    print(Solution().combinationSum([2, 3, 6, 7], 7))
