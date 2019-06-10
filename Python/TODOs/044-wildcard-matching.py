class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        TODO: back tracking dp
        Given an input string (s) and a pattern (p), implement wildcard pattern matching with
        support for '?' and '*'.

        '?' Matches any single character.
        '*' Matches any sequence of characters (including the empty sequence).

        The matching should cover the entire input string (not partial).

        Note:
        - s could be empty and contains only lowercase letters a-z.
        - p could be empty and contains only lowercase letters a-z, and characters like ? or *.

        >>> Solution().isMatch("aa", "a")
        False
        >>> Solution().isMatch("aa", "*")
        True
        >>> Solution().isMatch("cb", "?a")
        False
        >>> Solution().isMatch("adceb", "*a*b")
        True
        >>> Solution().isMatch("acdcb", "a*c?b")
        False

        :param s: the string
        :param p: the pattern
        :return: True if the string matches the pattern, false otherwise
        """


if __name__ == '__main__':
    Solution().isMatch("acdcb", "a*c?b")
