from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """
        You are given a string, s, and a list of words, words, that are all of the same length.
        Find all starting indices of substring(s) in s that is a concatenation of
        each word in words exactly once and without any intervening characters.

        >>> Solution().findSubstring("barfoothefoobarman", ["foo","bar"])
        [0,9]
        >>> Solution().findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"])
        []
        >>> Solution().findSubstring("", ["a"])
        []
        >>> Solution().findSubstring("aaaa", ["a"])
        [0, 1, 2, 3]

        :param s: the target string
        :param words: the list of substrings
        :return: the indices where s[i:] substring forms the combination of all strings in words
        """
        return self.brute_force(s, words)

    def brute_force(self, s: str, words: List[str]) -> List[int]:
        """
        T: O()
        The brute force solution

        :param s: the target string
        :param words: the list of substrings
        :return: the indices where s[i:] substring forms the combination of all strings in words
        """
