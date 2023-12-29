import numpy as np


class IllegalFormulaError(Exception):
    "Raised when input from user has bigger length than 3"
    pass


def do_math(x1, x2, op):
    match op:
        case '/':
            wynik = x1 / x2
        case '*':
            wynik = x1 * x2
        case '+':
            wynik = x1 + x2
        case '-':
            wynik = x1 - x2
        case _:
            raise IllegalFormulaError("To nie jest operator")
    return wynik


if __name__ == '__main__':
    userInput = 'User input'
    while userInput != 'KONIEC':
        userInput = input("Podaj input w formacie liczba operator liczba (pamiętaj o spacji): ")
        listFromInput = userInput.split(' ')
        if len(listFromInput) != 3:
            raise IllegalFormulaError("Raised when input from user has bigger length than 3")
        print(listFromInput)
        try:
            x1 = float(listFromInput[0])
            x2 = float(listFromInput[2])
        except ValueError:
            raise IllegalFormulaError("1 i 3 wartość muszą być liczbam")

        print(do_math(x1, x2, listFromInput[1]))

# if __name__ == '__main__':
# arr = np.array([1, 2, 3, 4, 5])
# arr0 = np.zeros(10, dtype=int)
# arr1 = np.ones((3,2), dtype=float)
# # Zadanie 1
# print(arr)
# print(arr0)
# print(arr1)
