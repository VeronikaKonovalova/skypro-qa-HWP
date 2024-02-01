from smartphone import Smartphone

iphone = Smartphone("iphone", "15pro", +79991112233)
samsung = Smartphone("samsung", "galaxy" , +79557872665)
motorola = Smartphone("motorola", "1234" , +79777777777)
iphone3 = Smartphone("iphone3", "3" , +791231234545)
huawei = Smartphone("huawei", "p30pro" , +79990000000)

catalog = [iphone, samsung, motorola, iphone3, huawei]

for tel in catalog:
    print(tel.marka, "-", tel.model,".", tel.number)