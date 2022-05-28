
"""
Доработать приложение из предыдущей задачи так, чтобы 
программа исправляла регистр символов. Пример:

Фамилия: ерШоВ
Имя: андрей
Отчество: петрович

Ершов А. П.


"""

lastname = input("LastName: ")
firstname = input("FirstName: ")
middlename = input("MiddleName: ")

print(f"{lastname.title()} {firstname[0].title()}. {middlename[0].title()}.")