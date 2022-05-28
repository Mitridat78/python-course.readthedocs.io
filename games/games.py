"""
Используя шаблон проекта, реализуйте игры «Камень, ножницы, бумага» и «Угадай число»
"""
import easygui


def rock_paper_scissors():
    #easygui.msgbox('Здесь будет игра "Камень, ножницы, бумага"')
    easygui.integerbox('Введите число (от 1 до 3)', 1, 3)


def guess_the_number():
    easygui.msgbox('Здесь будет игра "Угадай число"')


games = [
    'Камень, ножницы, бумага',
    'Угадай число',
    'Выход'
]

games_entry_points = [
    rock_paper_scissors,
    guess_the_number
]

while True:
    res = easygui.buttonbox('Выбери игру!', choices=games)
    if res == games[2]:
        break
    games_entry_points[games.index(res)]()
