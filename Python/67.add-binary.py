#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#
# https://leetcode.com/problems/add-binary/description/
#
# algorithms
# Easy (47.16%)
# Likes:    2618
# Dislikes: 336
# Total Accepted:    580.8K
# Total Submissions: 1.2M
# Testcase Example:  '"11"\n"1"'
#
# Given two binary strings a and b, return their sum as a binary string.
#
#
# Example 1:
# Input: a = "11", b = "1"
# Output: "100"
# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"
#
#
# Constraints:
#
#
# 1 <= a.length, b.length <= 10^4
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.
#
#
#


# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        Adds two binaries with string representation

        :param a: the first string represented binary
        :param b: the second string represented binary
        :return: the added string represented binary
        """
        return self.my_soln(a, b)

    def my_soln(self, a: str, b: str) -> str:
        result = ""
        carry = False
        # define b to be the shorter string
        if len(b) > len(a):
            a, b = b, a
        # access string in the reverse order by -i
        for i in range(1, len(a) + 1):
            if i <= len(b):
                ones = [a[-i] == "1", b[-i] == "1", carry]
            else:
                ones = [a[-i] == "1", carry]
            if ones.count(True) % 2 != 0:
                result = "1" + result
            else:
                result = "0" + result
            carry = ones.count(True) >= 2
        if carry:
            result = "1" + result
        return result

    def soln(self, a: str, b: str) -> str:
        if not a:
            return b
        if not b:
            return a

        result = ""
        sum_val = 0

        i, j = len(a) - 1, len(b) - 1

        while i >= 0 or j >= 0:
            if i >= 0:
                sum_val += int(a[i])
                i -= 1

            if j >= 0:
                sum_val += int(b[j])
                j -= 1

            result += str(sum_val % 2)
            sum_val = sum_val // 2

        if sum_val:
            result += str(sum_val)

        return result[::-1]


# @lc code=end

if __name__ == "__main__":
    print(Solution().addBinary("11", "1"))
