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
# Note: "aba" is also a valid reswer.
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


class Solution:
    def longestPalindrome(self, s: str) -> str:
        return self.middle_out(s)

    def middle_out(self, s: str) -> str:
        """
        Expand around center to form the palindrome.

        There are (2n - 1) instead of n centers because there exists
        palindromes such as "abba"

        Runtime: O(n^2)
        """
        def expand(left: int, right: int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        if len(s) < 2:
            return s
        start = end = 0
        for i in range(len(s)):
            max_len = max(expand(i, i), expand(i, i + 1))
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        return s[start: end + 1]

    def dp_bottom_up(self, s: str) -> str:
        """
        DP Bottom Up solution

        Runtime: O(n^2)
        """
        res = ""
        max_len = 0
        memo = [[0] * len(s) for _ in range(len(s))]  # n * n matrix
        for i in range(len(s)):
            memo[i][i] = True
            max_len = 1
            res = s[i]
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                memo[i][i + 1] = True
                res = s[i: i + 2]
                max_len = 2
        for j in range(len(s)):
            for i in range(0, j - 1):
                if s[i] == s[j] and memo[i + 1][j - 1]:
                    memo[i][j] = True
                    if max_len < j - i + 1:
                        res = s[i: j + 1]
                        max_len = j - i + 1
        return res

    def dp_recursive(self, s: str) -> str:
        """
        The memo Solution

        Subproblem:
        - The first character of the substring can be either
            - palindrome left
            - palindrome right
            - not in the palindrome
        """
        # TODO: This doesn't work...
        if len(s) < 2:
            return s

        def helper(i: int, j: int) -> bool:
            if i == j:
                return True, s[i]
            elif j == i + 1:
                if s[i] == s[j]:
                    return True, s[i: j + 1]
                else:
                    return False, s[i]
            else:
                is_sub_palindrome, sub_palindrome = helper(i + 1, j - 1)
                if is_sub_palindrome != "" and s[i] == s[j]:
                    return True, s[i] + sub_palindrome + s[j]
                else:
                    return False, sub_palindrome
        return helper(0, len(s) - 1)[1]

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

                # check to see if the current indices match against each other
                # to form a palindrome
                if memo[i][j] > max_common_len:
                    si = i - memo[i][j] + 1
                    sj = j - memo[i][j] + 1
                    if si + j + 1 == len(s) and sj + i + 1 == len(s):
                        max_common_len = memo[i][j]
                        res = s[si: i + 1]
        return res

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
    print(Solution().longestPalindrome("bb"))
    # print(Solution().longestPalindrome("babad"))
    # print(Solution().longestPalindrome("cbbd"))
    # print(Solution().longestPalindrome("bb"))
