from sorted_array_ologn.main import find_median_sorted_lists


def test_find_median_sorted_arrays_even():
    nums1 = [6, 10]
    nums2 = [1, 2, 3, 4, 5, 7, 8, 9, 11, 12, 13]

    output = find_median_sorted_lists(nums1, nums2)

    assert output == 6.5


def test_find_median_sorted_arrays_uneven():
    nums1 = [1, 5]
    nums2 = [2]

    output = find_median_sorted_lists(nums1, nums2)

    assert output == 2.0


def test_find_median_sorted_arrays_decimal():
    nums1 = [1, 5]
    nums2 = [0, 4]

    output = find_median_sorted_lists(nums1, nums2)

    assert output == 2.5
