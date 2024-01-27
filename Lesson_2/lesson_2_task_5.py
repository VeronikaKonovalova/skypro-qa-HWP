def month_to_season():
    month = input("Введите номер месяца (1-12): ")
    month_int = int(month)
    if month_int > 11:
        month_int = 0
    if month_int > 8:
            print("Осень") 
    elif month_int > 5:
           print("Лето") 
    elif month_int > 2:
        print("Весна")
    else:
           print("Зима")
month_to_season()