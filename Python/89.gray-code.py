#
# @lc app=leetcode id=89 lang=python3
#
# [89] Gray Code
#
# https://leetcode.com/problems/gray-code/description/
#
# algorithms
# Medium (50.57%)
# Likes:    857
# Dislikes: 1822
# Total Accepted:    182K
# Total Submissions: 356.9K
# Testcase Example:  '2'
#
# The gray code is a binary numeral system where two successive values differ
# in only one bit.
#
# Given an integer n representing the total number of bits in the code, return
# any sequence of gray code.
#
# A gray code sequence must begin with 0.
#
#
# Example 1:
#
#
# Input: n = 2
# Output: [0,1,3,2]
# Explanation:
# 00 - 0
# 01 - 1
# 11 - 3
# 10 - 2
# [0,2,3,1] is also a valid gray code sequence.
# 00 - 0
# 10 - 2
# 11 - 3
# 01 - 1
#
#
# Example 2:
#
#
# Input: n = 1
# Output: [0,1]
#
#
#
# Constraints:
#
#
# 1 <= n <= 16
#
#
#

# @lc code=start
from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        """
        Returns a sequence of number that can be represented by n bits
        and every 2 successive values differ by only 1 bit

        :param n: The number of bits
        :return: The gray code sequence using n bits
        """
        if n < 0:
            return []
        return self.back_tracking(n)

    def back_tracking(self, n: int) -> List[int]:
        """
        Back Tracking Solution

        With a few examples, there are some observations we can see

        - With each `n`, we can build the first half using `n - 1`
        - The second half is the reverse of the first half, except for the highest bit

        n = 1:
        - [0, 1]
        - [0, 1]

        n = 2:
        - [00, 01,
           11, 10]
        - [0, 1,
           3, 2]

        n = 3:
        - [000, 001, 011, 010,
           110, 111, 101, 100]
        - [0, 1, 3, 2,
           6, 7, 5, 4]

        n = 4:
        - [0000, 0001, 0011, 0010, 0110, 0111, 0101, 0100,
           1100, 1101, 1111, 1110, 1010, 1011, 1001, 1000]
        - [00, 01, 03, 02, 06, 07, 05, 04,
           12, 13, 15, 14, 10, 11, 09, 08]

        Runtime: O(2^n)
        Space: O(2^n)
        """
        res = [0]
        # build res list n times
        for i in range(n):
            for j in range(len(res) - 1, -1, -1):
                # equivalent to the following
                # prev = res[j]
                # first_bit = 1 << i # 1{0 * i}
                # res = prev | first_bit # 1{prev}
                res.append(res[j] | 1 << i)
        return res

    def recursive_soln(self, n: int) -> List[int]:
        """
        Recursive Solution

        Build each n from n - 1

        Runtime: O(2^n)
        Space: O(2^n)
        """
        # base cases
        if n == 0:
            return [0]
        elif n == 1:
            return [0, 1]
        elif n == 2:
            return [0, 1, 3, 2]
        else:
            res = []
            prev_res = self.recursive_soln(n - 1)
            res += prev_res
            for prev in prev_res[::-1]:
                res.append(prev + 2**(n - 1))
            return res


# @lc code=end

if __name__ == "__main__":
    # Test Case 1
    input1 = 1
    expected = [0, 1]
    actual = Solution().grayCode(input1)
    print("Test case 1")
    print(actual)
    print(expected)

    # Test Case 2
    input1 = 2
    expected = [0, 1, 3, 2]
    actual = Solution().grayCode(input1)
    print("Test case 2")
    print(actual)
    print(expected)

    # Test Case 3
    input1 = 3
    expected = [0, 1, 3, 2, 6, 7, 5, 4]
    actual = Solution().grayCode(input1)
    print("Test case 3")
    print(actual)
    print(expected)

    # Test Case 4
    input1 = 4
    expected = [0, 1, 3, 2, 6, 7, 5, 4, 12, 13, 15, 14, 10, 11, 9, 8]
    actual = Solution().grayCode(input1)
    print("Test case 4")
    print(actual)
    print(expected)
