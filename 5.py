import math

input_number = int(input())

if input_number < 0:
    print('not found')
else:
    square_root = math.sqrt(input_number)
    print(round(square_root, 1))
