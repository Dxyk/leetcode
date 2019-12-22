#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#
# https://leetcode.com/problems/longest-common-subsequence/description/
#
# algorithms
# Medium (57.59%)
# Likes:    415
# Dislikes: 10
# Total Accepted:    25.8K
# Total Submissions: 44.7K
# Testcase Example:  '"abcde"\n"ace"'
#
# Given two strings text1 and text2, return the length of their longest common
# subsequence.
#
# A subsequence of a string is a new string generated from the original string
# with some characters(can be none) deleted without changing the relative order
# of the remaining characters. (eg, "ace" is a subsequence of "abcde" while
# "aec" is not). A common subsequence of two strings is a subsequence that is
# common to both strings.
#
#
#
# If there is no common subsequence, return 0.
#
#
# Example 1:
#
#
# Input: text1 = "abcde", text2 = "ace"
# Output: 3
# Explanation: The longest common subsequence is "ace" and its length is 3.
#
#
# Example 2:
#
#
# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.
#
#
# Example 3:
#
#
# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.
#
#
#
# Constraints:
#
#
# 1 <= text1.length <= 1000
# 1 <= text2.length <= 1000
# The input strings consist of lowercase English characters only.
#
#
#

# @lc code=start


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.dp_bottom_up(text1, text2)

    def dp_bottom_up(self, text1: str, text2: str) -> int:
        memo = [[0] * (len(text2) + 1) for _ in range((len(text1) + 1))]

        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    memo[i + 1][j + 1] = memo[i][j] + 1
                else:
                    memo[i + 1][j + 1] = max(memo[i + 1][j], memo[i][j + 1])
        return memo[-1][-1]

    def dp_memoize(self, text1: str, text2: str) -> int:
        memo = [[-1] * len(text2) for _ in range(len(text1))]

        def helper(i: int, j: int) -> int:
            if i < 0 or j < 0:
                return 0
            elif memo[i][j] != -1:
                return memo[i][j]
            elif text1[i] == text2[j]:
                res = 1 + helper(i - 1, j - 1)
            else:
                res = max(helper(i - 1, j), helper(i, j - 1))
            memo[i][j] = res
            return res
        return helper(len(text1) - 1, len(text2) - 1)

    def dp_recursive(self, text1: str, text2: str) -> int:
        def helper(i: int, j: int) -> int:
            if i < 0 or j < 0:
                return 0
            elif text1[i] == text2[j]:
                return 1 + helper(i - 1, j - 1)
            else:
                return max(helper(i - 1, j), helper(i, j - 1))

        return helper(len(text1) - 1, len(text2) - 1)
# @lc code=end
