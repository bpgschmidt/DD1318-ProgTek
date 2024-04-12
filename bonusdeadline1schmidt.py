# rectangle area
def rectangle_area(height, width):
    area = height * width
    return area


# rectangle circumference
def rectangle_circumference(height, width):
    circumference = 2 * height + 2 * width
    return circumference


# third character of string
def third_character_of_string(string):
    count = 0
    for letter in string:
        count += 1
        if count == 3:
            return letter
    if count < 3:
        return "False"

