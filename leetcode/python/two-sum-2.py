# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

# Runtime: 138 ms, faster than 90.20% of Python3 online submissions for Two Sum II - Input Array Is Sorted.
# Memory Usage: 15 MB, less than 42.04% of Python3 online submissions for Two Sum II - Input Array Is Sorted.

# Complexity: time O(N), space O(1)

# Start with the full array. Let L be the leftmost element, R the rightmost.

# If L + R = target: We're done
# If L + R > target: The rightmost element is too big, because it exceeds the target, even when combined with the smallest available element. Since no element can be smaller than L, this proves that the rightmost element is useless and must be removed.
# If L + R < target: The leftmost element is too small, because it is smaller than the target, even when combined with the biggest available element. Therefore it must be removed.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while i != j:
            sum_ = numbers[i] + numbers[j]
            if sum_ == target:
                return [i+1, j+1]
            if sum_ > target: 
                j -= 1
            else:
                i += 1