# Napisz funkcję o nazwie objętość_kuli, która przyjmuje promień kuli i zwraca jej objętość zaokrągloną do 2 dp. (
# Google wzór na objętość kuli, użyj pi = 3,14)

pi = 3.14


def volume_of_sphere(r):
    return round(((4 / 3) * pi * r ** 3), 2)
