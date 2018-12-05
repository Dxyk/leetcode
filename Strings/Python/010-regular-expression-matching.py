class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

        - '.' Matches any single character.
        - '*' Matches zero or more of the preceding element.

        The matching should cover the entire input string (not partial).

        Note:
        - s could be empty and contains only lowercase letters a-z.
        - p could be empty and contains only lowercase letters a-z, and characters like . or *.

        >>> Solution().isMatch("aa", "a")
        False
        >>> Solution().isMatch("aa", "a")
        True
        >>> Solution().isMatch("ab", ".*")
        True
        >>> Solution().isMatch("aab", "c*a*b")
        False
        >>> Solution().isMatch("mississippi", "mis*is*p*.")
        False

        :type s: str
        :type p: str
        :rtype: bool
        """
        # TODO: Dynamic Programming


def main():
    print(Solution().isMatch("aa", "a"))


if __name__ == '__main__':
    main()
