# Napisz funkcję o nazwie check_range, która sprawdza, czy liczba znajduje się w podanym zakresie (zawiera zarówno niski i wysoki).
# Jeśli tak, zwróć „x jest między y a z”.
# Jeśli tak nie jest, zwróć „x NIE jest między y a z”.
# Gdzie:
#
# x to liczba
# y jest dolną granicą
# z to górna granica

def check_range(x, y, z):
    if y < x < z:
        return "x jest między y a z"
    else:
        return "x NIE jest między y a z"


def bool_range(x, y, z):
    return y < x < z
