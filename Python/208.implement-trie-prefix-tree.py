#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#
# https://leetcode.com/problems/implement-trie-prefix-tree/description/
#
# algorithms
# Medium (42.50%)
# Likes:    2186
# Dislikes: 39
# Total Accepted:    228K
# Total Submissions: 533.1K
# Testcase Example:
#   '["Trie","insert","search","search","startsWith","insert","search"],
#    [[],["apple"],["apple"],["app"],["app"],["app"],["app"]]'
#
# Implement a trie with insert, search, and startsWith methods.
#
# Example:
#
#
# Trie trie = new Trie();
#
# trie.insert("apple");
# trie.search("apple");   // returns true
# trie.search("app");     // returns false
# trie.startsWith("app"); // returns true
# trie.insert("app");
# trie.search("app");     // returns true
#
#
# Note:
#
#
# You may assume that all inputs are consist of lowercase letters a-z.
# All inputs are guaranteed to be non-empty strings.
#
#
#

# @lc code=start
from typing import Dict


class TrieNode:
    """
    A tree node
    """
    next_chars: Dict[str, "TrieNode"]
    is_end: bool

    def __init__(self):
        self.next_chars = dict()
        self.is_end = False


class Trie:
    """
    A Tree structure with each node containing a letter in the word.
    """
    head: TrieNode

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.head
        for ch in word:
            if ch not in curr.next_chars:
                curr.next_chars[ch] = TrieNode()
            curr = curr.next_chars[ch]
        curr.is_end = True
        return

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.head
        for ch in word:
            if ch not in curr.next_chars:
                return False
            curr = curr.next_chars[ch]
        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given
        prefix.
        """
        curr = self.head
        for ch in prefix:
            if ch not in curr.next_chars:
                return False
            curr = curr.next_chars[ch]
        return True


# @lc code=end
if __name__ == "__main__":
    trie = Trie()

    trie.insert("apple")
    print(trie.search("apple"), True)
    print(trie.search("app"), False)
    print(trie.startsWith("app"), True)
    trie.insert("app")
    print(trie.search("app"), True)
