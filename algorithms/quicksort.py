# https://www.programiz.com/dsa/quick-sort
# https://www.youtube.com/watch?v=WprjBK0p6rw
# https://www.youtube.com/watch?v=MZaf_9IZCrc

# When partitioning, we keep "pushing forward" elements which are bigger than the pivot. 
# The first pointer (i) keeps track of the last greater-than-pivot element found. 
# The second pointer (j) iterates through all elements and swaps lesser-than-pivot elements with greater-than-pivot elements. 

def partition(array, low, high):
  # choose the rightmost element as pivot
  pivot = array[high]

  # pointer for greater element
  i = low - 1

  # traverse through all elements
  # compare each element with pivot
  for j in range(low, high):
    if array[j] <= pivot:
      # if element smaller than pivot is found
      # swap it with the greater element pointed by i
      i += 1

      # swapping element at i with element at j
      (array[i], array[j]) = (array[j], array[i])

  # swap the pivot element with the greater element specified by i
  (array[i + 1], array[high]) = (array[high], array[i + 1])

  # return the position from where partition is done
  return i + 1

# function to perform quicksort
def quicksort(array, low, high):
  if low < high:

    # find pivot element such that
    # element smaller than pivot are on the left
    # element greater than pivot are on the right
    pi = partition(array, low, high)

    # recursive call on the left of pivot
    quicksort(array, low, pi-1)

    # recursive call on the right of pivot
    quicksort(array, pi+1, high)
    

l = [10, 8, 5, 2, 1, 7, 6]
l_copy = l.copy()

quicksort(l, 0, len(l)-1)
assert l == sorted(l_copy)