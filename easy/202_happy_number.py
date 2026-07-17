"""

202. Happy Number
Difficulty: Easy
Link: https://leetcode.com/problems/happy-number/

PROBLEM:
Write an algorithm to determine if a number n is happy.

A happy number is defined by this process:
1. Start with any positive integer.
2. Replace the number by the sum of the squares of its digits.
3. Repeat the process.

If the number eventually becomes 1, it is a happy number.
If it enters a cycle that does not include 1, it is not a happy number.

Example 1:
Input: n = 19
Output: True

Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

Example 2:
Input: n = 2
Output: False

APPROACH:
Use Floyd's cycle detection algorithm.

If the process does not reach 1, it must eventually repeat a number.
That means there is a cycle.

We use two pointers:
slow moves one step at a time.
fast moves two steps at a time.

If fast reaches 1, the number is happy.
If slow and fast meet, there is a cycle, so the number is not happy.

Time Complexity: O(log n)
Space Complexity: O(1)

"""


class Solution:
    def isHappy(self, n: int) -> bool:

        def get_next(number: int) -> int:
            total = 0

            while number > 0:
                digit = number % 10
                total += digit * digit
                number //= 10

            return total

        slow = n
        fast = get_next(n)

        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))

        return fast == 1


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()

    print(solution.isHappy(19))
    # True

    print(solution.isHappy(2))
    # False

    print(solution.isHappy(1))
    # True

    print(solution.isHappy(7))
    # True

    print(solution.isHappy(4))
    # False
