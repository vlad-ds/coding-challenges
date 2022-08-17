# https://leetcode.com/problems/zigzag-conversion/

# Runtime: 63 ms, faster than 89.83% of Python3 online submissions for Zigzag Conversion.
# Memory Usage: 14.1 MB, less than 51.21% of Python3 online submissions for Zigzag Conversion.

# Complexity: O(N)
# Note: The whole problem is reduced to generating a cyclic order

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1 or numRows >= len(s):
            return s
        
        result = [''] * numRows
        index, step = 0, 1
        
        for char in s:
            result[index] += char
        
            if index == 0:
                step = 1

            if index == numRows - 1:
                step = -1

            index += step
        
        return ''.join(result)