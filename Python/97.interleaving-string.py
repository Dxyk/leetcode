#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#
# https://leetcode.com/problems/interleaving-string/description/
#
# algorithms
# Medium (32.67%)
# Likes:    2133
# Dislikes: 111
# Total Accepted:    186.1K
# Total Submissions: 563.7K
# Testcase Example:  '"aabcc"\n"dbbca"\n"aadbbcbcac"'
#
# Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of
# s1 and s2.
#
# An interleaving of two strings s and t is a configuration where they are
# divided into non-empty substrings such that:
#
#
# s = s1 + s2 + ... + sn
# t = t1 + t2 + ... + tm
# |n - m| <= 1
# The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 +
# t3 + s3 + ...
#
#
# Note: a + b is the concatenation of strings a and b.
#
#
# Example 1:
#
#
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true
#
#
# Example 2:
#
#
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# Output: false
#
#
# Example 3:
#
#
# Input: s1 = "", s2 = "", s3 = ""
# Output: true
#
#
#
# Constraints:
#
#
# 0 <= s1.length, s2.length <= 100
# 0 <= s3.length <= 200
# s1, s2, and s3 consist of lowercase English letters.
#
#
#
# Follow up: Could you solve it using only O(s2.length) additional memory
# space?
#
#


# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        Given strings s1, s2, and s3, find whether s3 is formed by
        an interleaving of s1 and s2.

        An interleaving of two strings `s` and `t` is a configuration
        where they are divided into **non-empty substrings** such that
        - s = s1 + s2 + ... + sn
        - t = t1 + t2 + ... + tm
        - |n - m| <= 1
        - The interleaving is one of
            - s1 + t1 + s2 + t2 + s3 + t3 + ...
            - t1 + s1 + t2 + s2 + t3 + s3 + ...

        :param s1: The first string
        :param s2: The second string
        :param s3: The potential string that is an interleaving of s1 and s2
        :return: True if s3 is an interleaving of s1 and s2; False otherwise
        """
        if len(s1) + len(s2) != len(s3):
            return False
        return self.dp_linear_soln(s1, s2, s3)

    def dp_linear_soln(self, s1: str, s2: str, s3: str) -> bool:
        """
        DP Solution with linear space complexity

        Runtime: O(n1 * n2)
        Space: O(n2)
        """
        memo = [None for _ in range(len(s2) + 1)]
        memo[0] = True

        # substring starting at s2[j:] works
        for j in range(1, len(s2) + 1):
            memo[j] = memo[j - 1] and s2[j - 1] == s3[j - 1]

        for i in range(1, len(s1) + 1):
            # update 0 to true if s1 at this place works
            memo[0] = memo[0] and s1[i - 1] == s3[i - 1]
            for j in range(1, len(s2) + 1):
                # update [1:]: (prev i && curr s1) || (prev j && curr s2)
                memo[j] = (memo[j] and s1[i - 1] == s3[i - 1 + j]) or (
                    memo[j - 1] and s2[j - 1] == s3[i - 1 + j])
        return memo[-1]

    def dp_soln(self, s1: str, s2: str, s3: str) -> bool:
        """
        DP Solution

        Build the memo from top to bottom

        Base Case:
        - [0, 0] -> true by default
        - [i, 0] -> true if s1 substring starting from i works
        - [0, j] -> true if s2 substring starting from j works

        Inner Case:
        - [i, j] = [i - 1, j] (prev s1 worked) and curr s1 still works or
                   [i, j - 1] (prev s2 worked) and curr s2 still works

        Runtime: O(n1 * n2)
        Space: O(n1 * n2)
        """
        memo = [[None for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        memo[0][0] = True

        # first col: s1[i:] == s3[i:]
        for i in range(1, len(s1) + 1):
            memo[i][0] = memo[i - 1][0] and s1[i - 1] == s3[i - 1]
        # first row: s2[i:] == s3[i:]
        for j in range(1, len(s2) + 1):
            memo[0][j] = memo[0][j - 1] and s2[j - 1] == s3[j - 1]

        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                memo[i][j] = (memo[i - 1][j] and s1[i - 1] == s3[i - 1 + j]) or \
                    (memo[i][j - 1] and s2[j - 1] == s3[i - 1 + j])
        return memo[-1][-1]

    def memoized_soln(self, s1: str, s2: str, s3: str) -> bool:
        """
        Memoized Solution

        Memoize the recursive solution by constructing a 2D memo

        - Memo[s1_idx][s2_idx] == None
            - The memo has not been initialized
        - Memo[s1_idx][s2_idx] == True
            - The substrings starting from s1[s1_idx] and s2[s2_idx] are
              interleaving forming s3
        - Memo[s1_idx][s2_idx] == False
            - The substrings starting from s1[s1_idx] and s2[s2_idx] are
              interleaving forming s3

        Runtime: O(n1 * n2)
        Space: O(n1 * n2)
        """
        memo = [[None for _ in range(len(s2))] for _ in range(len(s1))]

        def recurse(s1_idx: int, s2_idx: int, s3_idx: int) -> bool:
            if memo[s1_idx][s2_idx] is not None:
                return memo[s1_idx][s2_idx]
            if s2_idx == len(s2):
                memo[s1_idx][s2_idx] = s1[s1_idx:] == s3[s3_idx:]
            elif s1_idx == len(s1):
                memo[s1_idx][s2_idx] = s2[s2_idx:] == s3[s3_idx:]
            else:
                if s1[s1_idx] == s3[s3_idx] and \
                    recurse(s1_idx + 1, s2_idx, s3_idx + 1):
                    memo[s1_idx][s2_idx] = True
                elif s2[s2_idx] == s3[s3_idx] and \
                    recurse(s1_idx, s2_idx + 1, s3_idx + 1):
                    memo[s1_idx][s2_idx] = True
                else:
                    memo[s1_idx][s2_idx] = False
            return memo[s1_idx][s2_idx]

        return recurse(0, 0, 0)

    def recursive_soln(self, s1: str, s2: str, s3: str) -> bool:
        """
        Recursive Solution

        Recursively increment index for (s1 & s3) || (s2 & s3) to
        check whether the list can exhaust

        Base Case:
        - s2_idx == len(s2) - compare the rest
            - return s1[s1_idx:] == s3[s3_idx:]
        - s1_idx == len(s1) - compare the rest
            - return s2[s2_idx:] == s3[s3_idx:]

        Recursive Case:
        - if s1 match, Recurse s1_idx + 1, s2_idx, s3_idx + 1
        - if s2 match, Recurse s1_idx, s2_idx + 1, s3_idx + 1

        Runtime: O(n1 * n2)
        Space: O(n1 * n2)
        """
        def recurse(s1_idx: int, s2_idx: int, s3_idx: int) -> bool:
            if s2_idx == len(s2):
                return s1[s1_idx:] == s3[s3_idx:]
            elif s1_idx == len(s1):
                return s2[s2_idx:] == s3[s3_idx:]
            else:
                if s1[s1_idx] == s3[s3_idx] and \
                    recurse(s1_idx + 1, s2_idx, s3_idx + 1):
                    return True
                elif s2[s2_idx] == s3[s3_idx] and \
                    recurse(s1_idx, s2_idx + 1, s3_idx + 1):
                    return True
                return False

        return recurse(0, 0, 0)


# @lc code=end

if __name__ == "__main__":
    # Test Case 1
    input1 = "aabcc"
    input2 = "dbbca"
    input3 = "aadbbcbcac"
    expected = True
    actual = Solution().isInterleave(input1, input2, input3)
    print("Test case 1")
    print(actual)
    print(expected)

    # Test Case 2
    input1 = "aabcc"
    input2 = "dbbca"
    input3 = "aadbbbaccc"
    expected = False
    actual = Solution().isInterleave(input1, input2, input3)
    print("Test case 2")
    print(actual)
    print(expected)

    # Test Case 4
    input1 = ""
    input2 = ""
    input3 = ""
    expected = True
    actual = Solution().isInterleave(input1, input2, input3)
    print("Test case 4")
    print(actual)
    print(expected)
