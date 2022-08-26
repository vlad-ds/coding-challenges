# https://www.interviewquery.com/questions/find-the-missing-number

# easier to do with a loop. here we explore a mathematical solution

def sum_n(n):
    return n * (n+1) / 2

def missing_number(nums):
    min_, max_ = nums[0], nums[-1]
    total = sum_n(max_) - sum_n(min_ - 1)
    sum_ = sum(nums)
    if sum_ == total:
        return -1
    else:
        return total - sum_
    
nums1 = [0, 1, 2, 4, 5] 
nums2 = [6, 7, 8, 9, 10]

assert missing_number(nums1) == 3
assert missing_number(nums2) == -1