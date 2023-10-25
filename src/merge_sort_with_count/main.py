"""
Given an integer array nums, return an integer array counts where counts[i] is the number of smaller elements to
the right of nums[i].

Example 1:

Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5, there are two smaller elements (2 and 1).
To the right of 2, there is only one smaller element (1).
To the right of 6, there is one smaller element (1).
To the right of 1, there are zero smaller elements.
"""
import math
from typing import List

from src.config.app_logger import logger


def count_smaller_n_squared(numbers):
    """
    O(n^2) solution, not ideal but the most simple. This is the first stop people will do when given this problem.
    It fulfills the requirement with the least work, the least expertise, and least familiarity required
    with the problem. It is also the slowest, hence why it is a good interview question to see if the candidate
    can even code the solution, then how they attempt to improve it if they can. It is very deceptive, because it is
    easy to code, but hard to improve.

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
    This is the container function that calls the internal recursive merge_sort_with_count function. This is the
    fastest you are realistically going to get in python, and one of the better solutions for this problem.
    You can improve it even further by multithreading it, but python does not handle that well with the global
    interpreter lock and all that jazz, so I am not going to bother.

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

        left_index = 0
        right_index = 0
        left_size = len(left)
        right_size = len(right)
        merged = []
        merged_counts = [0] * (left_size + right_size)

        # Very strange, very strange indeed.
        # We must compare each element in the left to each element in the right, this breaks from the regular merge-sort
        # algo.
        while left_index < left_size and right_index < right_size:
            left_element: int = left[left_index]
            right_element: int = right[right_index]

            if right_element < left_element:
                merged.append(right_element)

                right_index += 1
            else:
                merged.append(left_element)

                left_index += 1

        if left_index < left_size:
            merged = merged + left[left_index:]
        elif right_index < right_size:
            merged = merged + right[right_index:]

        # We had to inspect and compare both arrays which are sorted and essentially zipper them.
        # That means we inspected and compared every element already.
        # We MUST compare every left element to every right
        # until we hit the end OR we hit a right element > than a left element.
        index = 0

        # TODO shortcircuit delete
        if left == [2, 5]:
            logger.info("delete me")

        while index < left_size:
            sub_index = 0
            left_element: int = left[index]
            left_count: int = left_counts[index]

            while sub_index < right_size:
                right_element: int = right[sub_index]

                if right_element < left_element:
                    merged_counts[index] += left_count + 1

                sub_index += 1

            index += 1

        for count in right_counts:
            merged_counts[index] = count
            index += 1

        merged_with_counts = (merged, merged_counts)

        return merged_with_counts

    sorted_numbers, counts = _merge_sort_with_count(numbers)

    return counts


def test_count_smaller_n_squared():
    numbers = [1, 2]
    expected = [0, 0]

    results = count_smaller_n_squared(numbers)

    assert results == expected


def test_small_list_already_ordered():
    numbers = [1, 2]
    expected = [0, 0]

    results = count_smaller_n_log_n(numbers)

    assert results == expected


def test_small_list_not_ordered():
    numbers = [5, 2, 6]
    expected = [1, 0, 0]

    results = count_smaller_n_log_n(numbers)

    assert results == expected


def test_medium_list_not_ordered():
    numbers = [5, 2, 6, 1]
    expected = [2, 1, 1, 0]

    results = count_smaller_n_log_n(numbers)

    assert results == expected


def test_large_list_not_ordered():
    numbers = [5, 2, 6, 1, 3, 4]
    expected = [4, 1, 3, 0, 0, 0]

    results = count_smaller_n_log_n(numbers)

    assert results == expected


def test_medium_list_already_ordered():
    numbers = [1, 2, 3, 4, 5]
    expected = [0, 0, 0, 0, 0]

    results = count_smaller_n_log_n(numbers)

    assert results == expected
