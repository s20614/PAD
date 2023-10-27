from CwiczeniaDrugie.Tetranacci import Tetranacci

if __name__ == '__main__':
    print('Tetranacci')
    try:
        steps = int(input("Podaj liczbę kroków w ciągu Tetranacciego: "))
        if steps < 0:
            print("Liczba kroków nie może być mniejsza od zera!")
        else:
            tetranacci_iter = Tetranacci(steps)
            for value in tetranacci_iter:
                print(value, end=' ')
    except ValueError:
        print("To nie jest poprawna liczba.")