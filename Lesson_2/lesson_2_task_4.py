def fizz_buzz():
    n = input("Введите число: ")
    n_int = int(n)
    if (n_int % 3 == 0) and (n_int % 5 == 0):
        print("FizzBuzz")
    elif n_int % 3 == 0:
        print("Fizz")
    elif n_int % 5 == 0:
        print("Buzz")
   
    else:
        print(n_int)
fizz_buzz()