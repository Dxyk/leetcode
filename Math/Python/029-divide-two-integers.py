class Solution:
    MAX_INT = 0x7FFFFFFF  # 2 ** 31 - 1
    MIN_INT = -0x80000000  # -2 ** 32

    def divide(self, dividend: int, divisor: int) -> int:
        """
        Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

        Return the quotient after dividing dividend by divisor.

        The integer division should truncate toward zero.

        >>> Solution().divide(10, 3)
        3
        >>> Solution().divide(7, -3)
        -2
        >>> Solution().divide(1, 1)
        1

        :param dividend: the dividend
        :param divisor: the divisor
        :return: dividend // divisor
        """
        if divisor == 0:
            return self.MAX_INT
        if dividend == 0:
            return 0

        return self.process_nums_soln(dividend, divisor)

    def process_nums_soln(self, dividend: int, divisor: int) -> int:
        """
        process the numbers by dividing every ten digits

        :param dividend: the dividend
        :param divisor: the divisor
        :return: dividend // divisor
        """
        # TODO: Walk Through
        negative = (dividend > 0) ^ (divisor > 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1  # i *= 2
                temp <<= 1  # temp *= 2
        if negative:
            res *= -1
        return min(max(self.MIN_INT, res), self.MAX_INT)

    def python_soln(self, dividend: int, divisor: int) -> int:
        """
        the python soln

        :param dividend: the dividend
        :param divisor: the divisor
        :return: dividend // divisor
        """
        res = dividend // divisor
        if res > self.MAX_INT:
            return self.MAX_INT
        if res < self.MIN_INT:
            return self.MIN_INT
        opposite_sign = (divisor > 0) ^ (dividend > 0)
        if opposite_sign and dividend % divisor:
            return res + 1
        else:
            return res
