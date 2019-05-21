class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Implement strStr().

        Return the index of the first occurrence of needle in haystack,
        or -1 if needle is not part of haystack.

        >>> Solution().strStr("asdf", "")
        0
        >>> Solution().strStr("hello", "ll")
        2
        >>> Solution().strStr("aaaaa", "bba")
        -1
        >>> Solution().strStr("a", "a")
        0

        :param haystack: the string to find in
        :param needle: the target substring
        :return: the index of the substring
        """
        if len(needle) == 0:
            return 0
        if len(haystack) == 0 or len(haystack) < len(needle):
            return -1
        return self.python_built_in(haystack, needle)

    def python_built_in(self, haystack: str, needle: str) -> int:
        """
        T: O(n)
        The python built in method

        :param haystack: the string to find in
        :param needle: the target substring
        :return: the index of the substring
        """
        return haystack.index(needle) if needle in haystack else -1

    def two_pointer(self, haystack: str, needle: str) -> int:
        """
        T: O(n^2)
        The two po9inter solution. Note: also the brute force solution

        :param haystack: the string to find in
        :param needle: the target substring
        :return: the index of the substring
        """
        idx = 0
        while idx <= len(haystack) - len(needle):
            if haystack[idx] == needle[0]:
                is_match = True
                num_char = 0
                while num_char < len(needle):
                    if haystack[idx + num_char] != needle[num_char]:
                        is_match = False
                        break
                    num_char += 1
                if is_match:
                    return idx
            idx += 1
        return -1
