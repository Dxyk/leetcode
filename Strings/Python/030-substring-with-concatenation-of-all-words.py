import copy
from typing import Dict, List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """
        You are given a string, s, and a list of words that are all of the same length.
        Find all starting indices of substring(s) in s that is a concatenation of
        each word in words exactly once and without any intervening characters.

        Notations:
        - n: len(s)
        - k: len(words)
        - m: len(word[0])

        >>> sorted(Solution().findSubstring("barfoothefoobarman", ["foo","bar"]))
        [0, 9]
        >>> sorted(Solution().findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"]))
        []
        >>> sorted(Solution().findSubstring("", ["a"]))
        []
        >>> sorted(Solution().findSubstring("aaaa", ["a"]))
        [0, 1, 2, 3]
        >>> sorted(Solution().findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"]))
        [8]
        >>> sorted(Solution().findSubstring("a", []))
        []

        :param s: the target string
        :param words: the list of substrings
        :return: the indices where s[i:] substring forms the combination of all strings in words
        """
        if not s or not words or not words[0]:
            return []
        words = [word for word in words if word != ""]

        return self.two_pointer(s, words)

    def two_pointer(self, s: str, words: List[str]) -> List[int]:
        """
        T: O()

        :param s: the target string
        :param words: the list of substrings
        :return: the indices where s[i:] substring forms the combination of all strings in words
        """
        len_str = len(s)
        len_word = len(words[0])
        len_substr = len(words) * len_word
        word_to_times = {}

        # populate word_to_times dict
        for word in words:
            word_to_times[word] = 1 if word not in word_to_times else word_to_times[word] + 1

        ans = []
        for i in range(min(len_word, len_str - len_substr + 1)):
            self._find_answer(i, len_str, len_word, len_substr, s, word_to_times, ans)
        return ans

    def _find_answer(self, start_idx: int, end_idx: int,
                     len_word: int, len_substr: int,
                     s: str, word_to_times: Dict[str, int], ans: List[int]) -> None:
        """
        Helper method that appends answers to the result list

        :param start_idx: the start index of the current search
        :param end_idx: the end index of the current search
        :param len_word: the length of the word
        :param len_substr: the length of the substring all together
        :param s: the string to search for
        :param word_to_times: the times dict
        :param ans: the answer list
        :return: None
        """
        ptr = start_idx
        curr = {}
        while start_idx + len_substr <= end_idx:
            word = s[ptr: ptr + len_word]
            ptr += len_word
            if word in word_to_times:
                curr[word] = 1 if word not in curr else curr[word] + 1
                while curr[word] > word_to_times[word]:  # NOTE: This part is smart
                    # 1. If the word appears more time than it should, use start_idx as the pointer,
                    #    minus every word we've counted until we have met the current ptr word.
                    # 2. If we've generated the answer, then the next word in words in s must be
                    #    exceeding the max count, so we shift it in stead of starting right there.
                    curr[s[start_idx: start_idx + len_word]] -= 1
                    start_idx += len_word
                if ptr - start_idx == len_substr:
                    ans.append(start_idx)
            else:
                start_idx = ptr
                curr.clear()

    def hash_table(self, s: str, words: List[str]) -> List[int]:
        """
        T: O(n^2 k^2)
        Instead of looping through every word, use a hash table to store each word and check off
        each when encountered

        :param s: the target string
        :param words: the list of substrings
        :return: the indices where s[i:] substring forms the combination of all strings in words
        """
        # Hash table of [first letter of each word] : [List of words with that first letter]
        all_words: Dict[str, List[str]] = {}
        result = []
        for word in words:  # O(k)
            if word != "":
                k = word[0]
                if k in all_words:
                    all_words[k].append(word)
                else:
                    all_words[k] = [word]

        i = 0
        while i < len(s):  # O(n)
            all_words_cpy = copy.deepcopy(all_words)  # O(k)
            j = i
            while j < len(s) and all_words_cpy.values() and s[j] in all_words_cpy:  # O(n)
                found = False
                for word in all_words_cpy[s[j]]:  # O(k)
                    if s.startswith(word, j):
                        all_words_cpy[s[j]].remove(word)
                        if not all_words_cpy[s[j]]:
                            all_words_cpy.pop(s[j])
                        found = True
                        j += len(word)
                if not found:
                    break
            if not all_words_cpy:
                result.append(i)
            i += 1
        return result

    def python_built_in_brute_force(self, s: str, words: List[str]) -> List[int]:
        """
        T: O(k!)
        The brute force solution in the python way

        :param s: the target string
        :param words: the list of substrings
        :return: the indices where s[i:] substring forms the combination of all strings in words
        """
        import itertools
        result = []
        for permutation in itertools.permutations(words, len(words)):
            # T: O(k!) super costly
            substring = "".join(permutation)
            if substring != "":
                idx = 0
                while idx < len(s) and substring in s[idx:]:
                    # T(n)
                    idx = s.index(substring, idx)
                    if idx not in result:
                        result.append(idx)
                    idx += 1
        return result


if __name__ == '__main__':
    print(sorted(Solution().findSubstring("barfoothefoobarman", ["foo", "bar"])))
