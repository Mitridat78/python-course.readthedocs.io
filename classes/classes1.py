"""
Создать класс, описывающий человека. Должны быть поля для имени,
 фамилии и возраста. Создать экземпляр и вывести информацию о человеке
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return (f"Name: {self.name}, Age: {self.age}")


pers = Person("Jonh", 20)
#pers.name = "James"
#pers.age = 45
print(pers)

        