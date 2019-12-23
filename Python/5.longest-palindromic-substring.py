#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (28.44%)
# Likes:    4964
# Dislikes: 438
# Total Accepted:    743.4K
# Total Submissions: 2.6M
# Testcase Example:  '"babad"'
#
# Given a string s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.
#
# Example 1:
#
#
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
#
#
# Example 2:
#
#
# Input: "cbbd"
# Output: "bb"
#
#
#

# @lc code=start

from typing import List


class Solution:
    def longestPalindrome(self, s: str) -> str:
        return self.brute_force(s)

    def longest_common_substring(self, s: str) -> str:
        """
        Reverse S to get S'. O(n^2)

        The longest common substring between S and S' with the same index 
        is the longest palindrome.

        For implementation, refer to 1143.longest-common-subsequence.py
        """
        # TODO: THIS DOESN'T WORK ON "cddb"
        s_reverse = s[::-1]
        res = ""
        max_common_len = 0
        memo = [[0] * len(s) for _ in range(len(s))]  # len(s) by len(s) matrix
        for i in range(len(s)):
            for j in range(len(s_reverse)):
                if s[i] == s_reverse[j]:
                    memo[i][j] = 1 + memo[i - 1][j - 1]
                else:
                    memo[i][j] = 1

                # check to see if the current indices match against each other to
                # form a palindrome
                if memo[i][j] > max_common_len:
                    si = i - memo[i][j] + 1
                    sj = j - memo[i][j] + 1
                    if si + j + 1 == len(s) and sj + i + 1 == len(s):
                        max_common_len = memo[i][j]
                        res = s[si: i + 1]
        return res

    def dp_soln(self, s: str) -> str:
        """
        The DP Solution

        Subproblem:
        - The first character of the substring can be either 
            - palindrome left
            - palindrome right
            - not in the palindrome
        """
        return self.dp_soln_helper(s, [], "")

    def dp_soln_helper(self, substring: str, palindrome_stack: List[str],
                       curr_tracking: str) -> str:
        if not substring:
            return []
        else:
            if len(palindrome_stack) >= 1 and substring[0] == palindrome_stack[-1]:
                res1 = self.dp_soln_helper(
                    substring[1:], palindrome_stack[:-1], curr_tracking + substring[0])
            if len(palindrome_stack) >= 1 and substring[0] == palindrome_stack[-2]:
                res2 = self.dp_soln_helper(
                    substring[1:], palindrome_stack[: -2], curr_tracking + substring[0])
            res3 = self.dp_soln_helper(
                substring[1:], palindrome_stack[:], curr_tracking)

    def brute_force(self, s: str) -> str:
        """
        The brute force solution

        Runtime: O(n^3)
        """
        if len(s) < 2:
            return s
        res = ""
        for l in range(len(s)):
            for r in range(l + 1, len(s) + 1):
                substring = s[l: r]
                # check palindrome
                mid = len(substring) // 2
                is_palindrome = True
                for i in range(mid + 1):
                    if substring[i] != substring[len(substring) - i - 1]:
                        is_palindrome = False
                        break
                if is_palindrome and len(substring) > len(res):
                    res = substring
        return res

    # @lc code=end

if __name__ == "__main__":
    # print(Solution().longestPalindrome("babad"))
    # print(Solution().longestPalindrome("cbbd"))
    print(Solution().longestPalindrome("bb"))

