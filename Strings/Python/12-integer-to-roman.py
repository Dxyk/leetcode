class Solution:
    def intToRoman(self, num: int) -> str:
        """
        Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

        Symbol       Value
        I             1
        V             5
        X             10
        L             50
        C             100
        D             500
        M             1000

        For example, two is written as II in Roman numeral, just two one's added together.
        Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

        Roman numerals are usually written largest to smallest from left to right.
        However, the numeral for four is not IIII. Instead, the number four is written as IV.
        Because the one is before the five we subtract it making four.
        The same principle applies to the number nine, which is written as IX.

        There are six instances where subtraction is used:

        I can be placed before V (5) and X (10) to make 4 and 9.
        X can be placed before L (50) and C (100) to make 40 and 90.
        C can be placed before D (500) and M (1000) to make 400 and 900.

        Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

        >>> Solution().intToRoman(3)
        'III'
        >>> Solution().intToRoman(4)
        'IV'
        >>> Solution().intToRoman(9)
        'IX'
        >>> Solution().intToRoman(58)
        'LVIII'
        >>> Solution().intToRoman(1994)
        'MCMXCIV'

        :type num: int
        :rtype: str
        """
        if num < 1 or num >= 4000:
            return ""
        # int_to_roman_dict = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        # dividers = [1000, 100, 10, 1]
        # result = ""
        # # use max_divider to reduce time
        # while num != 0:
        #     for idx in range(len(dividers)):
        #         divider = dividers[idx]
        #         curr_roman = int_to_roman_dict[divider]
        #         if num // divider != 0:
        #             if num // divider == 9:
        #                 result += curr_roman
        #                 result += int_to_roman_dict[divider * 10]
        #                 num -= divider * 9
        #             elif num // divider // 5 != 0:
        #                 result += int_to_roman_dict[divider * 5]
        #                 num -= divider * 5
        #             elif num // divider == 4:
        #                 result += curr_roman
        #                 result += int_to_roman_dict[divider * 5]
        #                 num -= divider * 4
        #             else:
        #                 result += curr_roman
        #                 num -= divider
        #
        #             break
        # return result
        """ a better python approach """
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        res = ""
        for n, v in zip(numerals, values):
            res += (num // v) * n
            num %= v
        return res


def main():
    print(Solution().intToRoman(1994))


if __name__ == '__main__':
    import doctest

    doctest.testmod()
    # main()
