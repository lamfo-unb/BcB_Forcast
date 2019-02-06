# -*- coding: utf-8 -*-
import dash
import json_collect
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = json_collect.monthly_data_df

available_indicators = df['Indicador'].unique()

# df = df[df["Indicador"] == "IGP-DI"]

app.layout = html.Div([
    html.Div([
        dcc.Dropdown(
            id='xaxis-column',
            options=[{'label': i, 'value': i}
                     for i in available_indicators],
            value='IGP-ID'
        )
    ], style={'width': '48%', 'display': 'inline-block'}),

    dcc.Graph(id='indicator-graphic')
    # dcc.Graph(id='example-graph',
    #         figure={
    #             'data': [go.Scatter(x=df['DataReferencia'], y=df['Media'], mode='markers',
    #                                 marker={
    #                                     'size': 15,
    #                                     'opacity': 0.5,
    #                                     'line': {'width': 0.5, 'color': 'white'}
    #                                 })],
    #             'layout': {'title': 'Regression Data Example in Plotly'}})
])


@app.callback(
    dash.dependencies.Output('indicator-graphic', 'figure'),
    [dash.dependencies.Input('xaxis-column', 'value')])
def update_graph(xaxis_column_name):
    dff = json_collect.monthly_data_df[json_collect.monthly_data_df["Indicador"]
                                       == xaxis_column_name]

    return {
        'data': [go.Scatter(
            x=dff['DataReferencia'],
            y=dff['Maximo'],
            text=dff['Indicador'],
            mode='lines',
            marker={
                'size': 15,
                'opacity': 0.5,
                'line': {'width': 0.5, 'color': 'white'}
            }
        ),
            go.Scatter(
            x=dff['DataReferencia'],
            y=dff['Minimo'],
            text=dff['Indicador'],
            mode='lines',
            marker={
                'size': 15,
                'opacity': 0.5,
                'line': {'width': 0.5, 'color': 'white'}
            }
        )]
    }


# app.layout = html.Div(children=[
#     html.H1(children='Hello Dash'),

#     html.Div(children='''
#         Dash: A web application framework for Python.
#     '''),

#     dcc.Graph(id='example-graph',
#         figure={
#             'data': [go.Scatter(x=df['DataReferencia'], y=df['Media'], mode='markers',
#                                 marker={
#                                     'size': 15,
#                                     'opacity': 0.5,
#                                     'line': {'width': 0.5, 'color': 'white'}
#                                 })],
#             'layout': {'title': 'Regression Data Example in Plotly'}})
# ])
if __name__ == '__main__':
    app.run_server(debug=True)
