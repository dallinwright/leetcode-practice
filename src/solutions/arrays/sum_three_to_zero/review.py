import math
from typing import List

from loguru import logger


def sum_to_zero(numbers: List[int]):
    numbers.sort()

    middle_index = math.floor(len(numbers) / 2)

    left_index = 0
    right_index = len(numbers) - 1

    while left_index < middle_index < right_index:

        left_element = numbers[left_index]
        right_element = numbers[right_index]
        middle_element = numbers[middle_index]

        total = left_element + middle_element + right_element

        if total == 0:
            return [left_element, middle_element, right_element]
        else:
            if total > 0:
                right_index -= 1
            else:
                left_index += 1

    return []


def test_sum_to_zero():
    numbers = [1, 3, 5, 8, -14, -22, -3]

    assert sum_to_zero(numbers) == []

    numbers_two = [1, 3, 5, 8, -11]

    assert sum_to_zero(numbers_two) == [-11, 3, 8]
