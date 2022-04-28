import math
test_h = int(input("height of wall: "))
test_w = int(input("width of wall: "))

coverage = 5


def paint_calc(height, width, cover):
    number_of_cans = math.ceil((height * width) / cover)
    print(f"You'll need {number_of_cans} cans of paint.")


paint_calc(height=test_h, width = test_w, cover = coverage)
