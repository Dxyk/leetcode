#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#
# https://leetcode.com/problems/simplify-path/description/
#
# algorithms
# Medium (34.82%)
# Likes:    372
# Dislikes: 108
# Total Accepted:    277.9K
# Total Submissions: 792.4K
# Testcase Example:  '"/home/"'
#
# Given a string path, which is an absolute path (starting with a slash '/') to
# a file or directory in a Unix-style file system, convert it to the simplified
# canonical path.
#
# In a Unix-style file system, a period '.' refers to the current directory, a
# double period '..' refers to the directory up a level, and any multiple
# consecutive slashes (i.e. '//') are treated as a single slash '/'. For this
# problem, any other format of periods such as '...' are treated as
# file/directory names.
#
# The canonical path should have the following format:
#
#
# The path starts with a single slash '/'.
# Any two directories are separated by a single slash '/'.
# The path does not end with a trailing '/'.
# The path only contains the directories on the path from the root directory to
# the target file or directory (i.e., no period '.' or double period '..')
#
#
# Return the simplified canonical path.
#
#
# Example 1:
#
#
# Input: path = "/home/"
# Output: "/home"
# Explanation: Note that there is no trailing slash after the last directory
# name.
#
#
# Example 2:
#
#
# Input: path = "/../"
# Output: "/"
# Explanation: Going one level up from the root directory is a no-op, as the
# root level is the highest level you can go.
#
#
# Example 3:
#
#
# Input: path = "/home//foo/"
# Output: "/home/foo"
# Explanation: In the canonical path, multiple consecutive slashes are replaced
# by a single one.
#
#
# Example 4:
#
#
# Input: path = "/a/./b/../../c/"
# Output: "/c"
#
#
#
# Constraints:
#
#
# 1 <= path.length <= 3000
# path consists of English letters, digits, period '.', slash '/' or '_'.
# path is a valid absolute Unix path.
#
#
#


# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        return self.stack_soln(path)

    def stack_soln(self, path: str) -> str:
        """
        Create a stack using the splitted directories fromthe path
        For each item in the stack:
        - Do nothing if the item is not meaningful (`/` or `.`)
        - Pop an item if the item is parent dir (`..`)
        - Add the item to the stack otherwise

        Runtime: O(n)
        Space: O(n)

        :param path: The path to simplify
        :return: The simplified path
        """
        dir_list = path.split("/")
        res_list = []
        for item in dir_list:
            if item in ["", "."]:
                continue
            elif item == "..":
                if res_list:
                    res_list.pop()
            else:
                res_list.append(item)
        res_path = "/" + "/".join(res_list)
        return res_path


# @lc code=end

if __name__ == "__main__":
    print(Solution().simplifyPath("/home/"))
    print(Solution().simplifyPath("/../"))
    print(Solution().simplifyPath("/home//foo/"))
