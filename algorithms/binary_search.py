# iterative solution
def binary_search1(items, target):
    left = 0
    right = len(items) - 1
    while left <= right:
        midpoint = left + (right-left) // 2
        if items[midpoint] == target:
            return midpoint
        if items[midpoint] > target:
            right = midpoint - 1
        else:
            left = midpoint + 1
    return -1

# recursive solution
def binary_search2(items, left, right, target):
    if right >= left:
        midpoint = left + (right - left) // 2
        if items[midpoint] == target:
            return midpoint
        if items[midpoint] > target:
            return binary_search2(items, left, midpoint-1, target)
        else:
            return binary_search2(items, midpoint+1, right, target)
    return -1

l = [0, 1, 5, 9, 13, 31, 42]

assert binary_search1(l, 99) == -1 
assert binary_search2(l, 0, len(l)-1, 99) == -1 

for x in l:
    assert binary_search1(l, x) == l.index(x)
    assert binary_search2(l, 0, len(l) - 1, x) == l.index(x)
    