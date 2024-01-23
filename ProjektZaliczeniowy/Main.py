import numpy as np
import pandas as pd
from dash import dash

from ProjektZaliczeniowy import Dashboard


def set_settings():
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.width', None)


def get_data_from_file(file_name):
    data_ = pd.read_csv(file_name)
    return data_


def get_data_in_numpy_array(pd_array):
    data_1 = np.array(pd_array)
    return data_1


def outlier_data(out_data):
    # Zastosowanie zasady IQR do identyfikacji danych odstających
    Q1 = out_data['price'].quantile(0.25) #Pierwszy kwartyl
    Q3 = out_data['price'].quantile(0.75) #Trzeci kwartyl
    IQR = Q3 - Q1  # Rozstęp ćwiartkowy różnica między trzecim a pierwszym kwartylem

    lower_bound = Q1 - 1.5 * IQR # Dolna granica
    upper_bound = Q3 + 1.5 * IQR # Górna granica

    out_data = out_data[(out_data['price'] >= lower_bound) & (out_data['price'] <= upper_bound)]

    # print("Dane odstające:")
    return out_data


def data_clean(data):
    # Usunięcie spacji przed nazwami kolumn
    data.columns = [col.strip() for col in data.columns]
    # print(data.info())
    # print(data['price'].describe())

    # Zmiana błędnych/pustych wartości na NaN
    data = data.replace({"": np.nan, " ": np.nan})
    # print(data.isna().any())
    # print(data.isna().sum())

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
    data['price'] = data['price'].astype('float64')
    data['carat'] = data['carat'].astype('float64')
    data['x dimension'] = data['x dimension'].astype('float64')
    data['y dimension'] = data['y dimension'].astype('float64')
    data['z dimension'] = data['z dimension'].astype('float64')
    data['depth'] = data['depth'].astype('float64')
    data['table'] = data['table'].astype('int64')
    data['clarity'] = data['clarity'].astype('string')
    data['color'] = data['color'].astype('string')
    data['cut'] = data['cut'].astype('string')

    # Usunięcie wartości odstających
    data = outlier_data(data)
    # print(data)

    # Suma zduplikowanych wartości
    # print(data.duplicated().sum())

    # Wartości w tych kolumnach posiadają poprawną wartość ze zbioru co wskazuje na to że są najbardziej prawdopodobnie rzeczywiste
    # Usunięcie duplikatów
    data = data.drop_duplicates(subset=["clarity", "color", "cut", 'x dimension'], keep='first')
    # print(data)
    return data


if __name__ == '__main__':
    app = dash.Dash(__name__)
    set_settings()
    data_from_file = get_data_from_file('Dane/messy_data.csv')
    cleaned_data = data_clean(data_from_file)
    Dashboard.dashboard_creation(cleaned_data, app)
