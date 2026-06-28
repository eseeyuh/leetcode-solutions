"""

17. Letter Combinations of a Phone Number
Difficulty: Medium
Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/

PROBLEM:
Given a string containing digits from 2 to 9 inclusive,
return all possible letter combinations that the number could represent.

The mapping is the same as on telephone buttons:

2 -> abc
3 -> def
4 -> ghi
5 -> jkl
6 -> mno
7 -> pqrs
8 -> tuv
9 -> wxyz

Example 1:
Input: digits = "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

Example 2:
Input: digits = "2"
Output: ["a", "b", "c"]

APPROACH:
Use backtracking.

We build combinations character by character.

For every digit:
1. Get the letters mapped to that digit.
2. Try each possible letter.
3. Add the letter to the current path.
4. Move to the next digit.
5. When the path length equals digits length, save the combination.

Time Complexity: O(4^n)
Space Complexity: O(n), excluding the output array

where:
n = len(digits)

The base is 4 because some digits, like 7 and 9, map to 4 letters.

"""

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []

        def backtrack(index: int, path: str) -> None:
            if index == len(digits):
                result.append(path)
                return

            current_digit = digits[index]
            letters = phone_map[current_digit]

            for letter in letters:
                backtrack(index + 1, path + letter)

        backtrack(0, "")

        return result


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()

    print(solution.letterCombinations("23"))
    # ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

    print(solution.letterCombinations("2"))
    # ["a", "b", "c"]

    print(solution.letterCombinations(""))
    # []

    print(solution.letterCombinations("7"))
    # ["p", "q", "r", "s"]

    print(solution.letterCombinations("79"))
    # 16 combinations
