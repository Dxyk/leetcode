class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
        Given two non-negative integers num1 and num2 represented as strings,
        return the product of num1 and num2, also represented as a string.

        >>> Solution().multiply("2", "3")
        '6'
        >>> Solution().multiply("123", "456")
        '56088'

        :param num1: the first number in string
        :param num2: the second number in string
        :return: the product of num1 and num2 in string
        """
        return self.built_in_soln(num1, num2)

    def my_soln(self, num1: str, num2: str) -> str:
        """
        using python's built-ins

        :param num1: the first number in string
        :param num2: the second number in string
        :return: the product of num1 and num2 in string
        """
        zero_ord = 48
        if num1 == '0' or num2 == '0':
            return '0'
        for i in range(max(len(num1), len(num2))):




    def built_in_soln(self, num1: str, num2: str) -> str:
        """
        using python's built-ins

        :param num1: the first number in string
        :param num2: the second number in string
        :return: the product of num1 and num2 in string
        """
        return str(int(num1) * int(num2))


if __name__ == '__main__':
    print(Solution().multiply("123", "456"))
