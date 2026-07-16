"""

191. Number of 1 Bits
Difficulty: Easy
Link: https://leetcode.com/problems/number-of-1-bits/

PROBLEM:
Given a positive integer n, return the number of set bits in its binary
representation.

A set bit is a bit equal to 1.

This is also known as the Hamming weight.

Example 1:
Input: n = 11
Output: 3

Explanation:
11 in binary is 1011.
It has three set bits.

Example 2:
Input: n = 128
Output: 1

Explanation:
128 in binary is 10000000.
It has one set bit.

Example 3:
Input: n = 2147483645
Output: 30

APPROACH:
Use Brian Kernighan's bit manipulation algorithm.

The expression:

n & (n - 1)

removes the rightmost set bit from n.

So we repeatedly remove one set bit and increase the counter.
When n becomes 0, all set bits have been removed.

Time Complexity: O(k)
Space Complexity: O(1)

where:
k = number of set bits in n

In the worst case, for a 32-bit integer, this is still O(1),
because there are at most 32 bits.

"""


class Solution:
    def hammingWeight(self, n: int) -> int:

        count = 0

        while n:
            n &= n - 1
            count += 1

        return count


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()

    print(solution.hammingWeight(11))
    # 3

    print(solution.hammingWeight(128))
    # 1

    print(solution.hammingWeight(2147483645))
    # 30

    print(solution.hammingWeight(1))
    # 1

    print(solution.hammingWeight(15))
    # 4
