def isOverlap(v1, v2):
    """
    Check if two ranges overlap.

    Args:
        x (tuple): First range (start, stop).
        y (tuple): Second range (start, stop).

    Returns:
        bool: True if the ranges overlap, False otherwise.
    """
    return not (v2[1] < v1[0] or v2[1] < v2[0])

def checkCompability(shape_segments, color_ranges):
    for i in range(len(shape_segments)):
        for j in range(len(shape_segments)):
            if i != j and shape_segments[i] == shape_segments[j]:
                if isOverlap(color_ranges[i], color_ranges[j]):
                    return False, i, j
    return True, 0, 0

