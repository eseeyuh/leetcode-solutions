"""

67. Add Binary
Difficulty: Easy
Link: https://leetcode.com/problems/add-binary/

PROBLEM:
Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"

APPROACH:
Use two pointers starting from the end of both strings.

Binary addition works like normal addition:
0 + 0 = 0
1 + 0 = 1
1 + 1 = 10

So we keep a carry.

At each step:
1. Add the current digit from a if it exists.
2. Add the current digit from b if it exists.
3. Add the carry.
4. Append total % 2 to the answer.
5. Update carry as total // 2.

Since we build the answer from right to left, we reverse it at the end.

Time Complexity: O(max(n, m))
Space Complexity: O(max(n, m))

where:
n = len(a)
m = len(b)

"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:

        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            total = carry

            if i >= 0:
                total += int(a[i])
                i -= 1

            if j >= 0:
                total += int(b[j])
                j -= 1

            result.append(str(total % 2))
            carry = total // 2

        return "".join(reversed(result))


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()

    print(solution.addBinary("11", "1"))
    # "100"

    print(solution.addBinary("1010", "1011"))
    # "10101"

    print(solution.addBinary("0", "0"))
    # "0"

    print(solution.addBinary("1", "0"))
    # "1"

    print(solution.addBinary("1111", "1111"))
    # "11110"
