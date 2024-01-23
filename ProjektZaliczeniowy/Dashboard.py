import numpy as np
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, dash
from dash.dependencies import Input, Output
from sklearn.compose import ColumnTransformer
from sklearn.feature_selection import RFE
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import statsmodels.api as sm


# 2. wizualizacja rozkładu zmiennej price
def visaulization_distribution_variable_price(data):
    fig = px.histogram(data, x="price", nbins=50, title='Rozkład zmiennej price')
    fig.update_xaxes(title_text='price')
    fig.update_yaxes(title_text='count')
    return fig


def backward_elimination(X, y, significance_level=0.05):
    features = X.columns
    while len(features) > 0:
        X_const = sm.add_constant(X[features])
        print(np.asarray(X))
        print(np.asarray(y))
        model = sm.OLS(y, X_const).fit()
        max_p_value = max(model.pvalues)
        if max_p_value > significance_level:
            excluded_feature = model.pvalues.idxmax()
            features = features.drop(excluded_feature)
        else:
            break
    return X[features]


# 3 i 4. budowa modelu regresji ceny od pozostałych zmiennych. Istotne zmienne należy wybrać eliminacją wsteczną lub selekcją postępującą.
def regression_model(df):
    X = df.drop('price', axis=1)
    y = df['price']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Definiowanie modelu
    numeric_features = ['carat', 'x dimension', 'y dimension', 'z dimension', 'depth', 'table']
    categorical_features = ['clarity', 'color', 'cut']

    numeric_transformer = Pipeline(steps=[
        ('scaler', StandardScaler())
    ])

    categorical_transformer = Pipeline(steps=[
        # Zastosowanie kodowania OneHotEncoder do zmiennych kategorycznych w celu przekształcenia ich do postaci numerycznej
        ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])

    preprocessor = ColumnTransformer(  # Zastosowanie transformacji kolumn do danych numerycznych i kategorycznych
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)
        ])

    model = Pipeline(steps=[  # Zastosowanie modelu regresji liniowej
        ('preprocessor', preprocessor),
        ('regressor', LinearRegression())
    ])

    # Dopasowanie modelu
    model.fit(X_train, y_train)  # Dopasowanie modelu do danych treningowych

    # Ocena modelu
    y_pred = model.predict(X_test)  # Przewidywanie wartości dla danych testowych
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)  # Współczynnik determinacji
    print(f'MSE: {mse}')  # Błąd średniokwadratowy (MSE) - średnia kwadratów błędów predykcji modelu regresji
    print(f'R^2: {r2}')  # Współczynnik determinacji (R^2) - miara dopasowania modelu regresji do danych
    # wizualizacja wyników
    scatter_fig = {
        'data': [
            {'x': y_test, 'y': y_pred, 'type': 'scatter', 'mode': 'markers'}
        ],
        'layout': {'title': f'Model Regresji - Przewidywane vs. Rzeczywiste',
        'xaxis': {'title': 'Rzeczywiste'},
        'yaxis': {'title': 'Przewidywane'}
                   }
    }

    return scatter_fig


def regression_model_with_backward_elimination(df):
    df['price'] = df['price'].astype('float64')
    df_float_only = df.select_dtypes(include='float64')
    X = df_float_only.drop('price', axis=1)
    y = df_float_only['price']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Zakodowanie zmiennych kategorialnych
    X_train_encoded = pd.get_dummies(X_train)

    # Eliminacja wsteczna
    X_train_backward = backward_elimination(X_train_encoded, y_train)

    # Dopasowanie modelu
    model_backward = sm.OLS(y_train, X_train_backward).fit()

    # Zakodowanie i eliminacja zmiennych na zbiorze testowym
    X_test_encoded = pd.get_dummies(X_test)
    X_test_backward = X_test_encoded[X_train_backward.columns]

    # Predykcja na zbiorze testowym
    y_pred = model_backward.predict(X_test_backward)

    # Porównanie wyników
    mse = mean_squared_error(y_test, y_pred)

    scatter_fig = {
        'data': [
            {'x': y_test, 'y': y_pred, 'type': 'scatter', 'mode': 'markers'}
        ],
        'layout': {'title': f'Model Regresji z eliminacją wsteczną - Porównanie Rzeczwiste vs. Przewidywane',
        'xaxis': {'title': 'Rzeczywiste'},
        'yaxis': {'title': 'Przewidywane'}
                   }
    }

    return scatter_fig


# 5. stworzenie dashboardu z wykresami i tabelami
def application_layout(data, app):
    # Dodanie komponentu Store
    app.layout = html.Div([
        dcc.Store(id='data-store', storage_type='memory', data=data.to_dict('records')),
        html.H1("Analiza Danych - Projekt Zaliczeniowy"),

        # Dropdown do wyboru zmiennej do analizy
        html.Label("Wybierz zmienną do analizy:"),
        dcc.Dropdown(
            id='variable-dropdown',
            options=[{'label': col, 'value': col} for col in data.columns],
            value='carat'  # Domyślna wartość
        ),

        html.H2("Dashboard Analizy Danych"),

        # Wykres punktowy: Zależność ceny od innej wybranej przez użytkownika zmiennej
        dcc.Graph(id='scatter-plot'),

        html.H2("Model Regresji - Rzeczywiste vs. Przewidywane"),

        dcc.Graph(id='scatter-fig'),

        html.H2("Model Regresji z eliminacją wsteczną - Porównanie Rzeczwiste vs. Przewidywane"),

        dcc.Graph(id='scatter-fig-backward'),

        html.H2("Rozkład zmiennej price"),
        # Histogram: Rozkład zmiennej price
        html.Div([
            dcc.Graph(id='histogram-plot', figure=visaulization_distribution_variable_price(data))
        ]),

        # Tabela z próbką danych
        html.Div([
            html.H3("Tabela próbki danych"),
            html.Table(id='sample-table')
        ]),

    ])

    # Funkcja tworząca wykres punktowy
    def create_scatter_plot(selected_variable, data):
        scatter_figure = {
            'data': [
                {'x': data[selected_variable], 'y': data['price'], 'type': 'scatter', 'mode': 'markers'}
            ],
            'layout': {'title': f'Zależność ceny od {selected_variable}'}
        }
        return scatter_figure

    #
    @app.callback(
        Output('scatter-fig', 'figure'),
        [Input('data-store', 'data')]
    )
    def predict_vs_real(data):
        return regression_model(pd.DataFrame(data))

    @app.callback(
        Output('scatter-fig-backward', 'figure'),
        [Input('data-store', 'data')]
    )
    def predict_vs_real_with_backward_elimination(data):
        return regression_model_with_backward_elimination(pd.DataFrame(data))

    # Funkcja aktualizująca wykres punktowy
    @app.callback(
        Output('scatter-plot', 'figure'),
        [Input('variable-dropdown', 'value'),
         Input('data-store', 'data')]
    )
    def update_scatter_plot(selected_variable, data):
        return create_scatter_plot(selected_variable, pd.DataFrame(data))

    # # Funkcja aktualizująca tabelę
    @app.callback(
        Output('sample-table', 'children'),
        [Input('data-store', 'data')]
    )
    def update_sample_table(data):
        return [html.Tr([html.Th(col) for col in data[0].keys()])] + \
            [html.Tr([html.Td(row[col]) for col in data[0].keys()]) for row in data[:20]]

    app.run_server(debug=True)


def dashboard_creation(data, app):
    visaulization_distribution_variable_price(data)
    regression_model(data)
    application_layout(data, app)
    regression_model_with_backward_elimination(data)
