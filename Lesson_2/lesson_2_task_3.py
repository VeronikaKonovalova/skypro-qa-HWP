import math
def square():
    side = input("Введите сторону квадрата:")
    side_int = float(side)
    S = side_int * side_int
    
    print("Площадь квадрата: ", end = "")
    print(math.ceil(S))
square()