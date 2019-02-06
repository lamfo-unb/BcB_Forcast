# -*- coding: utf-8 -*-
import dash
import json_collect
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

avaiable_df = []

for key in json_collect.df_list:
    avaiable_df.append(key)

app.layout = html.Div([
    dcc.RadioItems(
        id='df-type',
        options=[{'label': i, 'value': i} for i in avaiable_df],
        labelStyle={'display': 'inline-block'}
    ),

    html.Div([
        dcc.Dropdown(
            id='xaxis-column',
            options=[]

    )], style={'width': '48%', 'display': 'inline-block'}),
    
    html.Div([
        dcc.Dropdown(
            id='yaxis-column',
            options=[]
    )], style={'width': '48%', 'display': 'inline-block'}),
    

    dcc.Graph(id='indicator-graphic')
])


@app.callback(
    dash.dependencies.Output('xaxis-column', 'options'),
    [dash.dependencies.Input('df-type', 'value')])
def callback_a(dropdown_value):
    return [{'label': i, 'value': i} for i in json_collect.df_list[dropdown_value]["Indicador"].unique()]

@app.callback(
    dash.dependencies.Output('yaxis-column', 'options'),
    [dash.dependencies.Input('df-type', 'value')])
def callback_b(dropdown_value):
    return [{'label': i, 'value': i} for i in json_collect.df_list[dropdown_value]["DataReferencia"].unique()]

@app.callback(
    dash.dependencies.Output('indicator-graphic', 'figure'),
    [dash.dependencies.Input('xaxis-column', 'value'),
     dash.dependencies.Input('yaxis-column', 'value'),
     dash.dependencies.Input('df-type', 'value')])
def update_graph(xaxis_column_name, yaxis_column_name, df_name):
    dff = json_collect.df_list[df_name]
    dff = dff[dff["Indicador"] == xaxis_column_name]

    return {
        'data': [go.Scatter(
            x=dff[dff['DataReferencia'] == yaxis_column_name]['Data'],
            y=dff[dff['DataReferencia'] == yaxis_column_name]['Media'],
            text=dff['Indicador'],
            name='Média',
            marker={
                'size': 15,
                'opacity': 0.5,
                'line': {'width': 3, 'color': 'white'}
            }
        )]
    }

if __name__ == '__main__':
    app.run_server(debug=True)
