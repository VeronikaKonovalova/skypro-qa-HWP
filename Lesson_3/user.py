class User:

    def __init__(self, first_name, last_name):
       self.first_name = first_name
       self.last_name = last_name

    def sayName(self):
        print("Имя: ", self.first_name)

    def sayLastname(self):
        print("Фамилия: ", self.last_name)

    def sayFrstLst(self):
        print("Фамилия и имя: ", self.last_name, self.first_name) 
