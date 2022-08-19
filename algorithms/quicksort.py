# https://www.programiz.com/dsa/quick-sort
# https://www.youtube.com/watch?v=WprjBK0p6rw

def quicksort1(array):
    """
    This is the naive Python version of the algorithm. 
    It glosses over the partitioning implementation. 
    """
    # base case: 1 or 0 elements
    if len(array) <= 1:
        return array
    # we use first element as pivot
    pivot = array[0]
    # get the partitions
    lesser = [el for el in array[1:] if el <= pivot]
    greater = [el for el in array[1:] if el > pivot]
    
    return quicksort1(lesser) + [pivot] + quicksort1(greater)

# def partition(array, low, high):
#     pivot = array[high]
#     i = low - 1 # pointer for greater element
#     for j in range(low, high):
#         if array[j] <= pivot:
#             array[i], array[j] = array[j], array[i]
#             i = i + 1
    

l = [10, 5, 2, 1, 7, 6]

assert quicksort1(l) == sorted(l)