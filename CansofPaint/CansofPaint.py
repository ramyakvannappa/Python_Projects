import math

def paint_calc(height, width, cover):
    cans_of_paint = height * width / cover
    up_number_cans_of_paint = math.ceil(cans_of_paint) # to UP the value to nearest higher integer
    print(f"You'll need {up_number_cans_of_paint} cans of paint")


height_ip = float(input("Enter the height of the wall in m \n"))
width_ip = float(input("Enter the width of the wall in m \n"))
coverage_ip = 5 # 1 can of paint can cover 5 square meters

paint_calc(height = height_ip, width = width_ip, cover = coverage_ip)