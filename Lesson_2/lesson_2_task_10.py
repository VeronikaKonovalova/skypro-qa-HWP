x = input("Введите сумму вклада: ")
y = input("Введите количество лет: ")
x_int = int(x)
y_int = int(y)
for i in range(1 ,y_int + 1):
    x_int = x_int*1.1
x_str =str(x_int)
print("На Вашем счету:" + x_str)