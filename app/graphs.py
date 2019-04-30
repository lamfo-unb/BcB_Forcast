import json_collect
import plotly.graph_objs as go
from datetime import datetime
import json
import plotly

# avaiable_df = []

# for key in json_collect.df_list:
#     avaiable_df.append(key)


def create_plot(yaxis_column_name, xaxis_column_name):
    dff = json_collect.df_list['Mensal']
    dff = dff[dff["Indicador"] == xaxis_column_name]

    data = [
        go.Scatter(
            x=sorted(dff[dff['Data'] == yaxis_column_name]['DataReferencia'],
                    key=lambda date: datetime.strptime(date, "%m/%Y")),
            y=dff[dff['Data'] == yaxis_column_name]['Media'],
            text=dff['Indicador'],
            name='Média',
            marker={
                'size': 15,
                'opacity': 0.5,
                'line': {'width': 3, 'color': 'white'}
            }),
        go.Scatter(
            x=sorted(dff[dff['Data'] == yaxis_column_name]['DataReferencia'],
                     key=lambda date: datetime.strptime(date, "%m/%Y")),
            y=dff[dff['Data'] == yaxis_column_name]['Maximo'],
            text=dff['Indicador'],
            name='Média',
            marker={
                'size': 15,
                'opacity': 0.5,
                'line': {'width': 3, 'color': 'white'}
            }),
        go.Scatter(
            x=sorted(dff[dff['Data'] == yaxis_column_name]['DataReferencia'],
                     key=lambda date: datetime.strptime(date, "%m/%Y")),
            y=dff[dff['Data'] == yaxis_column_name]['Minimo'],
            text=dff['Indicador'],
            name='Média',
            marker={
                'size': 15,
                'opacity': 0.5,
                'line': {'width': 3, 'color': 'white'}
            })
            ]
    
    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON
