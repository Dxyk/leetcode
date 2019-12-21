class Solution:
    def countAndSay(self, n: int) -> str:
        """
        The count-and-say sequence is the sequence of integers with the first five terms as
        following:

        1.  1
        2.  11
        3.  21
        4.  1211
        5.  111221

        1 is read off as "one 1" or 11.
        11 is read off as "two 1s" or 21.
        21 is read off as "one 2, then one 1" or 1211.

        Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

        Note: Each term of the sequence of integers will be represented as a string.

        >>> Solution().countAndSay(1)
        '1'
        >>> Solution().countAndSay(4)
        '1211'

        :param n: the nth term to generate
        :return: the nth term
        """
        return self.soln(n)

    def soln(self, n: int) -> str:
        """
        T: O()

        :param n: the nth term to generate
        :return: the nth term
        """
        res = "1"
        for _ in range(n - 1):
            res = self._get_result(res)
        return res

    def _get_result(self, prev_res: str) -> str:
        """
        Helper method that gets the new result given the previous result

        :param prev_res: the previous result
        :return: the next result
        """
        count, i, res = 1, 0, ""
        while i < len(prev_res) - 1:
            if prev_res[i] == prev_res[i + 1]:
                count += 1
            else:
                res += str(count) + prev_res[i]
                count = 1
            i += 1
        res += str(count) + prev_res[i]
        return res


if __name__ == "__main__":
    print(Solution().countAndSay(1))
