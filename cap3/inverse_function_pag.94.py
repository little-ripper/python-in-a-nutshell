from math import sin, asin ,cos, acos, tan, atan, log, exp
def add_inverse(i_dict):
    for f in list(i_dict):
        print(i_dict)
        i_dict[i_dict[f]] = f

math_map = { sin: asin, cos:acos, tan:atan, log:exp }
# print(math_map)
add_inverse(math_map)
# print(math_map)
