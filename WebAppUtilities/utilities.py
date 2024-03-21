def isOverlap(v1, v2):
    return 
def checkCompability(shape_segments, color_ranges):
    for i in range(len(shape_segments)):
        for j in range(len(shape_segments)):
            if i != j and shape_segments[i] == shape_segments[j]:
                if isOverlap(color_ranges[i], color_ranges[j]):
                    return False, i, j
    return True, 0, 0

