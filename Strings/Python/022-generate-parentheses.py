from typing import List


class Solution:
    # TODO: REVISIT
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

        >>> set(Solution().generateParenthesis(3)) == {"((()))", "(()())", "(())()", "()(())", "()()()"}
        True

        :param n: the number of pairs of parentheses
        :return: a list of all possible parenthesis
        """
        return self.closure_number(n)

    def closure_number(self, n: int) -> List[str]:
        """
        T: O()
        Generate all possible solutions using the closure number method

        :param n: the number of pairs of parentheses
        :return: a list of all possible parenthesis
        """
        if n == 0: return ['']
        ans = []
        for c in range(n):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(n - 1 - c):
                    ans.append('({}){}'.format(left, right))
        return ans

    def back_tracking(self, n: int) -> List[str]:
        """
        T: O()
        Generate all possible solutions by backtracking

        :param n: the number of pairs of parentheses
        :return: a list of all possible parenthesis
        """
        ans = []

        def back_track(s: str = '', left: int = 0, right: int = 0) -> None:
            """
            back track and add each result to the result list
            Note: we do not add every single one. instead, we check if we still have one of n places to place the parenthesis.

            :param s: the prev string
            :param left: the right-most left parentheses
            :param right: the right-most right parentheses
            """
            if len(s) == 2 * n:
                ans.append(s)
                return
            if left < n:
                back_track(s + '(', left + 1, right)
            if right < left:
                back_track(s + ')', left, right + 1)

        back_track()
        return ans

    def brute_force(self, n: int) -> List[str]:
        """
        T: O(2^(2n) n)
        Generate all possible solutions and check if they're valid

        :param n: the number of pairs of parentheses
        :return: a list of all possible parenthesis
        """
        ans = []

        def generate(prev_comb: List[str] = None) -> None:
            """
            Generates the combination and add it to the results list

            :param prev_comb: the previous combination
            :return: None
            """
            if prev_comb is None:
                prev_comb = []
            if len(prev_comb) == 2 * n:
                if self._is_valid(prev_comb):
                    ans.append("".join(prev_comb))
            else:
                prev_comb.append('(')
                generate(prev_comb)
                prev_comb.pop()
                prev_comb.append(')')
                generate(prev_comb)
                prev_comb.pop()

        generate()
        return ans

    def _is_valid(self, s: List[str]) -> bool:
        """
        Return if the given string is a valid combination of parentheses

        :param s:
        :return:
        """
        balance = 0
        for char in s:
            if char == "(":
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False
        return balance == 0


def main():
    print(Solution().generateParenthesis(3))


if __name__ == '__main__':
    main()
