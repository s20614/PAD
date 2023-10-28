'''
Zadanie 5 (4 pkt)
Napisz klasę FunkcjaKwadratowa, która przechowuje funkcje typu $ax^2$+bx+c.
Klasa powinna zawierać trzy pola: a, b, c, które są przypisywane w konstruktorze.
Główną metodą powinna być rozwiaz(), która zwraca miejsca zerowe podanej funkcji.
Należy zwrócić uwagę na przypadki gdy a=0, b=0 lub c=0,
a także obmyślić sposób informowania o nieskończonej liczbie, jednym lub zerze rozwiązań.
'''

'''
początek kodu dla ułatwienia

'''


class FunkcjaKwadratowa:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def wypisz(self):
        print(f"A = {self.a}, B = {self.b} C = {self.c} ")

    def oblicz_wartosc(self, x):
        return self.a * x ** 2 + self.b * x + self.c

    def rozwiaz(self):
        if self.numbers_not_zero() == True:
            delta = self.b ** 2 - 4 * self.a * self.c
            if delta < 0:
                return f"Delta jest równa {delta}, co znaczy, że nie ma rozwiązań rzeczywistych"
            elif delta == 0:
                x = self.oblicz_x()
                return f"Równanie posiada 1 punkt zerowy: X = {x}"
            elif delta > 0:
                x1 = self.oblicz_x1(delta)
                x2 = self.oblicz_x2(delta)
                return f"Równanie posiada 2 punkty zerowe X1 = {x1} X2 = {x2}"
        else:
            return "Równanie posiada nieskończona liczbę rozwiazań"

    def oblicz_x1(self, d):
        return (-self.b - (d ** 0.5)) / 2 * self.a

    def oblicz_x2(self, d):
        return (-self.b + (d ** 0.5)) / 2 * self.a

    def oblicz_x(self):
        return -self.b / (2 * self.a)

    def numbers_not_zero(self):
        if self.a == 0 or self.b == 0 or self.c == 0:
            return False
        elif self.a == 0:
            return False
        else:
            return True


def main():
    f1 = FunkcjaKwadratowa(2, 3, 1)
    f1.wypisz()
    print(f1.oblicz_wartosc(0))
    print(f1.oblicz_wartosc(1))

    print(FunkcjaKwadratowa(0, 0, 0).rozwiaz())
    print(FunkcjaKwadratowa(0, 0, 1).rozwiaz())
    print(FunkcjaKwadratowa(0, 2, 3).rozwiaz())
    print(FunkcjaKwadratowa(1, 2, 3).rozwiaz())
    print(FunkcjaKwadratowa(1, -5, 6).rozwiaz())
    print(FunkcjaKwadratowa(1, 4, 4).rozwiaz())


if __name__ == "__main__":
    main()
