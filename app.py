# -*- coding: utf-8 -*-
import dash
import json_collect
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = json_collect.monthly_data_df

available_indicators = df['Indicador'].unique()

app.layout = html.Div([
    html.Div([
        dcc.Dropdown(
            id='yaxis-column',
            options=[{'label': i, 'value': i}
                     for i in available_indicators],
            value='Life expectancy at birth, total (years)'
        )
    ], style={'width': '48%', 'float': 'right', 'display': 'inline-block'}),

    dcc.Graph(id='indicator-graphic')
])


@app.callback(
    dash.dependencies.Output('indicator-graphic', 'figure'),
    [dash.dependencies.Input('yaxis-column', 'value')])
def update_graph(yaxis_column_name):
    dff = df

    return {
        'data': [go.Scatter(
            x=dff[dff['Indicador'] == xaxis_column_name]['Media'],
            y=dff[dff['Indicador'] == yaxis_column_name]['Media'],
            text=dff[dff['Indicador'] ==
                     yaxis_column_name]['Indicador'],
            mode='markers',
            marker={
                'size': 15,
                'opacity': 0.5,
                'line': {'width': 0.5, 'color': 'white'}
            }
        )],
        'layout': go.Layout(
            xaxis={
                'title': xaxis_column_name,
                'type': 'linear' if xaxis_type == 'Linear' else 'log'
            },
            yaxis={
                'title': yaxis_column_name,
                'type': 'linear' if yaxis_type == 'Linear' else 'log'
            },
            margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
            hovermode='closest'
        )
    }


if __name__ == '__main__':
    app.run_server(debug=True)
