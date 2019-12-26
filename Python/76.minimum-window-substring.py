#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#
# https://leetcode.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (32.77%)
# Likes:    3218
# Dislikes: 238
# Total Accepted:    310.5K
# Total Submissions: 946.8K
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# Given a string S and a string T, find the minimum window in S which will
# contain all the chs in T in complexity O(n).
#
# Example:
#
#
# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
#
#
# Note:
#
#
# If there is no such window in S that covers all chs in T, return the
# empty string "".
# If there is such window, you are guaranteed that there will always be only
# one unique minimum window in S.
#
#
#

# @lc code=start


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        return self.filtered_sliding_window_soln(s, t)

    def filtered_sliding_window_soln(self, s: str, t: str) -> str:
        """
        Sliding window but with a filtered s

        Runtime: O(2 * |filtered_s| + |s| + |t|)
        """
        if s == "" or t == "":
            return ""

        t_dict = {}
        for curr in t:
            t_dict[curr] = t_dict.get(curr, 0) + 1

        num_unique = len(t_dict)
        num_satisfied = 0
        window_counts = {}

        filtered_s = []
        for i, ch in enumerate(s):
            if ch in t_dict:
                filtered_s.append((i, ch))

        res = ""

        left, right = 0, 0
        while right < len(filtered_s):
            curr = filtered_s[right][1]
            window_counts[curr] = window_counts.get(curr, 0) + 1

            if curr in t_dict and window_counts[curr] == t_dict[curr]:
                num_satisfied += 1

            while left <= right and num_satisfied == num_unique:
                curr = filtered_s[left][1]
                end = filtered_s[right][0]
                start = filtered_s[left][0]
                if res == "" or end - start + 1 < len(res):
                    res = s[start: end + 1]
                window_counts[curr] -= 1
                if curr in t_dict and window_counts[curr] < t_dict[curr]:
                    num_satisfied -= 1
                left += 1

            right += 1

        return res

    def sliding_window_soln(self, s: str, t: str) -> str:
        """
        Sliding window solution

        Runtime: O(|s| + |t|)
        """
        if s == "" or t == "":
            return ""

        t_dict = {}
        for curr in t:
            t_dict[curr] = t_dict.get(curr, 0) + 1

        num_unique = len(t_dict)
        num_satisfied = 0
        window_counts = {}

        res = ""

        left, right = 0, 0
        while right < len(s):
            curr = s[right]
            window_counts[curr] = window_counts.get(curr, 0) + 1

            if curr in t_dict and window_counts[curr] == t_dict[curr]:
                num_satisfied += 1

            while left <= right and num_satisfied == num_unique:
                curr = s[left]
                if res == "" or right - left + 1 < len(res):
                    res = s[left: right + 1]
                window_counts[curr] -= 1
                if curr in t_dict and window_counts[curr] < t_dict[curr]:
                    num_satisfied -= 1
                left += 1

            right += 1

        return res

    def brute_force(self, s: str, t: str) -> str:
        """
        Brute force solution

        Runtime: O(mn^2) // n = len(s), m = len(t)
        """
        if s == "" or t == "":
            return ""

        res = ""
        for left in range(len(s)):
            t_cpy = t
            for i in range(left, len(s)):
                curr = s[i]
                if curr in t_cpy:
                    idx = t_cpy.find(curr)
                    t_cpy = t_cpy[:idx] + t_cpy[idx + 1:]
                if t_cpy == "" and (i - left < len(res) or res == ""):
                    res = s[left: i + 1]
                    break
        return res
# @lc code=end


if __name__ == "__main__":
    print(Solution().minWindow("ADOBECODEBANC", "ABC"), "BANC")
