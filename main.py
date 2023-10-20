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

NUMBERS = [5, 2, 6, 1]
EXPECTED = [2, 1, 1, 0]


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
    def merge_sort_with_count(number_list):
        # Return 0 for empty list
        if len(number_list) <= 1:
            return number_list, []

        # Chop in half to get o nlogn, and floor to an int to get index. We recursive chop it in half.
        mid = len(number_list) // 2
        left_split = number_list[:mid]
        right_split = number_list[mid:]

        left, remaining_count = merge_sort_with_count(left_split)
        right, right_counts = merge_sort_with_count(right_split)

        merged, merged_counts = [], []
        left_count, right_count = 0, 0

        while left_count < len(left) and right_count < len(right):
            # If left element at count is > right element at count, merge sort and append
            left_element = left[left_count]
            right_element = right[right_count]

            if left_element > right_element:
                merged.append(right_element)

                remaining_left = len(left) - left_count

                if right_count:
                    element = right_counts[right_count] + remaining_left
                else:
                    element = remaining_left

                # print(f"appending to merge count: {element}")
                merged_counts.append(element)

                # print(f"merged_counts: {merged_counts}")
                right_count += 1
            else:
                left_element = left[left_count]

                # print(f"left element: {left_element}")
                merged.append(left_element)

                # print(f"Current Merged: {merged}")
                remaining_right = len(right_counts) - right_count

                # print(f"remaining_right: {remaining_right}")
                # print(f"Merged in right > left: {merged}")
                # print(f"right_counts: {right_counts}, right_count: {right_count}")

                element = right_counts[remaining_right]
                merged_counts.append(element)

                left_count += 1

        merged += left[left_count:]
        merged_counts += right_counts[right_count:]

        return merged, merged_counts

    _, result = merge_sort_with_count(numbers)
    return result


def test_count_smaller_n_squared():
    results = count_smaller_n_squared(NUMBERS)

    assert results == EXPECTED


def test_count_smaller_n_log_n():
    results = count_smaller_n_log_n(NUMBERS)

    assert results == EXPECTED

