import numpy as np
import pandas as pd


def set_settings():
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.width', None)


def get_data_from_file(file_name):
    data_ = pd.read_csv(file_name)
    return data_


def get_data_in_numpy_array(pd_array):
    data1 = np.array(pd_array)
    return data1


def data_clean(data):
    # typy danych dla poszczególnych kolumn
    # print(data.dtypes)

    # typy danych dla poszczególnych kolumn i liczba wartości null
    # print(data.info())

    # Usunięcie spacji przed nazwami kolumn
    data.columns = [col.strip() for col in data.columns]
    # print(data.info())
    # print(data['price'].describe())

    # Zmiana błędnych/pustych wartości na NaN
    data = data.replace({"": np.nan, " ": np.nan})
    print(data.isna().any())
    print(data.isna().sum())

    # Zmiana na duże litery dla zgodności
    data['cut'] = data['cut'].str.upper()
    data['color'] = data['color'].str.upper()
    data['clarity'] = data['clarity'].str.upper()

    # Usunięcie wierszy dla wartości NaN w kolumnie price
    data = data.dropna(subset=['price'])

    # Wstawienie mediany dla pól carat, x dimension, y dimension, z dimension, depth, table
    data['carat'].fillna(data['carat'].median(), inplace=True)
    data['x dimension'].fillna(data['x dimension'].median(), inplace=True)
    data['y dimension'].fillna(data['y dimension'].median(), inplace=True)
    data['z dimension'].fillna(data['z dimension'].median(), inplace=True)
    data['depth'].fillna(data['depth'].median(), inplace=True)
    data['table'].fillna(data['table'].median(), inplace=True)

    # Konwersja danych na poprawny typ
    data['price'] = data['price'].astype('int64')
    data['carat'] = data['carat'].astype('float64')
    data['x dimension'] = data['x dimension'].astype('float64')
    data['y dimension'] = data['y dimension'].astype('float64')
    data['z dimension'] = data['z dimension'].astype('float64')
    data['depth'] = data['depth'].astype('float64')
    data['table'] = data['table'].astype('int64')

    # Suma zduplikowanych wartości
    # print(data.duplicated().sum())

    # Wartości w tych kolumnach posiadają poprawną wartość ze zbioru co wskazuje na to że są najbardziej prawdopodobnie rzeczywiste
    duplicates = data.duplicated(subset=["clarity", "color", "cut", 'x dimension'], keep=False)
    print(data[duplicates])

    print(data)


if __name__ == '__main__':
    set_settings()
    data = get_data_from_file('Dane/messy_data.csv')
    data_clean(data)
