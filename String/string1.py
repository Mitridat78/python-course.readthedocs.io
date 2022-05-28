
"""
Пользователь вводит фамилию, имя и отчество. Приложение должно 
вывести фамилию и инициалы. Пример:

Фамилия: Ершов
Имя: Андрей
Отчество: Петрович

Ершов А. П.
"""

lastname = input("LastName: ")
firstname = input("FirstName: ")
middlename = input("MiddleName: ")

print(f"{lastname} {firstname[0]}. {middlename[0]}.")