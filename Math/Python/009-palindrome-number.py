class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

        >>> Solution().isPalindrome(121)
        True
        >>> Solution().isPalindrome(-121)
        False
        >>> Solution().isPalindrome(10)
        False

        :type x: int
        :rtype: bool
        """
        # """ Python Hacky Way """
        # return 0 <= x == int(str(x)[::-1])
        """ Normal Way """
        if x < 0:
            return False
        x_cpy = x
        x_rev = 0
        while x_cpy != 0:
            x_rev = 10 * x_rev + x_cpy % 10
            x_cpy //= 10
        return x_rev == x


def main():
    print(Solution().isPalindrome(121))


if __name__ == '__main__':
    main()
