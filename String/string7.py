
"""
Пользователь вводит строку и два слова. Приложение заменяет все вхождения первого слова на второе. Пример:

> To be or not to be.
Find: be
Replace: eat

To eat or not to eat.
"""

str1 = input("Input string: ")
find1 = input("Find: ")
replace1 = input("Replace: ")

print(str1.replace(find1, replace1))
