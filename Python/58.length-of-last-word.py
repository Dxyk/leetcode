class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        Given a string s consists of upper/lower-case alphabets and
        empty space characters ' ', return the length of last word in the string.

        If the last word does not exist, return 0.

        Note:
        A word is defined as a character sequence consists of non-space characters only.

        >>> Solution().lengthOfLastWord("Hello World")
        5
        >>> Solution().lengthOfLastWord("   ")
        0
        >>> Solution().lengthOfLastWord("  abc  d   ")
        1

        :param s: the string
        :return: the length of the last word in the string
        """
        if not s:
            return 0
        return self.counter_soln(s)

    def counter_soln(self, s: str) -> int:
        """
        The counter soln

        :param s: the string
        :return: the length of the last word in the string
        """
        count = 0
        while s and s[-1] == " ":
            s = s[:-1]
        if not s:
            return 0
        while count < len(s) and s[-(count + 1)] != " ":
            count += 1
        return count

    def python_soln(self, s: str) -> int:
        """
        The python soln

        :param s: the string
        :return: the length of the last word in the string
        """
        return len(s.strip().split(" ")[-1])
