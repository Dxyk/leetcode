class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        """ Brute Force: O(n^3) """
        # max_length = 0
        # for start in range(len(s)):
        #     for end in range(start + 1, len(s) + 1):
        #         substring = s[start: end]
        #         has_repeat = False
        #         for idx in range(len(substring)):
        #             if substring[idx] in substring[idx + 1:]:
        #                 has_repeat = True;
        #                 break;
        #         if not has_repeat and len(substring) > max_length:
        #             max_length = len(substring)
        # return max_length

        """ Sliding Window: O(n) """
        # used_chars contains {char -> closest index}
        used_chars = {}
        start = max_length = 0

        for i, char in enumerate(s):
            if char in used_chars and start <= used_chars[char]:
                start = used_chars[char] + 1
            else:
                max_length = max(max_length, i - start + 1)
            used_chars[char] = i
        return max_length


def main():
    ret = Solution().lengthOfLongestSubstring("tmmzuxt")

    out = str(ret)
    print(out)


if __name__ == '__main__':
    main()