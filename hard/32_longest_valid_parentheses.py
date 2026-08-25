"""

32. Longest Valid Parentheses
Difficulty: Hard
Link: https://leetcode.com/problems/longest-valid-parentheses/

PROBLEM:
Given a string containing only the characters '(' and ')',
return the length of the longest valid well-formed parentheses substring.

Example 1:
Input: s = "(()"
Output: 2

Explanation:
The longest valid parentheses substring is "()".

Example 2:
Input: s = ")()())"
Output: 4

Explanation:
The longest valid parentheses substring is "()()".

Example 3:
Input: s = ""
Output: 0

APPROACH:
Use a stack of indices.

We store indices of unmatched parentheses.

The stack starts with -1.
This value acts as a base index before the valid substring starts.

When we see '(':
- push its index to the stack.

When we see ')':
- pop from the stack because we found a possible matching pair.

After popping:
1. If the stack is empty, push the current index.
   This means the current ')' cannot be matched, so it becomes the new base.
2. Otherwise, calculate the current valid length:
   current_index - stack[-1]

Update the maximum length whenever we find a longer valid substring.

Time Complexity: O(n)
Space Complexity: O(n)

"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:

        stack = [-1]
        max_length = 0

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()

                if not stack:
                    stack.append(i)
                else:
                    current_length = i - stack[-1]
                    max_length = max(max_length, current_length)

        return max_length


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()

    print(solution.longestValidParentheses("(()"))
    # 2

    print(solution.longestValidParentheses(")()())"))
    # 4

    print(solution.longestValidParentheses(""))
    # 0

    print(solution.longestValidParentheses("()(()"))
    # 2

    print(solution.longestValidParentheses("()(())"))
    # 6

    print(solution.longestValidParentheses("(()())"))
    # 6
