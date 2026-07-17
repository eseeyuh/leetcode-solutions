"""

38. Count and Say
Difficulty: Medium
Link: https://leetcode.com/problems/count-and-say/

PROBLEM:
The count-and-say sequence is a sequence of digit strings defined by:

countAndSay(1) = "1"
countAndSay(n) = run-length encoding of countAndSay(n - 1)

Run-length encoding means replacing each group of consecutive identical
characters with:

count + character

Example:
"3322251" becomes:
"33"  -> "23"
"222" -> "32"
"5"   -> "15"
"1"   -> "11"

So the encoded string is:
"23321511"

Given a positive integer n, return the nth element of the count-and-say sequence.

Example 1:
Input: n = 4
Output: "1211"

Explanation:
countAndSay(1) = "1"
countAndSay(2) = "11"
countAndSay(3) = "21"
countAndSay(4) = "1211"

Example 2:
Input: n = 1
Output: "1"

APPROACH:
Use an iterative solution.

Start with current = "1".

Then repeat n - 1 times:
1. Read the current string from left to right.
2. Count consecutive equal characters.
3. Append the count and character to the next string.
4. Replace current with the next string.

Time Complexity: O(L)
Space Complexity: O(L)

where:
L is the total length of generated strings up to n.

"""


class Solution:
    def countAndSay(self, n: int) -> str:

        current = "1"

        for _ in range(n - 1):
            next_string = []
            count = 1

            for i in range(1, len(current)):
                if current[i] == current[i - 1]:
                    count += 1
                else:
                    next_string.append(str(count))
                    next_string.append(current[i - 1])
                    count = 1

            next_string.append(str(count))
            next_string.append(current[-1])

            current = "".join(next_string)

        return current


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()

    print(solution.countAndSay(1))
    # "1"

    print(solution.countAndSay(2))
    # "11"

    print(solution.countAndSay(3))
    # "21"

    print(solution.countAndSay(4))
    # "1211"

    print(solution.countAndSay(5))
    # "111221"
