# This is a sample Python script.
from statistics import median
from typing import List


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    sorted_array = []
    # O(log(m+n)) means we have to cut in half repeatedly to get the data we want
    # Start by calculating the kth element
    # k = (m+n)/2
    # if k is odd, then we need to find the kth element
    # if k is even, then we need to find the kth and k+1th element and take the average

    middle_index = (len(nums1) + len(nums2)) / 2

    last_index_first = len(nums1) - 1
    if middle_index > last_index_first:
        # We need to get the last element of the first array
        sorted_array.append(nums1[last_index_first])
        # We need to get the first element of the second array
        sorted_array.append(nums2[0])

    return median(sorted_array)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass
