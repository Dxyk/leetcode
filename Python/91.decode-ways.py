#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#
# https://leetcode.com/problems/decode-ways/description/
#
# algorithms
# Medium (26.77%)
# Likes:    4453
# Dislikes: 3471
# Total Accepted:    570.4K
# Total Submissions: 2.1M
# Testcase Example:  '"12"'
#
# A message containing letters from A-Z can be encoded into numbers using the
# following mapping:
#
#
# 'A' -> "1"
# 'B' -> "2"
# ...
# 'Z' -> "26"
#
#
# To decode an encoded message, all the digits must be grouped then mapped back
# into letters using the reverse of the mapping above (there may be multiple
# ways). For example, "11106" can be mapped into:
#
#
# "AAJF" with the grouping (1 1 10 6)
# "KJF" with the grouping (11 10 6)
#
#
# Note that the grouping (1 11 06) is invalid because "06" cannot be mapped
# into 'F' since "6" is different from "06".
#
# Given a string s containing only digits, return the number of ways to decode
# it.
#
# The answer is guaranteed to fit in a 32-bit integer.
#
#
# Example 1:
#
#
# Input: s = "12"
# Output: 2
# Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
#
#
# Example 2:
#
#
# Input: s = "226"
# Output: 3
# Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2
# 2 6).
#
#
# Example 3:
#
#
# Input: s = "0"
# Output: 0
# Explanation: There is no character that is mapped to a number starting with
# 0.
# The only valid mappings with 0 are 'J' -> "10" and 'T' -> "20", neither of
# which start with 0.
# Hence, there are no valid ways to decode this since all digits need to be
# mapped.
#
#
# Example 4:
#
#
# Input: s = "06"
# Output: 0
# Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is
# different from "06").
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 100
# s contains only digits and may contain leading zero(s).
#
#
#

# @lc code=start
from typing import List


class Solution:
    def numDecodings(self, s: str) -> int:
        """
        Get the number of possible decodings given
        a string of numbers, where each number can be mapped
        to a letter

        :param s: The string of encoded numbers
        :return: The number of ways which the encoded string can be decoded
        """
        if not s:
            return 0
        return self.dp_linear_soln(s)

    def dp_linear_soln(self, s: str) -> int:
        """
        Dynamic Programming Linear Solution

        From dp solution we can see that each iteration only
        depends on the previous 2 indices of the memo, so it is
        unnecessary to keep a list.

        Runtime: O(n)
        Space: O(1)
        """
        prev_1 = 1
        prev_2 = 0

        for idx in range(len(s) - 1, -1, -1):
            if s[idx] == "0":
                curr = 0
            else:
                curr = prev_1
            if idx < len(s) - 1 and (s[idx] == '1' or \
                    (s[idx] == '2' and int(s[idx + 1]) <= 6)):
                curr += prev_2

            prev_2 = prev_1
            prev_1 = curr
        return prev_1

    def dp_soln(self, s: str) -> int:
        """
        Dynamic Programming Solution

        Build the memo bottom up (idx from len(s) - 1 to 0)
        Compared to the memoized solution, set the last item of the memo
        to 1 so it acts as the base case

        Runtime: O(n)
        Space: O(n)
        """
        memo = [0 for _ in range(len(s) + 1)]
        memo[len(s)] = 1
        for idx in range(len(s) - 1, -1, -1):
            if s[idx] != '0':
                memo[idx] = memo[idx + 1]
                if idx < len(s) - 1 and (s[idx] == '1' or \
                    (s[idx] == '2' and int(s[idx + 1]) <= 6)):
                    memo[idx] += memo[idx + 2]
        return memo[0]

    def memoized_soln(self, s: str) -> int:
        """
        Memoized solution derived from the recursive solution

        Use a memo (list) of size n to keep track of the results
        that has already been calculated

        Runtime: O(n)
        """
        def recursive_helper(idx: int, memo: List[int]) -> int:
            if idx == len(s):
                return 1
            if s[idx] == '0':
                return 0
            if memo[idx]:
                return memo[idx]
            memo[idx] = recursive_helper(idx + 1, memo)
            if idx < len(s) - 1 and (s[idx] == '1' or \
                (s[idx] == '2' and int(s[idx + 1]) <= 6)):
                memo[idx] += recursive_helper(idx + 2, memo)
            return memo[idx]

        memo = [None for _ in range(len(s))]
        return recursive_helper(0, memo)

    def recursive_soln(self, s: str) -> int:
        """
        Recursive solution

        recursively solve by incrementing the index to look at

        Runtime: O(2^n)
        """
        def recursive_helper(idx: int) -> int:
            """
            Base Case:
            - idx == len(s): 1  # reached the end
            - s[idx] == 0: 0  # invalid

            Recursive Case:
            - recurse(idx + 1)  # no matter what the current one is, recurse
            - recurse(idx + 2) if s[idx] == 1 or (s[idx] == 2 and s[idx + 1] in {0, ..., 6})
            """
            if idx == len(s):
                return 1
            if s[idx] == '0':
                return 0
            res = recursive_helper(idx + 1)
            if idx < len(s) - 1 and (s[idx] == '1' or \
                (s[idx] == '2' and int(s[idx + 1]) <= 6)):
                res += recursive_helper(idx + 2)
            return res

        return recursive_helper(0)


# @lc code=end

if __name__ == "__main__":
    # Test Case 1
    input1 = "12"
    expected = 2
    actual = Solution().numDecodings(input1)
    print("Test case 1")
    print(actual)
    print(expected)

    # Test Case 2
    input1 = "226"
    expected = 3
    actual = Solution().numDecodings(input1)
    print("Test case 2")
    print(actual)
    print(expected)

    # Test Case 3
    input1 = "0"
    expected = 0
    actual = Solution().numDecodings(input1)
    print("Test case 3")
    print(actual)
    print(expected)

    # Test Case 4
    input1 = "06"
    expected = 0
    actual = Solution().numDecodings(input1)
    print("Test case 4")
    print(actual)
    print(expected)
