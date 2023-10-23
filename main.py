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


def count_smaller_n_log_n(numbers):
    """
    O(n * log(n)) solution, better than O(n^2). More complex and is recursive so hard to understand/debug
    This is the container function that calls the internal recursive merge_sort_with_count function.

    :param numbers: Array of numbers
    :return: Array of counts, where a +1 is the number of smaller elements to the right of nums[i]
    """

    def _merge_sort_with_count(number_list: List[int]) -> (List[int], List[int]):
        list_size = len(number_list)

        # Return 0 for empty list
        if list_size <= 1:
            return number_list, [0]

        # Chop in half to get O(n * log(n)), and floor to an int to get a usable index. We recursive chop it in half.
        mid = list_size // 2
        left_split = number_list[:mid]
        right_split = number_list[mid:]

        # This at the deepest call in the recursive call stack, will return a 2 element list, and a count of 0 if
        # the list has 2 equal numbers, otherwise a count of 1. The 2 elements will be sorted via merge sort.
        left, left_counts = _merge_sort_with_count(left_split)
        right, right_counts = _merge_sort_with_count(right_split)

        left_count, right_count = 0, 0
        merged = []
        merged_counts = []

        left_list_size = len(left)
        right_list_size = len(right)

        while left_count < left_list_size and right_count < right_list_size:

            # Bug happens on second iteration. We need the count array to be the same length as the merged array.
            left_element: int = left[left_count]
            right_element: int = right[right_count]

            if right_element < left_element:
                merged.append(left_element)

                # This is where we keep count of the smaller elements to the right of numbers[i]
                current_smaller_than_count: int = left_counts[left_count]
                new_smaller_than_count: int = current_smaller_than_count + 1

                merged_counts.append(new_smaller_than_count)

                left_count += 1
            else:
                merged.append(right_element)

                new_smaller_than_count: int = 0

                merged_counts.append(new_smaller_than_count)

                right_count += 1

        merged_counts += right_counts[right_count:]
        merged += left[left_count:]

        merged_with_counts = (merged, merged_counts)

        return merged_with_counts

    _, result = _merge_sort_with_count(numbers)
    return result


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
