#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#
# https://leetcode.com/problems/combinations/description/
#
# algorithms
# Medium (57.77%)
# Likes:    2244
# Dislikes: 83
# Total Accepted:    364.8K
# Total Submissions: 625.2K
# Testcase Example:  '4\n2'
#
# Given two integers n and k, return all possible combinations of k numbers out
# of the range [1, n].
#
# You may return the answer in any order.
#
#
# Example 1:
#
#
# Input: n = 4, k = 2
# Output:
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
#
#
# Example 2:
#
#
# Input: n = 1, k = 1
# Output: [[1]]
#
#
#
# Constraints:
#
#
# 1 <= n <= 20
# 1 <= k <= n
#
#
#

# @lc code=start
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n < 1 or k < 1 or n < k:
            return []
        return self.backtrack_iterative_soln(n, k)

    def backtrack_iterative_soln(self, n: int, k: int) -> List[List[int]]:
        """
        Backtrack solution iteratively

        Runtime: O(n^min{k, n-k})

        :param n: The max range to select the combinations from [1, n]
        :param k: The number of elements in the combination
        :return: The list of all possible combinations
        """
        result: List[List[int]] = []
        stack: List[int] = []
        curr_num = 1
        while True:
            length = len(stack)
            if length == k:
                result.append(stack[:])
            if length == k or n - (curr_num - 1) < k - length:
                # explanation for `n - (curr_num - 1) < k - length`
                # - need `k - length` numbers to complete the combination
                # - appending stack in ascending order
                # - there are `n - (curr_num - 1)` numbers left
                # - if condition met, there aren't enough numbers left. backtrack
                if not stack:
                    return result
                curr_num = stack.pop() + 1
            else:
                stack.append(curr_num)
                curr_num += 1

    def dfs_soln(self, n: int, k: int) -> List[List[int]]:
        """
        DFS solution
        Similar idea to backtracking but building the result in place and
        enumerating forward (from 1 to n)

        Runtime: O(n^min{k, n-k})

        :param n: The max range to select the combinations from [1, n]
        :param k: The number of elements in the combination
        :return: The list of all possible combinations
        """
        result: List[List[int]] = []

        def dfs(candidates: List[int], k: int, path: List[int],
                result: List[List[int]]) -> None:
            """DFS helper"""
            if len(path) == k:
                result.append(path)
            else:
                # case 1: candidate not empty, continue
                # case 2: candidate empty, abandon path
                for i in range(len(candidates)):
                    dfs(candidates[i + 1:], k, path + [candidates[i]], result)
            return

        dfs(list(range(1, n + 1)), k, [], result)
        return result

    def backtrack_recursive_soln(self, n: int, k: int) -> List[List[int]]:
        """
        Backtracking solution

        Base case:
        - k = 1
            - Return a list of all [[n], ..., [1]]
        - n = k
            - Return a list of the only combination [[n, ..., 1]]
        Recursive case:
        - Part 1: Curr combinations starting with n
            - Combining n with backtrack(n - 1, k - 1)
        - Part 2: Cases not including n
            - Eleminate n and backtrack(n - 1, k)

        Runtime: O(n^min{k, n-k})

        :param n: The max range to select the combinations from [1, n]
        :param k: The number of elements in the combination
        :return: The list of all possible combinations
        """
        result: List[List[int]] = []
        if k == 1:
            # base case 1
            for i in range(n, 0, -1):
                result.append([i])
        elif n == k:
            # base case 2
            result.append(list(range(n, 0, -1)))
        else:
            # recursive case 1
            n_combinations = self.backtrack_recursive_soln(n - 1, k - 1)
            for n_combination in n_combinations:
                result.append([n] + n_combination)
            # recursive case 2
            result += self.backtrack_recursive_soln(n - 1, k)
        return result


# @lc code=end

if __name__ == "__main__":
    # Test Case 1
    expected = [
        [2, 4],
        [3, 4],
        [2, 3],
        [1, 2],
        [1, 3],
        [1, 4],
    ]
    actual = Solution().combine(4, 2)
    print("Test case 1")
    print(actual)
    print(expected)

    # Test Case 2
    expected = [[1]]
    actual = Solution().combine(1, 1)
    print("Test case 2")
    print(actual)
    print(expected)
