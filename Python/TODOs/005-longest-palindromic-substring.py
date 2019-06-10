class Solution(object):
    def longestPalindrome(self, s: str) -> str:
        """
        Dynamic programming

        Given a string s, find the longest palindromic substring in s.
        You may assume that the maximum length of s is 1000.

        >>> Solution().longestPalindrome("babad")  # 'aba' and 'bab' are both correct
        'bab'
        >>> Solution().longestPalindrome("cbbd")
        'bb'

        :type s: str
        :rtype: str
        """
        return self.brute_force(s)

    def brute_force(self, s: str) -> str:
        """
        O(n^3)
        The brute force soln

        :type s: str
        :rtype: str
        """
        longest_palindrome, max_length = "", 0
        for start in range(len(s)):
            for end in range(start + 1, len(s) + 1):
                substring = s[start: end]
                is_palindrome = True
                for i in range(len(substring) // 2):
                    if substring[i] != substring[len(substring) - i - 1]:
                        is_palindrome = False
                        break
                if is_palindrome and len(substring) > max_length:
                    longest_palindrome = substring
                    max_length = len(substring)
        return longest_palindrome

    def dynamic_programming_soln(self, s: str) -> str:
        """
        The dp soln

        :type s: str
        :rtype: str
        """
        # TODO


if __name__ == '__main__':
    print(Solution().longestPalindrome(""))
