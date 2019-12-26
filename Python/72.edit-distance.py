#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#
# https://leetcode.com/problems/edit-distance/description/
#
# algorithms
# Hard (40.50%)
# Likes:    2795
# Dislikes: 44
# Total Accepted:    213.4K
# Total Submissions: 526.3K
# Testcase Example:  '"horse"\n"ros"'
#
# Given two words word1 and word2, find the minimum number of operations
# required to convert word1 to word2.
#
# You have the following 3 operations permitted on a word:
#
#
# Insert a character
# Delete a character
# Replace a character
#
#
# Example 1:
#
#
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation:
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
#
#
# Example 2:
#
#
# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation:
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')
#
#
#

# @lc code=start


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        return self.dp_bottom_up(word1, word2)

    def dp_bottom_up(self, word1: str, word2: str) -> int:
        """
        dp bottom up solution
        """
        memo = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        for i in range(len(word1) + 1):
            memo[i][0] = i
        for j in range(len(word2) + 1):
            memo[0][j] = j

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    memo[i][j] = memo[i - 1][j - 1]
                else:
                    memo[i][j] = 1 + min(memo[i - 1][j],
                                         memo[i][j - 1],
                                         memo[i - 1][j - 1])
        return memo[-1][-1]

    def dp_memoize(self, word1: str, word2: str) -> int:
        """
        dp memoized solution
        """
        memo = [[None] * len(word2) for _ in range(len(word1))]

        def helper(i: int, j: int) -> int:
            if i >= len(word1) and j >= len(word2):
                return 0
            if i >= len(word1) or j >= len(word2):
                return max(len(word1) - i, len(word2) - j)
            if word1[i:] == word2[j:]:
                return 0

            if memo[i][j] is None:
                if word1[i] == word2[j]:
                    return helper(i + 1, j + 1)
                insert = helper(i + 1, j)
                remove = helper(i, j + 1)
                replace = helper(i + 1, j + 1)
                res = 1 + min(insert, remove, replace)
                memo[i][j] = res
            return memo[i][j]

        return helper(0, 0)

    def dp_recursive(self, word1: str, word2: str) -> int:
        """
        DP recursive Solution

        Let P(word1, word2) := min number of moves to match word 1 and word 2

        P(word1, word2) =
        1. 0 if word1 == word2
        2. 1 + min(A, B, C)
            where A = insert a char, B = remove a char, C = replace a char
        """
        def helper(word1: str, word2: str) -> int:
            if word1 == word2:
                return 0
            if word1 == "" or word2 == "":
                return max(len(word1), len(word2))
            if word1[0] == word2[0]:
                return helper(word1[1:], word2[1:])
            insert = helper(word1[1:], word2)
            remove = helper(word1, word2[1:])
            replace = helper(word1[1:], word2[1:])
            return 1 + min(insert, remove, replace)

        return helper(word1, word2)
# @lc code=end


if __name__ == "__main__":
    print(Solution().minDistance("horse", "ros"), 3)
