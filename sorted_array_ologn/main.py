# This is a sample Python script.
import math
from statistics import median
from typing import List


def find_median_sorted_lists(nums1: List[int], nums2: List[int]) -> float:
    """
    This is actually very difficult as you cannot iterate the lists
    You cant even introspect them but operate on general information
    To achieve O(log(m+n)) we need to use binary operations basically.

    This comes from leetcode hard level exercises. They want to see if you can take a single liner that operates in
    O(m+n) and make it O(log(m+n)). Might seem overkill for 99% of use cases, but it is a good exercise since sometimes
    that difference makes all the difference.

    :parameter nums1: List[int]
    :parameter nums2: List[int]

    :return: Float (the median of the two sorted but unmerged lists)
    """
    # O(log(m+n)) means we have to cut in half repeatedly to get the data we want. Think binary search like a tree.

    # We have two lists, and we want to find the median they are both sorted but unmerged which is the problem.
    # Merging is time complexity O(M + N) so we want to avoid that for the exercise.
    # According to algorithm wiki page and docs, we need to use the smaller list as the base.

    # Assign the shorter and longer lists.
    shorter_list, longer_list = (nums1, nums2) if len(nums1) <= len(nums2) else (nums2, nums1)
    shorter_length = len(shorter_list)
    longer_length = len(longer_list)
    midpoint: int = (shorter_length + longer_length + 1) // 2

    # When we start traversing to find the correct partition, we begin at index 0 and will iterate up to the
    # length of the list. This is because we won't need to traverse the whole longer list, just the median.
    # If the midpoint is odd, we floor it to make sure we grab all the indexes we need to traverse.
    # Shorter needs to error on the left side of the sorted list and work in
    shorter_start_index = 0
    shorter_end_index = len(shorter_list)

    while shorter_start_index <= shorter_end_index:
        shorter_midpoint = (shorter_start_index + shorter_end_index) // 2
        longer_midpoint = midpoint - shorter_midpoint

        if shorter_midpoint < shorter_length and nums2[longer_midpoint - 1] > nums1[shorter_midpoint]:
            shorter_start_index = shorter_midpoint + 1
        elif shorter_midpoint > 0 and nums1[shorter_midpoint - 1] > nums2[longer_midpoint]:
            shorter_end_index = shorter_midpoint - 1
        else:
            if shorter_midpoint == 0:
                max_of_left = nums2[longer_midpoint - 1]
            elif longer_midpoint == 0:
                max_of_left = nums1[shorter_midpoint - 1]
            else:
                max_of_left = max(nums1[shorter_midpoint - 1], nums2[longer_midpoint - 1])

            if (shorter_length + longer_length) % 2 == 1:
                return max_of_left

            if shorter_midpoint == shorter_length:
                min_of_right = nums2[longer_midpoint]
            elif longer_midpoint == longer_length:
                min_of_right = nums1[shorter_midpoint]
            else:
                min_of_right = min(nums1[shorter_midpoint], nums2[longer_midpoint])

            return (max_of_left + min_of_right) / 2.0

        print("Iterating...")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass
