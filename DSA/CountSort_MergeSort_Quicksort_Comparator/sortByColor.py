'''Given an array with N objects colored red, white, or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will represent the colors as,

red -> 0
white -> 1
blue -> 2

Note: Using the library sort function is not allowed.'''

A = [0, 1, 2, 0, 1, 2]
# A = [0]
# arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]

# Function to sort array
def sort012(arr, n):
    lo = 0
    hi = n - 1
    mid = 0
    # Iterate till all the elements
    # are sorted
    while mid <= hi:
      # If the element is 0
      if arr[mid] == 0:
        arr[lo], arr[mid] = arr[mid], arr[lo]
        lo = lo + 1
        mid = mid + 1
        # If the element is 1
      elif arr[mid] == 1:
        mid = mid + 1
        # If the element is 2
      else:
        arr[mid], arr[hi] = arr[hi], arr[mid]
        hi = hi - 1
    return arr



n = len(A)
arr = sort012(A, n)
print(arr)
print()
