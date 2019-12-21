class Solution:
    ZERO_ORD = 48

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
        return self.array_representation_soln(num1, num2)

    def array_representation_soln(self, num1: str, num2: str) -> str:
        """
        https://leetcode.com/problems/multiply-strings/discuss/17605

        :param num1: the first number in string
        :param num2: the second number in string
        :return: the product of num1 and num2 in string
        """
        if num1 == '0' or num2 == '0':
            return '0'

        res = ""
        pos = [0] * (len(num1) + len(num2))

        for i in range(len(num1) - 1, -1, -1):
            n1 = self._str_to_num(num1[i])
            for j in range(len(num2) - 1, -1, -1):
                n2 = self._str_to_num(num2[j])
                mul = n1 * n2
                p1, p2 = i + j, i + j + 1
                curr_sum = mul + pos[p2]

                pos[p1] += curr_sum // 10
                pos[p2] = curr_sum % 10

        for i in range(len(pos)):
            if not (i == 0 and pos[i] == 0):
                res += self._num_to_str(pos[i])
        return res

    def my_soln(self, num1: str, num2: str) -> str:
        """
        My method: loop through each digit

        :param num1: the first number in string
        :param num2: the second number in string
        :return: the product of num1 and num2 in string
        """
        res = ""
        if num1 == '0' or num2 == '0':
            return '0'

        rows = []
        for i in range(len(num1) - 1, -1, -1):
            n1 = self._str_to_num(num1[i])
            prev_carry = 0
            curr_res = 0
            for j in range(len(num2) - 1, -1, -1):
                n2 = self._str_to_num(num2[j])
                product = n1 * n2 + prev_carry
                carry = product // 10
                digit = product - carry * 10
                curr_res += digit * (10 ** (len(num2) - j - 1))
                prev_carry = carry
            curr_res += prev_carry * (10 ** len(num2))
            rows.append(curr_res)

        i = 0
        res_num = 0
        while i < len(rows):
            res_num += rows[i] * (10 ** i)
            i += 1

        while res_num:
            nxt = res_num // 10
            digit = res_num - nxt * 10
            res = self._num_to_str(digit) + res
            res_num = nxt
        return res

    def _num_to_str(self, num: int) -> str:
        """
        Helper function that turns a number to a string

        :param num: the number
        :return: the string
        """
        return chr(num + self.ZERO_ORD)

    def _str_to_num(self, string: str) -> int:
        """
        Helper function that turns a string to a number

        :param string: the string
        :return: the number
        """
        return ord(string) - self.ZERO_ORD

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
