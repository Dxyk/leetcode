from typing import List, Dict, Tuple


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
        return self.hash_map_letter_count_soln(strs)

    def hash_map_letter_count_soln(self, strs: List[str]) -> List[List[str]]:
        """
        T: O(n * k)
        where
        - n is the length of strs
        - k is the max length of word in strs

        The hash map solution
        The map: (countOfEachCharacter) : [strs anagrams]

        e.g. "aaabbc"
        {(3, 2, 1, 0, ..., 0) : ["aaabbc"]}

        :param strs: an array of strings
        :return: a list of groups of anagrams
        """
        d: Dict[Tuple[int], List[str]] = {}
        head = ord("a")

        for word in strs:
            count = [0] * 26
            for ch in word:
                count[ord(ch) - head] += 1
            if tuple(count) in d:
                d[tuple(count)].append(word)
            else:
                d[tuple(count)] = [word]
        return list(d.values())


    def hash_map_sorted_letters_soln(self, strs: List[str]) -> List[List[str]]:
        """
        T: O(n * k * log(k))
        where
        - n is the length of strs
        - k is the max length of word in strs

        The hash map solution
        The map: sortedLetters : [strs anagrams]

        :param strs: an array of strings
        :return: a list of groups of anagrams
        """
        d: Dict[str, List[str]] = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in d:
                d[sorted_word].append(word)
            else:
                d[sorted_word] = [word]

        return list(d.values())

    def _sort_word(self, word: str) -> str:
        """
        Helper method that sorts a word

        :param word: the unsorted word
        :return: the sorted word
        """
        ords = [ord(ch) for ch in word]
        ords.sort()
        return "".join([chr(code) for code in ords])

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
