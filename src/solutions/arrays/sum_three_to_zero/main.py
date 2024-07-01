import math
from typing import List
from loguru import logger


def sum_to_zero(numbers: List[int]) -> List[int]:
    # O(n^2) approach
    first_index = 0
    current_index = 1
    last_index = len(numbers) - 1

    while current_index < last_index and first_index < last_index:
        first_item = numbers[first_index]
        next_item = numbers[current_index]
        last_item = numbers[last_index]

        total = first_item + next_item + last_item

        if total == 0:
            return [first_item, next_item, last_item]

        current_index += 1

        if current_index == last_index:
            # Reached end of list, increment first and try again
            first_index += 1

    raise ValueError("No solution found")


def sum_to_zero_fast(numbers: List[int]) -> List[int]:
    # O(n log n) approach
    enumerated = list(enumerate(numbers))
    length = len(numbers)

    sorted_list = sorted(enumerated, key=lambda tup: tup[1])

    for index in range(length - 2):
        current_item = sorted_list[index]
        current_value = current_item[1]

        # If we are at the beginning skip duplicate check as we would go out of bounds
        if index > 0:
            # skip duplicate values
            previous_value = sorted_list[index - 1][1]

            if current_value == previous_value:
                continue
        else:
            continue

        start_index = index + 1
        right_index = length - 1

        while start_index < right_index:
            left_item = sorted_list[start_index]
            left_value = left_item[1]

            right_item = sorted_list[right_index - 1]
            right_value = right_item[1]

            total = current_value + left_value + right_value

            if total == 0:
                items = [left_item, current_item, right_item]
                original_order = sorted(items, key=lambda item: item[0])
                original_list = [item[1] for item in original_order]

                return original_list

            elif total < 0:
                start_index += 1
            else:
                right_index -= 1

    raise ValueError("No solution found")


def test_sum_to_zero():
    numbers = [3, 5, 8, 10, -9, -11]

    result = sum_to_zero(numbers)

    assert result == [3, 8, -11]
