from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Given an array of strings, group anagrams together.

        >>> Solution().groupAnagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat'])
        [['ate', 'eat', 'tea'], ['nat', 'tan'], ['bat']]
        >>> Solution().groupAnagrams(['yup', 'yup', 'pup'])
        [['yup', 'yup'], ['pup']]

        Note:
        - All inputs will be in lowercase.
        - The order of your output does not matter.

        :param strs: an array of strings
        :return: a list of groups of anagrams
        """
        if not strs:
            return []
        return self.brute_force(strs)

    def hash_map_soln(self, strs: List[str]) -> List[List[str]]:
        """
        T: O(n^2 * k^2)
        the brute force soln

        :param strs: an array of strings
        :return: a list of groups of anagrams
        """

    def brute_force(self, strs: List[str]) -> List[List[str]]:
        """
        T: O(n^2 * k^2)
        the brute force soln

        :param strs: an array of strings
        :return: a list of groups of anagrams
        """

        def is_anagram(s1: str, s2: str) -> bool:
            """
            T: O(k^2)
            Returns True if the given two strings are anagram

            :param s1: the first string
            :param s2: the second string
            :return: true if s1 and s2 are anagrams
            """
            if len(s1) == len(s2):
                seen = []
                for i in range(len(s1)):
                    found = False
                    for j in range(len(s2)):
                        if j not in seen and s1[i] == s2[j]:
                            found = True
                            seen.append(j)
                            break
                    if not found:
                        return False
                return True
            else:
                return False

        res = []
        for s in strs:
            has_anagram = False
            for i in range(len(res)):
                if is_anagram(s, res[i][0]):
                    has_anagram = True
                    res[i].append(s)
            if not has_anagram:
                res.append([s])
        return res


if __name__ == '__main__':
    Solution().groupAnagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat'])
