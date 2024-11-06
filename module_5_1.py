# Task  "Developer - не только разработчик"



class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to (self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            for i in range (1, (new_floor+1)):
                print(i)


H1 = House('ЖК Эльбрус', 30)
H2 = House('Вилла', 3)

print(H1.name, H1.number_of_floors)
print(H2.name, H2.number_of_floors)
H1.go_to(7)
H2.go_to(3)

H1.go_to(0)
H2.go_to(12)