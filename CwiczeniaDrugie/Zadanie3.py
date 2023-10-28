'''
Zadanie 3 (1 pkt)
W kodzie z zajęć w klasie Pojazd utwórz atrybut, który niezależnie od utworzonego obiektu będzie miał taką samą wartość.
każdy obiekt ma mieć kolor biały
'''


class Pojazd:
    kolor = "biały"

    def __init__(self, predkosc_max, przebieg):
        self.predkosc_max = predkosc_max
        self.przebieg = przebieg


def main():
    pojazd1 = Pojazd(240, 50)
    pojazd2 = Pojazd(180, 17)
    print(pojazd1.predkosc_max)
    print(pojazd1.przebieg)
    print(pojazd1.kolor)
    print(pojazd2.kolor)

if __name__ == "__main__":
    main()
