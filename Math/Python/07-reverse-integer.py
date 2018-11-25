class Solution(object):
    def reverse(self, x: int) -> int:
        """
        Given a 32-bit signed integer, reverse digits of an integer.

        >>> Solution().reverse(123)
        321
        >>> Solution().reverse(-123)
        -321
        >>> Solution().reverse(120)
        21

        :type x: int
        :rtype: int
        """
        """ Python hacky way """
        # str_x = str(x) if x >= 0 else str(x)[1:]
        # reverse_x = int(str_x[::-1]) if x >= 0 else -int(str_x[::-1])
        # return reverse_x if -(2 ** 31) - 1 < reverse_x < 2 ** 31 else 0

        """ Number manipulation """
        res = 0
        positive = x >= 0
        x = abs(x)
        while x != 0:
            res = res * 10 + x % 10 if positive else res * 10 - x % 10
            x //= 10
        return res if -(2 ** 31) - 1 < res < 2 ** 31 else 0


def main():
    print(Solution().reverse(-123))


if __name__ == '__main__':
    main()
