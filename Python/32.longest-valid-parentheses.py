#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#
# https://leetcode.com/problems/longest-valid-parentheses/description/
#
# algorithms
# Hard (26.92%)
# Likes:    2574
# Dislikes: 112
# Total Accepted:    235.9K
# Total Submissions: 876.2K
# Testcase Example:  '"(()"'
#
# Given a string containing just the characters '(' and ')', find the length of
# the longest valid (well-formed) parentheses substring.
#
# Example 1:
#
#
# Input: "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()"
#
#
# Example 2:
#
#
# Input: ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()"
#
#
#

# @lc code=start


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        return self.counter_soln(s)

    def counter_soln(self, s: str) -> int:
        """
        use two counters left_count and right_count

        for every "(", left_count += 1. For every ")", right += 1.

        when left_count == right_count, parentheses match and calculate length

        when left_count < right_count, reset both to 0

        we do this for both left to right and right to left
        """
        res = left_count = right_count = 0

        for i in range(len(s)):
            if s[i] == "(":
                left_count += 1
            else:
                right_count += 1
            if left_count == right_count:
                res = max(res, 2 * right_count)
            elif right_count > left_count:
                left_count = right_count = 0

        left_count = right_count = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "(":
                left_count += 1
            else:
                right_count += 1
            if left_count == right_count:
                res = max(res, 2 * left_count)
            elif left_count > right_count:
                left_count = right_count = 0

        return res

    def stack_soln(self, s: str) -> int:
        """
        Using a stack, push each index of "(" into the stack so we can
        calculate the length

        Runtime: O(n)
        """
        res = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                else:
                    res = max(res, i - stack[-1])
        return res

    def dp_soln(self, s: str) -> int:
        """
        DP solution

        Algorithm:
        Keep a memo of length n. The ith idx indicates the length of valid
        parentheses ending at i.
        """
        res = 0
        memo = [0] * len(s)
        for i in range(1, len(s)):
            if s[i] == ")":
                if s[i - 1] == "(":
                    if i == 1:
                        memo[i] = 2
                    else:
                        memo[i] = 2 + memo[i - 2]
                elif i - memo[i - 1] > 0 and s[i - memo[i - 1] - 1] == "(":
                    if i - memo[i - 1] >= 2:
                        memo[i] = memo[i - 1] + memo[i - memo[i - 1] - 2] + 2
                    else:
                        memo[i] = memo[i - 1] + 2
                res = max(res, memo[i])
        return res

    def brute_force(self, s: str) -> int:
        """
        brute force solution

        Consider every possible even length pair and check using stack

        Runtime: O(n^3)
        """
        def is_valid(left: int, right: int) -> bool:
            stack = []
            for i in range(left, right + 1):
                if s[i] == "(":
                    stack.append(s[i])
                else:
                    if len(stack) == 0:
                        return False
                    else:
                        stack.pop()
            return len(stack) == 0

        res = 0
        for length in range(2, len(s) + 1, 2):
            for i in range(len(s) - length + 1):
                if is_valid(i, i + length - 1):
                    res = length
        return res

    def dp_recursive_max_single(self, s: str) -> int:
        """
        DP recursive solution

        NOTE: This is not the correct implementation since it only
              finds the maximum length in a single pair.
              i.e. ()() will return 2 instead of 4

        Subproblem structure:
        P(i, j) := max number of valid parenthesis in s[i: j]

        P(i, j) =
        1. 1 if i + 1 == j and s[i] == "(" and s[j] == ")"
        2. 0 if i == j or (i + 1 == j and (s[i] != "(" or s[j] != ")"))
        3. 1 + P(i + 1, j - 1) if s[i] == "(" and s[j] == ")" and
            P(i + 1, j - 1) == (j - i + 1)//2
        4. max(P(i, j - 1), P(i + 1, j)) else
        """
        def helper(i: int, j: int) -> int:
            if i >= j:
                return 0
            curr_pair = s[i] == "(" and s[j] == ")"
            if i + 1 == j:
                return 2 if curr_pair else 0
            if curr_pair:
                included_pair = helper(i + 1, j - 1)
                if included_pair + 2 == j - i + 1:
                    return 2 + included_pair
            return max(helper(i + 1, j), helper(i, j - 1))

        return helper(0, len(s) - 1)

# @lc code=end


if __name__ == "__main__":
    print(Solution().longestValidParentheses("()"), 2)
    print(Solution().longestValidParentheses("(()"), 2)
    print(Solution().longestValidParentheses(")()())"), 4)
