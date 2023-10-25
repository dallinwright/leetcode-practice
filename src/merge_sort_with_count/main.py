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

    def count_smaller(nums):
        if not nums:
            return []

        def sort(enum):
            half = len(enum) // 2

            if half:
                left, right = sort(enum[:half]), sort(enum[half:])
                for i in range(len(enum) - 1, -1, -1):
                    if not right or left and left[-1][1] > right[-1][1]:
                        smaller[left[-1][0]] += len(right)
                        enum[i] = left.pop()
                    else:
                        enum[i] = right.pop()
            return enum

        smaller = [0] * len(nums)
        sort(list(enumerate(nums)))
        return smaller

    return count_smaller(numbers)


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
