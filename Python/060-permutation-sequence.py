import math
from typing import List


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        """
        The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

        By listing and labeling all of the permutations in order,
        we get the following sequence for n = 3:
        1. "123"
        2. "132"
        3. "213"
        4. "231"
        5. "312"
        6. "321"

        Given n and k, return the kth permutation sequence.

        Note:
        - Given n will be between 1 and 9 inclusive.
        - Given k will be between 1 and n! inclusive.

        >>> Solution().getPermutation(3, 3)
        '213'
        >>> Solution().getPermutation(4, 9)
        '2314'

        :param n: the number n
        :param k: the number k
        :return: the kth permutation of n to return
        """
        # if not 1 <= n <= 9 or not 1 <= k <= math.factorial(n):
        #     raise ValueError("n must be between 1-9, and k must be between 1-n!.")

        return self.index_soln(n, k)

    def index_soln(self, n: int, k: int) -> str:
        """
        https://leetcode.com/problems/permutation-sequence/discuss/22512

        :param n: the number n
        :param k: the number k
        :return: the kth permutation of n to return
        """
        # cache all factorials
        factors = [1]
        for i in range(1, n):
            factors.append(factors[-1] * i)
        factors.reverse()

        result = ''
        digits = [str(x) for x in range(1, n + 1)]

        k -= 1
        for i in range(n):
            # factors[i] = math.factorial(n-1-i)
            index, k = divmod(k, factors[i])
            curr_digit = digits[index]
            result += curr_digit
            digits.remove(curr_digit)
        return result

    def brute_force(self, n: int, k: int) -> str:
        """
        The brute force soln:
        generate a list of all permutations and return the kth idx

        :param n: the number n
        :param k: the number k
        :return: the kth permutation of n to return
        """

        def dfs_recursive(nums: List[int], path: str, res: List[str]) -> None:
            if not nums:
                res.append(path)
            for i in range(len(nums)):
                dfs_recursive(nums[:i] + nums[i + 1:], path + str(nums[i]), res)

        nums = list(range(1, n + 1))
        res = []
        dfs_recursive(nums, "", res)
        return res[k - 1]
