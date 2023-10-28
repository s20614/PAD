'''
Zadanie 2 (4 pkt)
Zaimplementuj własny generator o nazwie repeat, zwracający obiekt podany przez użytkownika dokładnie N razy.
Jeśli wartość parametru N nie została określona, generator powinien zwracać wartości w nieskończoność.

PRZYKŁAD
repeat(10, 3) → 10 10 10
repeat(10, 5) → 10 10 10 10 10
repeat(5) → 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5…
repeat(5, None) → 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5…
'''


def repeat(gen_obj, count=-1):
    if count == -1:
        while True:
            yield gen_obj
    else:
        for i in range(count):
            yield gen_obj


def main():
    for i in repeat(10,5):
        print(i, end=" ")


if __name__ == "__main__":
    main()
