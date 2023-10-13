# This is a sample Python script.
from CwiczeniaPierwsze.Zadanie1 import check_range, bool_range
from CwiczeniaPierwsze.Zadanie2 import unique_list
from CwiczeniaPierwsze.Zadanie3 import volume_of_sphere
from CwiczeniaPierwsze.Zadanie4 import num_fact


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Zadanie 1
    print('Zadanie 1')
    print(check_range(34, 9, 228))
    print(check_range(7, 2, 5))

    print(bool_range(7, 5, 20))
    print(bool_range(67, 22, 25))

    # Zadanie 2
    print('Zadanie 2')
    my_list = [1, 3, 5, 6, 4, 3, 2, 3, 3, 4, 3, 4, 5, 6, 6, 4, 3, 2, 12, 3, 5, 63, 4, 5, 3, 3, 2]

    print(unique_list(my_list))
    print(set(my_list))

    # Zadanie 3
    print('Zadanie 3')
    print(volume_of_sphere(2))

    # Zadanie 4
    print('Zadanie 4')
    print(num_fact(10))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
