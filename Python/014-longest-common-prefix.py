from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Write a function to find the longest common prefix string amongst an array of strings.

        If there is no common prefix, return an empty string "".

        >>> Solution().longestCommonPrefix(["flower","flow","flight"])
        'fl'
        >>> Solution().longestCommonPrefix(["dog","racecar","car"])
        ''

        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        # ===== the python way O(mn) =====
        # return self._my_soln(strs)

        # ===== Horizontal Scanning O(mn) =====
        # return self._horizontal_scanning(strs)

        # ===== Vertical Scanning O(mn) =====
        # return self._lcp_vertical_scanning(strs)

        # ===== Divide and Conquer O(mn) Space: O(m * log(n)) =====
        # return self._divide_and_conquer(strs, 0, len(strs) - 1)

        # ===== Binary Search: Time O(), Space: O() =====
        return self._binary_search(strs)

    def _my_soln(self, strs: List[str]) -> str:
        """
        :param strs: the list of strings
        :return: the longest common prefix
        """
        res = ""
        first_s = strs[0]
        for i in range(len(first_s)):
            if all([s.startswith(first_s[: i + 1]) for s in strs]):
                res = first_s[: i + 1]
        return res

    def _horizontal_scanning(self, strs: List[str]) -> str:
        """
        Horizontal Scanning O(mn): (where s is sum of all chars in the array)
        LCP(S1, ..., Sn) = LCP(S1, LCP(S2, ... LCP(Sn-2, LCP(Sn-1, Sn)))

        :param strs: the list of strings
        :return: the longest common prefix
        """
        prefix = strs[0]
        for i in range(len(strs)):
            while not strs[i].startswith(prefix):
                prefix = prefix[: len(prefix) - 1]
                if prefix == "":
                    return prefix
        return prefix

    def _vertical_scanning(self, strs: List[str]) -> str:
        """
        Vertical Scanning O(mn):
        Instead of scanning with each string, scan for each column.

        :param strs: the list of strings
        :return: the longest common prefix
        """
        first_s = strs[0]
        for i in range(len(first_s)):
            c = first_s[i]
            for j in range(len(strs)):
                s = strs[j]
                if i == len(s) or s[i] != c:
                    return first_s[:i]
        return first_s

    def _divide_and_conquer(self, strs: List[str], left: int, right: int) -> str:
        """
        Divide and Conquer O(mn) Space: O(m * log(n)):
        LCP(S1, ..., Sn) = LCP(LCP(S1, ..., Si-1), LCP(Si, ..., Sn))

        :param strs: the list of strings
        :param left: left idx
        :param right: right index
        :return: the longest common prefix
        """
        if left == right:
            return strs[left]
        else:
            mid = (left + right) // 2
            left_result = self._divide_and_conquer(strs, left, mid)
            right_result = self._divide_and_conquer(strs, mid + 1, right)

            # Got left and right results, now get longest common prefix
            min_len = min(len(left_result), len(right_result))
            for i in range(min_len):
                if left_result[i] != right_result[i]:
                    return left_result[:i]
            return left_result[:min_len]

    def _binary_search(self, strs: List[str]) -> str:
        """
        Binary Search. Time: O(m*n*log(n)). Space: (1)
        Binary search the longest possible prefix (min length string among strs) and get the max length prefix

        :param strs: the list of strings
        :return: the longest common prefix
        """
        min_len = min([len(s) for s in strs])
        left, right = 1, min_len
        first_s = strs[0]
        while left <= right:
            mid = (left + right) // 2
            is_common_prefix = True
            for i in range(len(strs)):
                if not strs[i].startswith(first_s[: mid]):
                    is_common_prefix = False
                    break
            if is_common_prefix:
                left = mid + 1
            else:
                right = mid - 1
        return first_s[: (left + right) // 2]


def main():
    print(Solution().longestCommonPrefix(["c", "c"]))


if __name__ == '__main__':
    main()
