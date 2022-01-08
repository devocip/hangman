import csv
from random import choice


def hangman(word):
    wrong = 0
    stages = ["",
              "________      ",
              "|      |      ",
              "|      |      ",
              "|      O      ",
              "|     /|\     ",
              "|     / \     ",
              "|             "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Добро пожаловать на казнь!")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "Введите букву: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("Вы выйграли! Было загадано слово: ")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong]))
        print("Вы проиграли! Было загадано слово: {}.".format(word))


with open("spisok_slov.csv", "r") as f:
    r = csv.reader(f, delimiter=";")
    for i in r:
        spisok_slov = (";".join(i).split(';'))

hangman(choice(spisok_slov))
