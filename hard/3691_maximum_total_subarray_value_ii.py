"""

3691. Maximum Total Subarray Value II
Difficulty: Hard
Link: https://leetcode.com/problems/maximum-total-subarray-value-ii/

PROBLEM:
You are given an integer array nums and an integer k.

You must select exactly k distinct non-empty subarrays.
Subarrays may overlap, but the exact same subarray cannot be chosen more than once.

The value of a subarray is:
max(subarray) - min(subarray)

Return the maximum possible total value of exactly k chosen subarrays.

APPROACH:
Unlike version I, we cannot choose the same subarray more than once.
So we need the sum of the k largest subarray values.

We binary search the kth largest subarray value.

For a value x, we can count how many subarrays have:
max(subarray) - min(subarray) >= x

This is done by counting how many subarrays have range <= x - 1,
then subtracting from the total number of subarrays.

After finding the kth largest value, we calculate:
1. Sum of all subarray values greater than that value.
2. Add the remaining needed subarrays with exactly that kth value.

Time Complexity: O(n log V)
where V = max(nums) - min(nums)

Space Complexity: O(n)

"""

from collections import deque
from typing import List, Tuple


class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:

        n = len(nums)
        total_subarrays = n * (n + 1) // 2
        max_range = max(nums) - min(nums)

        def count_at_most(limit: int) -> int:
            if limit < 0:
                return 0

            max_deque = deque()
            min_deque = deque()
            left = 0
            count = 0

            for right, value in enumerate(nums):
                while max_deque and nums[max_deque[-1]] <= value:
                    max_deque.pop()
                max_deque.append(right)

                while min_deque and nums[min_deque[-1]] >= value:
                    min_deque.pop()
                min_deque.append(right)

                while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                    if max_deque[0] == left:
                        max_deque.popleft()
                    if min_deque[0] == left:
                        min_deque.popleft()
                    left += 1

                count += right - left + 1

            return count

        def count_sum_at_most(limit: int) -> Tuple[int, int]:
            if limit < 0:
                return 0, 0

            max_deque = deque()
            min_deque = deque()

            sum_max = 0
            sum_min = 0

            left = 0
            count = 0
            total_sum = 0

            for right, value in enumerate(nums):
                max_count = 1
                while max_deque and max_deque[-1][0] <= value:
                    old_value, old_count = max_deque.pop()
                    sum_max -= old_value * old_count
                    max_count += old_count
                max_deque.append([value, max_count])
                sum_max += value * max_count

                min_count = 1
                while min_deque and min_deque[-1][0] >= value:
                    old_value, old_count = min_deque.pop()
                    sum_min -= old_value * old_count
                    min_count += old_count
                min_deque.append([value, min_count])
                sum_min += value * min_count

                while max_deque[0][0] - min_deque[0][0] > limit:
                    sum_max -= max_deque[0][0]
                    max_deque[0][1] -= 1
                    if max_deque[0][1] == 0:
                        max_deque.popleft()

                    sum_min -= min_deque[0][0]
                    min_deque[0][1] -= 1
                    if min_deque[0][1] == 0:
                        min_deque.popleft()

                    left += 1

                valid_subarrays_ending_here = right - left + 1
                count += valid_subarrays_ending_here
                total_sum += sum_max - sum_min

            return count, total_sum

        def count_at_least(value: int) -> int:
            return total_subarrays - count_at_most(value - 1)

        low = 0
        high = max_range

        while low < high:
            mid = (low + high + 1) // 2

            if count_at_least(mid) >= k:
                low = mid
            else:
                high = mid - 1

        kth_value = low

        _, total_sum = count_sum_at_most(max_range)
        count_less_or_equal, sum_less_or_equal = count_sum_at_most(kth_value)

        count_greater = total_subarrays - count_less_or_equal
        sum_greater = total_sum - sum_less_or_equal

        remaining = k - count_greater

        return sum_greater + remaining * kth_value


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()

    print(solution.maxTotalValue([1, 3, 2], 2))
    # 4

    print(solution.maxTotalValue([4, 2, 5, 1], 3))
    # 12

    print(solution.maxTotalValue([5], 1))
    # 0

    print(solution.maxTotalValue([1, 1, 1], 3))
    # 0
