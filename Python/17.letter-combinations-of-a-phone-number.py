from typing import Dict, List


class Solution:
    DIGIT_TO_LETTER: Dict[str, List[str]] = {
        "1": [],
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
        "0": []
    }

    def letterCombinations(self, digits: str) -> List[str]:
        """
        Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

        A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

        See [http://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Telephone-keypad2.svg/200px-Telephone-keypad2.svg.png] for image

        Note: Although the above answer is in lexicographical order, your answer could be in any order you want.

        >>> s = Solution().letterCombinations("23")
        >>> s.sort()
        >>> s
        ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']


        :param digits: the input digits
        :return: all possible letter combinations
        """
        if not digits.isdigit() or len(digits) == 0:
            return []

        return self.standard_soln(digits)

    def standard_soln(self, digits: str) -> List[str]:
        """
        T: O(n)
        use of recursion

        :param digits: the input digits
        :return: all possible letter combinations
        """
        # base case
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return Solution.DIGIT_TO_LETTER[digits[0]]

        # recursive step
        prev = self.standard_soln(digits[: -1])
        new = Solution.DIGIT_TO_LETTER[digits[-1]]
        return [p + n for n in new for p in prev]

    def my_soln(self, digits: str) -> List[str]:
        """
        T: O(n)

        :param digits: the input digits
        :return: all possible letter combinations
        """
        result = []

        for i in range(len(digits)):
            digit = digits[i]
            if i == 0:
                result = Solution.DIGIT_TO_LETTER[digit][:]
            else:
                new_result = []
                while len(result) != 0:
                    prev_combination = result.pop(0)
                    new_result += [prev_combination + letter for letter in Solution.DIGIT_TO_LETTER[digit]]
                result = new_result[:]

        return result


def main():
    print(Solution().letterCombinations("23"))


if __name__ == "__main__":
    main()
