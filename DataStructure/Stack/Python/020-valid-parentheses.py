from typing import TypeVar, List

T = TypeVar('T')


class Stack:
    """ A FILO stack """
    _stack: List[T]

    def __init__(self):
        self._stack = []

    def push(self, item: T) -> None:
        """
        push an item to the stack

        :param item: the item to push into the stack
        :return: None
        """
        self._stack.append(item)

    def pop(self) -> T:
        """
        pop an item out of the stack

        :return: the last item that's added to the stack
        """
        return self._stack.pop()

    def is_empty(self) -> bool:
        """
        return if the stack is empty

        :return: True if the stack is empty, False otherwise
        """
        return len(self._stack) == 0


class Solution:
    def isValid(self, s: str) -> bool:
        """
        Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
        determine if the input string is valid.

        An input string is valid if:
        1. Open brackets must be closed by the same type of brackets.
        2. Open brackets must be closed in the correct order.

        Note that an empty string is also considered valid.

        >>> Solution().isValid("")
        True
        >>> Solution().isValid("()[]{}")
        True
        >>> Solution().isValid("(]")
        False

        :param s: the given string containing only characters '(', ')', '{', '}', '[' and ']'
        :return: True if the given parentheses are valid, false otherwise
        """
        return self.my_soln(s)

    def my_soln(self, s: str) -> bool:
        """
        T: O(n), Space: O(n)

        :param s: the given string containing only characters '(', ')', '{', '}', '[' and ']'
        :return: True if the given parentheses are valid, false otherwise
        """
        valid_pairs = {"]": "[", "}": "{", ")": "("}
        stack = Stack()
        for char in s:
            if char in valid_pairs.values():
                stack.push(char)
            else:
                if char not in valid_pairs or stack.is_empty() or valid_pairs[char] != stack.pop():
                    return False

        return stack.is_empty()

    def is_matching_pair(self, left: str, right: str) -> bool:
        return (left == "(" and right == ")") or \
               (left == "[" and right == "]") or \
               (left == "{" and right == "}")


def main():
    print(Solution().isValid("23"))


if __name__ == "__main__":
    main()
