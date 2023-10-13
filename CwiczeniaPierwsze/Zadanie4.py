# Zdefiniuj funkcję rekurencyjną o nazwie num_fact, która zwraca silnię podanej liczby.
def num_fact(num):
    if num > 0:
        return num * num_fact(num - 1)
    else:
        return 1
