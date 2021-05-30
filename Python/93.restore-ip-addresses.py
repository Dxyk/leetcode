#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#
# https://leetcode.com/problems/restore-ip-addresses/description/
#
# algorithms
# Medium (37.75%)
# Likes:    1805
# Dislikes: 570
# Total Accepted:    237.3K
# Total Submissions: 620K
# Testcase Example:  '"25525511135"'
#
# Given a string s containing only digits, return all possible valid IP
# addresses that can be obtained from s. You can return them in any order.
#
# A valid IP address consists of exactly four integers, each integer is between
# 0 and 255, separated by single dots and cannot have leading zeros. For
# example, "0.1.2.201" and "192.168.1.1" are valid IP addresses and
# "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP
# addresses.
#
#
# Example 1:
# Input: s = "25525511135"
# Output: ["255.255.11.135","255.255.111.35"]
# Example 2:
# Input: s = "0000"
# Output: ["0.0.0.0"]
# Example 3:
# Input: s = "1111"
# Output: ["1.1.1.1"]
# Example 4:
# Input: s = "010010"
# Output: ["0.10.0.10","0.100.1.0"]
# Example 5:
# Input: s = "101023"
# Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
#
#
# Constraints:
#
#
# 0 <= s.length <= 3000
# s consists of digits only.
#
#
#

# @lc code=start
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        """
        Given a string s containing only digits,
        return all possible valid IP addresses that
        can be obtained from s.

        A valid IP address consists of exactly four integers,
        each integer is between 0 and 255,
        separated by single dots and cannot have leading zeros.

        :param s: The string containing IP address digits
        :return: A list of all possible IP addresses using the digits in s
        """
        if not s:
            return []
        return self.dfs_soln(s)

    def dfs_soln(self, s: str) -> List[str]:
        """
        DFS Solution

        Keep track of
        - The remaining available digits
        - The current list of digits composing the IP address
        - The current list of built IP addresses

        Base case:
        - idx == 4 and not s: valid IP
            - Add to result list

        DFS Case:
        - First build base on next 1 digtit. This could be any digit
        - Then if the first digit is not 0, build base on next 2-3 digits that
          are <= 255

        Runtime: O(n)
        Space: O(1)
        """
        res = set()

        def dfs(remain: str, curr: List[str]) -> None:
            if len(curr) == 4 and not remain:
                res.add('.'.join(curr))
            elif len(curr) < 4 and remain:
                dfs(remain[1:], curr + [remain[0]])
                if remain[0] != '0':
                    for i in range(1, min(len(remain), 3)):
                        if int(remain[:i + 1]) <= 255:
                            dfs(remain[i + 1:], curr + [remain[:i + 1]])

        dfs(s, [])
        return list(res)


# @lc code=end

if __name__ == "__main__":
    # Test Case 1
    input1 = "25525511135"
    expected = ["255.255.11.135", "255.255.111.35"]
    actual = Solution().restoreIpAddresses(input1)
    print("Test case 1")
    print(actual)
    print(expected)
