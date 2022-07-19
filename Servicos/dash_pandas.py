# pip install pandas dash sqlalchemy psycopg2
# dash.ploty.com -> página dash

# Run this app with `python dash_pandas.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from socket import NI_NUMERICHOST
from dash import Dash, html, dcc, Output, Input
from matplotlib.pyplot import figure
import dash_bootstrap_components as dbc
from datetime import date
import plotly.express as px
import pandas as pds

import psycopg2
from sqlalchemy import create_engine


valor = 3

# Create an engine instance
alchemyEngine = create_engine(
    'postgresql+psycopg2://postgres:241500@127.0.0.1/utilidades', pool_recycle=3600)

# Connect to PostgreSQL server
dbConnection = alchemyEngine.connect()

# Read data from PostgreSQL database table and load into a DataFrame instance
dataFrame = pds.read_sql("select * from \"ar_comprimido\"", dbConnection)

#pds.set_option('display.expand_frame_repr', False)

# Print the DataFrame
# print(dataFrame)

# Close the database connection
dbConnection.close()


app = Dash(__name__)


# cria gráfico
fig = px.line(dataFrame, x="data", y="valor")


# Layout Html
app.layout = dbc.Container([

    # html page
    dbc.Row([
        dbc.Col([
            html.H2(children='Utilidade Ar Comprimido V_1.0'),
        ], width=12)
    ]),

    # html page
    dbc.Row([
        dbc.Col([
            html.H5(children='''
        Dash: A web application framework for your data.
    '''),
        ], width=12)
    ]),


    dbc.Row([
        dbc.Col([
            html.H5(id="dd-output-container"),
        ], width=12)
    ]),


    dbc.Row([
        dbc.Col([
            dcc.Dropdown(['ANO', 'MES', 'TODOS'], 'ANO', id='demo-dropdown',
                         style={'width': "30%"},
                         ),
        ], width=1),

        dbc.Col([
            dbc.Input(id="entrada", value=2030,
                      type="number",
                      style={'width': "10%"},
                      ),
        ], width=4),

    ]),

    # Dash graph
    dcc.Graph(
        id='example-graph',
        figure=fig
    ),

    # Dash intervalo de atualização da aplicação
    dcc.Interval(
        id='graph-update',
        interval=10000,
        n_intervals=0
    )

])


@ app.callback(
    Output('example-graph', 'figure'),
    Input('graph-update', 'n_intervals'),
    Input('demo-dropdown', 'value'),
    Input('entrada', 'value')
)
def update_graph_scatter(n, seltipo, seldata):
   # Connect to PostgreSQL server
    dbConnection = alchemyEngine.connect()

    # Read data from PostgreSQL database table and load into a DataFrame instance
    #dataFrame = pds.read_sql(f"SELECT * FROM ar_comprimido WHERE valor='{valor}'", dbConnection)
    # dataFrame = pds.read_sql(
    #    f"SELECT * FROM ar_comprimido WHERE EXTRACT(YEAR FROM data) = 2030", dbConnection)

    if seltipo == "ANO":
        dataFrame = pds.read_sql(
            f"SELECT * ,concat(data,hora) as datatime FROM ar_comprimido WHERE EXTRACT(YEAR FROM data) = \
                {seldata} ORDER by datatime", dbConnection)
    elif seltipo == "MES":
        if seldata == "":
            seldata = 1
        selano = date.today()
        dataFrame = pds.read_sql(
            f"SELECT * ,concat(data,hora) as datatime FROM ar_comprimido WHERE EXTRACT(YEAR FROM data) = \
                 2022 AND EXTRACT(MONTH FROM data) = {seldata} ORDER by datatime", dbConnection)
    elif seltipo == "TODOS":
        dataFrame = pds.read_sql(
            f"SELECT *  ,concat(data,hora) as datatime FROM ar_comprimido ORDER by datatime ", dbConnection)

    # Print the DataFrame
    print(dataFrame)
    print(valor)
    print(seldata)

    # Close the database connection
    dbConnection.close()

    # cria gráfico
    fig = px.line(dataFrame, x="datatime", y="valor")

    return fig


@ app.callback(
    Output('dd-output-container', 'children'),
    Input('demo-dropdown', 'value'),
    Input('entrada', 'value')



)
def update_output(valor1, valor2):
    return f'You have selected {valor1} = {valor2}',


if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port='8050')
