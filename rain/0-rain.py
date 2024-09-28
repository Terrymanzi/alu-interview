#!/usr/bin/python3
"""Check readme for full description"""


def rain(walls):
    """Rain function"""
    water_retained = 0

    if not isinstance(walls, list) or len(walls) < 3:
        return 0

    # The left and right max at each index
    length = len(walls)
    left, right = [0] * length, [0] * length

    # Compute the values of those maxes using if conditions instead of max()
    left[0] = walls[0]
    for i in range(1, length):
        if left[i-1] > walls[i]:
            left[i] = left[i-1]
        else:
            left[i] = walls[i]

    right[length-1] = walls[length-1]
    for i in range(length-2, -1, -1):
        if right[i + 1] > walls[i]:
            right[i] = right[i + 1]
        else:
            right[i] = walls[i]

    # Compute the water retained at each index
    for i in range(len(walls)):
        water_retained += min(left[i], right[i]) - walls[i]

    return water_retained
