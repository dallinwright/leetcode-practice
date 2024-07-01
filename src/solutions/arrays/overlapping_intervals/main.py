def merge(numbers: list[(int, int)]):
    left = None
    right = None

    for numbers in numbers:
        if left is None:
            left = numbers[0]

        if right is None:
            right = numbers[1]

        if numbers[0] < left:
            left = numbers[0]

        if numbers[1] > right:
            right = numbers[1]

    return left, right


def test_merge():
    intervals = [(1, 5), (3, 7), (4, 6), (6, 8)]

    result = merge(intervals)

    assert result == (1, 8)
