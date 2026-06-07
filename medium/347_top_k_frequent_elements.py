"""
==================================================
347. Top K Frequent Elements
Difficulty: Medium
Link: https://leetcode.com/problems/top-k-frequent-elements/
==================================================

PROBLEM:
Given an integer array nums and an integer k, return the
k most frequent elements. You may return the answer in
any order.

APPROACH:
First count the frequency of each number using a hash map.
Then use bucket sort: create buckets indexed by frequency,
where bucket[i] holds all numbers that appear exactly i
times. Since a number can appear at most len(nums) times,
we need len(nums) + 1 buckets. Finally, iterate from the
highest frequency down, collecting numbers until we have k.

==================================================
"""

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)

        result = []
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result
        return result


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()
    print(solution.topKFrequent([1, 1, 1, 2, 2, 3], 2))              # [1, 2]
    print(solution.topKFrequent([1], 1))                             # [1]
    print(solution.topKFrequent([1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2))  # [1, 2]
