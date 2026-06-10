"""

20. Valid Parentheses
Difficulty: Easy
Link: https://leetcode.com/problems/valid-parentheses/

PROBLEM:
Given a string s containing only the characters:
'(', ')', '{', '}', '[' and ']'

Determine if the input string is valid.

A string is valid if:
1. Open brackets are closed by the same type of brackets.
2. Open brackets are closed in the correct order.
3. Every closing bracket has a corresponding opening bracket.

APPROACH:
Use a stack to store opening brackets.

When we see an opening bracket, we push it into the stack.
When we see a closing bracket, we check whether the stack is not empty
and whether the last opening bracket matches the current closing bracket.

If it does not match, the string is invalid.
At the end, the string is valid only if the stack is empty.

Time Complexity: O(n)
Space Complexity: O(n)

"""


class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        matching = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for char in s:
            if char in matching:
                if not stack or stack[-1] != matching[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)

        return not stack


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()

    print(solution.isValid("()"))
    # True

    print(solution.isValid("()[]{}"))
    # True

    print(solution.isValid("(]"))
    # False

    print(solution.isValid("([])"))
    # True

    print(solution.isValid("([)]"))
    # False

    print(solution.isValid("{[]}"))
    # True
