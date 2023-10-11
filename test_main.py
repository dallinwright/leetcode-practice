from main import Solution


def test_find_median_sorted_arrays_even():
    nums1 = [1, 2]
    nums2 = [3, 4]

    solution = Solution()
    output = find_median_sorted_arrays(nums1, nums2)

    assert output == 2.5


def test_find_median_sorted_arrays_uneven():
    nums1 = [1, 3]
    nums2 = [2]

    solution = Solution()
    output = find_median_sorted_arrays(nums1, nums2)

    assert output == 2.0
