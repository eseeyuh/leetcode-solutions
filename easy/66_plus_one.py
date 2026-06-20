"""

66. Plus One
Difficulty: Easy
Link: https://leetcode.com/problems/plus-one/

PROBLEM:
You are given a large integer represented as an integer array digits.

Each digits[i] is one digit of the number.
The digits are ordered from most significant to least significant.

Increment the large integer by one and return the resulting array of digits.

Example:
Input: digits = [1, 2, 3]
Output: [1, 2, 4]

Explanation:
The array represents 123.
123 + 1 = 124.

APPROACH:
Start from the last digit and add one.

If the digit is less than 9, simply add 1 and return digits.
If the digit is 9, it becomes 0 and we continue carrying 1 to the left.

If all digits were 9, for example [9, 9, 9],
then after the loop we need to add 1 at the beginning:
[1, 0, 0, 0]

Time Complexity: O(n)
Space Complexity: O(1), excluding the output array

"""

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits

            digits[i] = 0

        return [1] + digits


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()

    print(solution.plusOne([1, 2, 3]))
    # [1, 2, 4]

    print(solution.plusOne([4, 3, 2, 1]))
    # [4, 3, 2, 2]

    print(solution.plusOne([9]))
    # [1, 0]

    print(solution.plusOne([9, 9, 9]))
    # [1, 0, 0, 0]

    print(solution.plusOne([1, 9, 9]))
    # [2, 0, 0]
