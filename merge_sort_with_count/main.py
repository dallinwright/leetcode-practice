'''
Given an integer array nums, return an integer array counts where counts[i] is the number of smaller elements to the right of nums[i].
de


Example 1:

Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Example 2:

Input: nums = [-1]
Output: [0]
Example 3:

Input: nums = [-1,-1]
Output: [0,0]
'''
import copy
import math
from typing import List

NUMBERS = [1, 2]
EXPECTED = [0, 0]


def count_smaller_n_squared(numbers):
    """
    O(n^2) solution, not ideal but the most simple.

    :param numbers: Array of numbers
    :return: Array of counts, where a +1 is the number of smaller elements to the right of nums[i]
    """
    sub_index = 1
    results = []

    for index, number in enumerate(numbers):
        smaller_than_count = 0
        remaining_numbers = numbers[sub_index:]

        for sub_number in remaining_numbers:
            if sub_number < number:
                smaller_than_count += 1

        results.append(smaller_than_count)

        sub_index += 1

    return results


def count_smaller_n_log_n(numbers) -> List[int]:
    """
    O(n * log(n)) solution, better than O(n^2). More complex and is recursive, so hard to understand/debug
    This is the container function that calls the internal recursive merge_sort_with_count function.

    :param numbers: Array of numbers
    :return: Array of counts, where a +1 is the number of smaller elements to the right of nums[i]
    """

    def _merge_sort_with_count(number_list: List[int]) -> (List[int], List[int]):
        list_size = len(number_list)

        # Return 0 for an empty or 1 length list
        if list_size <= 1:
            return number_list, [0]

        # Chop in half to get O(n * log(n)), and floor to an int to get a usable index. We recursively chop it in half.
        mid = math.ceil(list_size / 2)
        # mid = list_size // 2
        left_split = number_list[:mid]
        right_split = number_list[mid:]

        # This at the deepest call in the recursive call stack will return a 2-element list, and a count of 0 if
        # the list has 2 equal numbers, otherwise a count of 1. The 2 elements will be sorted via merge sort.
        left, left_counts = _merge_sort_with_count(left_split)
        right, right_counts = _merge_sort_with_count(right_split)

        left_list_size = len(left)
        right_list_size = len(right)

        left_index, right_index = 0, 0
        merged = []
        # This will fixed-length list where we store counts as we progress through the merge sort
        merged_counts = [0] * (left_list_size + right_list_size)

        # This is the merge sort part, we go until one array is emptied
        while left and right:
            # Select the smallest value from the front of each list (excluding values already in the sorted array)
            left_element: int = left[left_index]
            right_element: int = right[right_index]

            # Select the minimum of the two values
            if right_element < left_element:
                # Since the right element is smaller, we append that element next to the list
                merged.append(right_element)
                right.pop(0)

                merged_counts[right_index + 1] = right_counts[right_index] + 1
                right_counts.pop(0)

                # We need to match the list, if we were [5, 1] and sorted becomes [1, 5] the count should be [0, 1]
                right_index += 1
            else:
                # Add the selected value to the sorted array
                merged.append(left_element)
                left.pop(0)
                left_counts.pop(0)

                left_index += 1

        merged_length = len(merged)

        # TODO so this still throws a new bug, we are now double counting...
        if left_index == left_list_size:
            for remaining_index in range(right_index, right_list_size):
                remaining_element = right[right_index]

                merged_index = remaining_index + merged_length
                current_count = merged_counts[merged_index]

                for sub_index in range(merged_length):
                    picked_element = merged[sub_index]

                    if picked_element > remaining_element:
                        current_count += 1
                        merged_counts[merged_index] = current_count

                merged.append(remaining_element)

            merged += right[right_index:]
        else:
            for remaining_index in range(left_index, left_list_size):
                remaining_element = left[remaining_index]

                merged_index = remaining_index + merged_length
                current_count = merged_counts[merged_index]

                for sub_index in range(merged_length):
                    picked_element = merged[sub_index]

                    if picked_element > remaining_element:
                        current_count += 1
                        merged_counts[merged_index] = current_count

                merged.append(remaining_element)

        merged_with_counts = (merged, merged_counts)

        return merged_with_counts

    sorted_numbers, counts = _merge_sort_with_count(numbers)

    return counts


def test_count_smaller_n_squared():
    results = count_smaller_n_squared(NUMBERS)

    assert results == EXPECTED


def test_small_list_already_ordered():
    numbers = [1, 2]
    expected = [0, 0]

    results = count_smaller_n_log_n(numbers)

    assert results == expected


def test_small_list_not_ordered():
    numbers = [2, 1]
    expected = [1, 0]

    results = count_smaller_n_log_n(numbers)

    assert results == expected


def test_medium_list_already_ordered():
    numbers = [1, 2, 3, 4, 5]
    expected = [0, 0, 0, 0, 0]

    results = count_smaller_n_log_n(numbers)

    assert results == expected


def test_medium_list_not_ordered():
    numbers = [2, 5, 1, 6, 4, 3]
    expected = [1, 3, 0, 2, 1, 0]

    results = count_smaller_n_log_n(numbers)

    assert results == expected
