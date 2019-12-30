#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#
# https://leetcode.com/problems/word-break/description/
#
# algorithms
# Medium (37.59%)
# Likes:    3137
# Dislikes: 170
# Total Accepted:    434.3K
# Total Submissions: 1.2M
# Testcase Example:  '"leetcode"\n["leet","code"]'
#
# Given a non-empty string s and a dictionary wordDict containing a list of
# non-empty words, determine if s can be segmented into a space-separated
# sequence of one or more dictionary words.
#
# Note:
#
#
# The same word in the dictionary may be reused multiple times in the
# segmentation.
# You may assume the dictionary does not contain duplicate words.
#
#
# Example 1:
#
#
# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet
# code".
#
#
# Example 2:
#
#
# Input: s = "applepenapple", wordDict = ["apple", "pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple
# pen apple".
# Note that you are allowed to reuse a dictionary word.
#
#
# Example 3:
#
#
# Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output: false
#
#
#

# @lc code=start
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.dp_bottom_up(s, wordDict)

    def dp_bottom_up(self, s: str, wordDict: List[str]) -> bool:
        """
        DP bottom up solution

        Runtime:
        Space:
        """
        memo = [False] * len(s)
        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if s[i:].startswith(word) and \
                        (i + len(word) >= len(s) or memo[i + len(word)]):
                    memo[i] = True
        return memo[0]

    def dp_memoized(self, s: str, wordDict: List[str]) -> bool:
        """
        DP memoized solution

        Runtime:
        Space:
        """
        memo = [None] * len(s)

        def helper(start: int) -> bool:
            if start >= len(s):
                return True
            if memo[start] is None:
                res = False
                for word in wordDict:
                    if s[start:].startswith(word):
                        if helper(start + len(word)):
                            res = True
                            break
                memo[start] = res
            return memo[start]
        return helper(0)

    def dp_recursive_soln(self, s: str, wordDict: List[str]) -> bool:
        """
        DP recursive solution

        Runtime: O(|S| * |WordDict|)
        Space: O(|S| * |WordDict|)
        """
        def helper(start: int) -> bool:
            if start >= len(s):
                return True
            for word in wordDict:
                if s[start:].startswith(word):
                    if helper(start + len(word)):
                        return True
            return False
        return helper(0)
# @lc code=end


if __name__ == "__main__":
    print(Solution().wordBreak("leetcode", ["leet", "code"]), True)
    print(Solution().wordBreak("applepenapple", ["apple", "pen"]), True)
    print(Solution().wordBreak("catsandog",
                               ["cats", "dog", "sand", "and", "cat"]), False)
