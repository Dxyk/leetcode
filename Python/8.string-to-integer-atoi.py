class Solution:
    def myAtoi(self, s):
        """
        Implement atoi which converts a string to an integer.

        The function first discards as many whitespace characters as necessary until the first non-whitespace character is found.
        Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible,
        and interprets them as a numerical value.

        The string can contain additional characters after those that form the integral number,
        which are ignored and have no effect on the behavior of this function.

        If the first sequence of non-whitespace characters in s is not a valid integral number,
        or if no such sequence exists because either s is empty or it contains only whitespace characters, no conversion is performed.

        If no valid conversion could be performed, a zero value is returned.

        Note:
        - Only the space character ' ' is considered as whitespace character.
        - Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1].
          If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.

        >>> Solution().myAtoi("42")
        42
        >>> Solution().myAtoi("   -42")
        -42
        >>> Solution().myAtoi("4193 with words")
        4193
        >>> Solution().myAtoi("words and 987")
        0
        >>> Solution().myAtoi("-91283472332")
        -2147483648

        :type str: str
        :rtype: int
        """
        MAX_INT = 2 ** 31 - 1
        MIN_INT = - 2 ** 31
        i = 0
        str_val = ""
        s = s.lstrip()
        if s.startswith('-') or s.startswith('+'):
            str_val += s[0]
            s = s[1:]
        while i < len(s) and s[i].isdigit():
            str_val += s[i]
            i += 1
        if str_val == "+" or str_val == "-":
            str_val = ""
        int_val = int(str_val) if str_val != "" else 0
        if int_val > MAX_INT:
            return MAX_INT
        elif int_val < MIN_INT:
            return MIN_INT
        return int_val


def stringToString(input):
    import json

    return json.loads(input)


def main():
    print(Solution().myAtoi("42"))


if __name__ == '__main__':
    main()
