class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        Implement pow(x, n), which calculates x raised to the power n (x^n).

        Note:
        - -100.0 < x < 100.0
        - n is a 32-bit signed integer, within the range [−2^31, 2^31 − 1]

        >>> Solution().myPow(2.0, 10)
        1024.0
        >>> Solution().myPow(2.1, 3)
        9.261
        >>> Solution().myPow(2.0, -2)
        0.25

        :param x: base
        :param n: power
        :return: x^n
        """
        if x <= -100 or x >= 100:
            return 0
        if n < -2 ** 31 or n > 2 ** 31 - 1:
            return 0
        return round(self.recursive_soln(x, n), 5)

    def recursive_soln(self, x: float, n: int) -> float:
        """
        The recursive solution

        :param x: base
        :param n: power
        :return: x^n
        """
        if not n:
            return 1
        if n < 0:
            return 1 / self.recursive_soln(x, -n)
        if n % 2:
            return x * self.recursive_soln(x, n - 1)
        return self.recursive_soln(x * x, n // 2)

    def iterative_soln(self, x: float, n: int) -> float:
        """
        The iterative solution

        :param x: base
        :param n: power
        :return: x^n
        """
        if n < 0:
            x = 1 / x
            n = -n
        res = 1
        while n:
            if n % 2:
                res *= x
            x *= x
            n //= 2
        return res

    def built_in(self, x: float, n: int) -> float:
        """
        The built in implementation

        :param x: base
        :param n: power
        :return: x^n
        """
        return x ** n


if __name__ == '__main__':
    Solution().myPow(2.0, 10)
