# https://leetcode.com/problems/two-sum/submissions/ 

# Runtime: 106 ms, faster than 57.61% of Python3 online submissions for Two Sum.
# Memory Usage: 15.2 MB, less than 24.20% of Python3 online submissions for Two Sum.

# Complexity: time O(N), space O(N)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i