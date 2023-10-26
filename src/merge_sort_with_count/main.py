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


def count_smaller_n_log_n(numbers: List[int]) -> List[int]:
    """
    O(n * log(n)) solution, better than O(n^2). More complex and is recursive, so hard to understand/debug
    This is the container function that calls the internal recursive merge_sort_with_count function. This is the
    fastest you are realistically going to get in python, and one of the better solutions for this problem.
    You can improve it even further by multithreading it, but python does not handle that well with the global
    interpreter lock and all that jazz, so I am not going to bother.

    :param numbers: Array of numbers
    :return: Array of counts, where a +1 is the number of smaller elements to the right of nums[i]
    """
    if not numbers:
        return []

    def sort(data):
        split_point = len(data) // 2

        if split_point:
            left_half = sort(data[:split_point])
            right_half = sort(data[split_point:])

            index = len(data) - 1
            continue_until_value = -1

            # This is the key part. We are going to iterate backwards through the list, and we are going to
            # iterate in reverse order, and go until we hit the element at index 0.
            while index > continue_until_value:
                # If the right half is empty
                if not right_half:
                    left_last_element = left_half[-1]
                    left_last_element_index = left_last_element[0]

                    smaller_counts[left_last_element_index] += len(right_half)
                    data[index] = left_half.pop()

                # If the left half still has items and the last element of the left half is
                # greater than the last element of the right half
                elif left_half:
                    # The first -1 takes the last element in the array, for example (2, 6) and the [1] takes the 6
                    # the 2 in this case would be the index in the original list, and the 6 is the value
                    left_last_element = left_half[-1]
                    left_last_element_value = left_last_element[1]

                    right_last_element = right_half[-1]
                    right_last_element_value = right_last_element[1]

                    if left_last_element_value > right_last_element_value:
                        left_last_element_index = left_last_element[0]
                        smaller_counts[left_last_element_index] += len(right_half)
                        data[index] = left_half.pop()
                    else:
                        data[index] = right_half.pop()
                else:
                    data[index] = right_half.pop()

                index -= 1

        return data

    # We from the start create the list that will be modified in place; this is the list that will be returned
    # at the end of the function
    smaller_counts = [0] * len(numbers)

    # Used to create a list of tuples where the first element of the tuple is the index
    # and the second element is the value from the original list
    index_with_number = enumerate(numbers)

    # We then take the enumerated object and convert it to a list of tuples, basically a python-specific thing
    aggregate = list(index_with_number)

    # The recursive function that does the actual counting and sorting, it will again modify in place the smaller_counts
    sort(aggregate)

    return smaller_counts


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
