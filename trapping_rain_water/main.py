from typing import List


def trap(heights: List[int]) -> int:
    """
    Given n non-negative integers representing an elevation map where the width of each bar is 1, 
    compute how much water it can trap after raining.
    
    Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
    Output: 6
    Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
    In this case, 6 units of rain water (blue section) are being trapped.
    
    :param heights:
    
    :return: "Area" of water trapped
    """

    # Catch edge-case and return 0 if there is no height to trap water.
    # We do not trap water on the 0's until we encounter a number > 0, y-axis does not trap water.
    if len(heights) == 0:
        return 0

    index = 0
    stored_water = 0
    previous_height = heights[index]

    while index < len(heights):
        # Inspect and store the current height.
        current_height = heights[index]

        # We need to calculate based on heights, not keep count as we go.
        # If slope down then up we trap water. We loop backwards in the array to find the point at our height
        # sum the counts if the next point is also up, we look back until we find out height and sum the counts

        # If current > previous we hit a slope up. We can potentially hold water.
        if previous_height < current_height:
            potential_water = 0
            inspecting_index = index - 1

            # We look backwards. Examples are easier than explaining.
            # If we are N high, we look backwards until we find N and sum the distance count,
            # Then we decrease to N-1 and do the same thing until we find a matching N-1 height and sum.
            # Do until height 0.
            # At index 3, we have height 2. First look back to 0 and see if we see another height 2.
            while inspecting_index > 0:
                

                inspecting_index -= 1

            inspecting_index -= 1

        previous_height = current_height
        index += 1

    return stored_water


def test_trap():
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

    assert trap(height) == 6
