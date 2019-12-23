#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#
# https://leetcode.com/problems/regular-expression-matching/description/
#
# algorithms
# Hard (25.99%)
# Likes:    3361
# Dislikes: 616
# Total Accepted:    368.3K
# Total Submissions: 1.4M
# Testcase Example:  '"aa"\n"a"'
#
# Given an input string (s) and a pattern (p), implement regular expression
# matching with support for '.' and '*'.
#
#
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
#
#
# The matching should cover the entire input string (not partial).
#
# Note:
#
#
# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like
# . or *.
#
#
# Example 1:
#
#
# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
#
#
# Example 2:
#
#
# Input:
# s = "aa"
# p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore,
# by repeating 'a' once, it becomes "aa".
#
#
# Example 3:
#
#
# Input:
# s = "ab"
# p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
#
#
# Example 4:
#
#
# Input:
# s = "aab"
# p = "c*a*b"
# Output: true
# Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore,
# it matches "aab".
#
#
# Example 5:
#
#
# Input:
# s = "mississippi"
# p = "mis*is*p*."
# Output: false
#
#
#

# @lc code=start


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.dp_bottom_up(s, p)

    def dp_bottom_up(self, s: str, p: str):
        """
        dp bottom-up solution
        """
        memo = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        memo[-1][-1] = True

        for i in range(len(s), -1, -1):
            for j in range(len(p) - 1, -1, -1):
                first_match = i < len(s) and p[j] in {s[i], '.'}

                if j + 1 < len(p) and p[j + 1] == '*':
                    exhausted_match = memo[i][j + 2]
                    unexhausted_match = first_match and memo[i + 1][j]
                    memo[i][j] = exhausted_match or unexhausted_match
                else:
                    memo[i][j] = first_match and memo[i + 1][j + 1]

        return memo[0][0]

    def dp_memoize(self, s: str, p: str) -> bool:
        """
        dp top-down solution

        Subproblem structure:
        Let P(i, j) := True if s[i:] matches with p[j:]

        Then P(i, j) =
        1. s[i:]=""                                 if p[j:]==""
        2. s[i].match and P(i+1, j+1)               if p[1]!="*"
        3. P(i,j+2) or [P(i+1, j) and s[i].match]   if p[1]=="*"
        """
        memo = [[None] * (len(p) + 1) for _ in range(len(s) + 1)]

        def helper(i: int, j: int) -> bool:
            if memo[i][j] is None:
                if j == len(p):
                    res = i == len(s)
                else:
                    first_match = i < len(s) and p[j] in (s[i], ".")

                    if j + 1 < len(p) and p[j + 1] == "*":
                        # Two cases:
                        # 1. ".*" has been exhausted
                        # 2. ".*" has not been exhausted
                        exhausted_match = helper(i, j + 2)
                        unexhausted_match = first_match and helper(i + 1, j)
                        res = exhausted_match or unexhausted_match
                    else:
                        res = first_match and helper(i + 1, j + 1)

                memo[i][j] = res
            return memo[i][j]

        return helper(0, 0)

    def recursive_soln(self, s: str, p: str) -> bool:
        """
        recursive solution
        """
        if p == "":
            return s == ""

        first_match = s != "" and p[0] in (s[0], ".")

        if len(p) >= 2 and p[1] == "*":
            # Two cases:
            # 1. ".*" has been exhausted
            # 2. ".*" has not been exhausted
            exhausted_match = self.recursive_soln(s, p[2:])
            unexhausted_match = first_match and self.recursive_soln(s[1:], p)
            return exhausted_match or unexhausted_match
        else:
            return first_match and self.recursive_soln(s[1:], p[1:])


# @lc code=end


if __name__ == "__main__":
    print(Solution().isMatch("aa", "a"), False)
    print(Solution().isMatch("aa", "a*"), True)
    print(Solution().isMatch("ab", ".*"), True)
    print(Solution().isMatch("ab", ".*c"), False)
    print(Solution().isMatch("aab", "c*a*b*"), True)
    print(Solution().isMatch("mississippi", "mis*is*p*."), False)
