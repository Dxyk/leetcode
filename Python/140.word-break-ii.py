#
# @lc app=leetcode id=140 lang=python3
#
# [140] Word Break II
#
# https://leetcode.com/problems/word-break-ii/description/
#
# algorithms
# Hard (29.06%)
# Likes:    1355
# Dislikes: 302
# Total Accepted:    190.4K
# Total Submissions: 653.8K
# Testcase Example:  '"catsanddog"\n["cat","cats","and","sand","dog"]'
#
# Given a non-empty string s and a dictionary wordDict containing a list of
# non-empty words, add spaces in s to construct a sentence where each word is a
# valid dictionary word. Return all such possible sentences.
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
# Input:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# Output:
# [
# "cats and dog",
# "cat sand dog"
# ]
#
#
# Example 2:
#
#
# Input:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# Output:
# [
# "pine apple pen apple",
# "pineapple pen apple",
# "pine applepen apple"
# ]
# Explanation: Note that you are allowed to reuse a dictionary word.
#
#
# Example 3:
#
#
# Input:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output:
# []
#
#

# @lc code=start
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        return self.dp_memoized(s, wordDict)

    def dp_memoized(self, s: str, wordDict: List[str]) -> List[str]:
        """
        DP memoized solution

        Runtime:
        Space:
        """
        # Large word dict is the reason why the runtime might be slow.
        # Tuse we use a hashset to mitigate this
        word_dict_set = set(wordDict)
        memo = {len(s): [""]}

        def helper(i):
            if i not in memo:
                memo[i] = []
                for j in range(i + 1, len(s) + 1):
                    if s[i: j] in word_dict_set:
                        for tail in helper(j):
                            if tail != "":
                                memo[i].append(s[i:j] + " " + tail)
                            else:
                                memo[i].append(s[i:j])
            return memo[i]
        return helper(0)

    def dp_recursive_soln(self, s: str, wordDict: List[str]) -> List[str]:
        """
        DP recursive solution
        """
        res = []

        def helper(start: int, curr_res: str) -> bool:
            if start >= len(s):
                if curr_res != "":
                    res.append(curr_res)
                return True
            found = False
            for word in wordDict:
                if s[start:].startswith(word):
                    if curr_res != "":
                        new_curr_res = curr_res + " " + word
                    else:
                        new_curr_res = word
                    if helper(start + len(word), new_curr_res):
                        found = True
            return found
        helper(0, "")
        return res
# @lc code=end


if __name__ == "__main__":
    print(Solution().wordBreak("catsanddog",
                               ["cat", "cats", "and", "sand", "dog"]))
    print(["cats and dog", "cat sand dog"])

    print(Solution().wordBreak("pineapplepenapple",
                               ["apple", "pen", "applepen", "pine",
                                "pineapple"]))
    print(["pine apple pen apple", "pineapple pen apple",
           "pine applepen apple"])

    print(Solution().wordBreak("catsandog",
                               ["cats", "dog", "sand", "and", "cat"]))
    print([])
