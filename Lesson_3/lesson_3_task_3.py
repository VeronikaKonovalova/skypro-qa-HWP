from Adress import Address
from Mailing import Mailing

to_a = Address(111111, "Moscow", "Perovskaya", 455, 56)
from_a = Address(123123, "London", "Baker Street", 221, 13)
mail = Mailing(to_a, from_a, 1500, "aa2223344")

#mail.post()
print("Отправление", mail.track, "из", to_a.index,",",to_a.city,",", to_a.street,",",
       to_a.home,"-",to_a.flat,"в",from_a.index,",",from_a.city,",", from_a.street,",",
       from_a.home,"-",from_a.flat,". Стоимость", mail.cost,"рублей.")
