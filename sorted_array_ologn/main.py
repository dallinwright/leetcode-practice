# This is a sample Python script.
from statistics import median
from typing import List


def find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    """
    This is actually very difficult as you cannot iterate the arrays
    You cant even introspect them but operate on general information
    To achieve O(log(m+n)) we need to use binary operations basically.

    This comes from leetcode hard level exercises. They want to see if you can take a single liner that operates in
    O(m+n) and make it O(log(m+n)). Might seem overkill for 99% of use cases, but it is a good exercise since sometimes
    that difference makes all the difference.

    :parameter nums1: List[int]
    :parameter nums2: List[int]

    :return: float (the median of the two sorted but unmerged arrays)
    """
    # O(log(m+n)) means we have to cut in half repeatedly to get the data we want. Think binary search like a tree.
    # Start by calculating the kth element, in our case the median/middle element
    # k = (m+n)/2
    # if k is odd, then we need to find the kth element
    # if k is even, then we need to find the kth and k+1st element and take the average
    aggregate_middle_index = (len(nums1) + len(nums2)) / 2

    # We have two arrays, and we want to find the median they are both sorted but unmerged which is the problem.
    # Merging is time complexity O(M + N) so we want to avoid that for the exercise.
    # According to algorithm wiki page and docs, we need to use the smaller array as the base.
    first_length = len(nums1)
    second_length = len(nums2)

    shorter_array = nums1 if first_length < second_length else nums2
    longer_array = nums1 if first_length > second_length else nums2

    start_index = 0
    end_index = len(longer_array)

    # Tricky and not straightforward. We need to find in the longer array, the point to partition it so that the left
    # side of the partition is less than the right side of the partition calculates the index where the median would be
    # if you combined the two arrays into a single sorted array
    # (if the combined size is odd, this is the exact median index).
    # Notice the double slash divide by 2. This floors it and forces an int conversion if it is a float.
    combined_median_index: int = (first_length + second_length + 1) // 2

    # Subtracting mid from this index gives you the corresponding index in the other array (longer array)
    # that would be part of the median partition.
    longer_array_partition_index = combined_median_index - aggregate_middle_index

    smaller_list_partition = shorter_array[longer_array_partition_index]

    return 0.0


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass
