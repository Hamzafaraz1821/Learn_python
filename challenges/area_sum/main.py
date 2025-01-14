def area(height, width):
    return height * width


def area_sum(rectangles):
    area_s = 0
    for a in rectangles:
        area_s += area(a["height"],a["width"])

    return area_s