
"""
Пользователь вводит строку, содержащую два слова. 
Приложение выводит их в обратном порядке. Пример:

Harry Potter
Potter Harry
"""

str1 = input("Input string: ")
# спочатку стр1 від індексу першого пробілу + 1 до кінця строки, потім від початку строки 
# до індексу першого пробілу
print(str1[str1.find(' ') + 1:], str1[:str1.find(' ')])