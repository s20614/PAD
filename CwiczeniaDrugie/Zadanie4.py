'''
Zadanie 4 (2 pkt)
Wykorzystaj klasy Autobus i Pojazd.
Zdefiniuj metodę opłata, k†óra będzie miała wartość domyślną liczba_miejsc * 100
Jeżeli Pojazd jest instancją Autobusu, opłata ma zostać powiększona o 10% wartości opłaty początkowej.
Np. jeżeli autobus domyślnie ma 50 miejsc to opłata całkowita wyniesie 5500
'''


class Pojazd:
    def __init__(self, predkosc_max, przebieg, nazwa_modelu):
        self.predkosc_max = predkosc_max
        self.przebieg = przebieg
        self.nazwa_modelu = nazwa_modelu

    def liczba_miejsc(self, miejsca):
        return f"{self.nazwa_modelu} pomieści {miejsca} osób."

    def oplata(self, miejsca):
        return miejsca * 100


class Autobus(Pojazd):
    def liczba_miejsc(self, miejsca=50):
        return super().liczba_miejsc(miejsca)

    def oplata(self, miejsca):
        return super().oplata(miejsca) * 1.1


def main():
    autobus1 = Autobus(300, 20, "Autobus XYZ")
    pojazd1 = Pojazd(300, 20, "Pojazd XYZ")
    print(autobus1.liczba_miejsc())
    print(autobus1.liczba_miejsc(20))
    print(pojazd1.liczba_miejsc(20))
    print(f"Opłata za pojazd wynosi {pojazd1.oplata(20)}")
    print(f"Opłata za autobus wynosi {autobus1.oplata(20)}")


if __name__ == "__main__":
    main()
