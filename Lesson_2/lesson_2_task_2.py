def is_year_leap():
    year = input("Введите год:")
    year_int = int(year)
    if year_int % 4 == 0:
        print("Год " + year + ": True")
    else: print("Год " + year + ": False")
is_year_leap()