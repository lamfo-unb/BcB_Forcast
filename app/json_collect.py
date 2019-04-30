import urllib.request, json 
import pandas as pd
from pandas.io.json import json_normalize

# coleta dados api
with urllib.request.urlopen("https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/ExpectativaMercadoMensais?$top=1000&$orderby=Data%20desc&$format=json&$select=Indicador,Data,DataReferencia,Media,Mediana,Minimo,Maximo,numeroRespondentes") as url:
    monthly_data = json.loads(url.read().decode())

with urllib.request.urlopen("https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/ExpectativasMercadoTrimestrais?$top=100&$orderby=Data%20desc&$format=json&$select=Indicador,Data,DataReferencia,Media,Mediana,Minimo,Maximo,numeroRespondentes") as url:
    quarterly_data = json.loads(url.read().decode())

with urllib.request.urlopen("https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/ExpectativasMercadoInflacao12Meses?$top=100&$orderby=Data%20desc&$format=json&$select=Indicador,Data,Suavizada,Media,Mediana,Minimo,Maximo,numeroRespondentes") as url:
    twelve_months_data = json.loads(url.read().decode())

with urllib.request.urlopen("https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/ExpectativasMercadoAnuais?$top=1000&$orderby=Data%20desc&$format=json&$select=Indicador,IndicadorDetalhe,Data,DataReferencia,Media,Mediana,Minimo,Maximo,numeroRespondentes") as url:
    annual_data = json.loads(url.read().decode())
    
with urllib.request.urlopen("https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/ExpectativasMercadoTop5Anuais?$top=1000&$orderby=Data%20desc&$format=json&$select=Indicador,IndicadorDetalhe,Data,DataReferencia,tipoCalculo,Media,Mediana,Minimo,Maximo") as url:
    top_5_anual_data = json.loads(url.read().decode())

with urllib.request.urlopen("https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/ExpectativasMercadoTop5Mensais?$top=1000&$orderby=Data%20desc&$format=json&$select=Indicador,Data,DataReferencia,tipoCalculo,Media,Mediana,DesvioPadrao,CoeficienteVariacao,Minimo,Maximo") as url:
    top_5_monthly_data = json.loads(url.read().decode())


# transforma json para df
monthly_data_df = pd.DataFrame.from_dict(
    monthly_data['value'], orient='columns')

quarterly_data_df = pd.DataFrame.from_dict(
    quarterly_data['value'], orient='columns')

twelve_months_data_df = pd.DataFrame.from_dict(
    twelve_months_data['value'], orient='columns') # nao possui DataReferencia

annual_data_df = pd.DataFrame.from_dict(
    annual_data['value'], orient='columns')

top_5_anual_df = pd.DataFrame.from_dict(
    top_5_anual_data['value'], orient='columns')

top_5_monthly_df = pd.DataFrame.from_dict(
    top_5_monthly_data['value'], orient='columns')

df_list = {"Mensal":monthly_data_df, "Quaternal":quarterly_data_df, "Doze meses":twelve_months_data_df, "Anual":annual_data_df, "Top 5 anual":top_5_anual_df}

# print('Doze meses:')
# print(twelve_months_data_df[twelve_months_data_df['Indicador']
#                             == 'IPCA'][twelve_months_data_df['Data'] == '2019-04-26'])
# print('Mesal:')
# print(monthly_data_df[monthly_data_df['Indicador']
#                             == 'IPCA'][monthly_data_df['Data'] == '2019-04-26'])
# print('Quaternal:')
# print(quarterly_data_df[quarterly_data_df['Indicador']
#                             == 'IPCA'][quarterly_data_df['Data'] == '2019-04-26'])
# print('Anual:')
# print(annual_data_df[annual_data_df['Indicador']
#                             == 'IPCA'][annual_data_df['Data'] == '2019-04-26'])
# print('Top 5 Anual:')
# print(top_5_anual_df[top_5_anual_df['Indicador']
#                             == 'IPCA'][top_5_anual_df['Data'] == '2019-04-26'])
print('Top 5 Mensal:')
print(top_5_monthly_df[top_5_monthly_df['Indicador']
                            == 'IPCA'][top_5_monthly_df['Data'] == '2019-04-26'])

# print('Quaternal:')
# print(quarterly_data_df[quarterly_data_df['Indicador'] == 'IGP-DI'])
# print('Top 5 Anual:')
# print(top_5_anual_df[top_5_anual_df['Indicador'] == 'IGP-DI'])


# monthly_data_df['DataReferencia'] = pd.to_datetime(
#     monthly_data_df['DataReferencia'], format='%m/%Y')
# quarterly_data_df['DataReferencia'] = pd.to_datetime(
#     quarterly_data_df['DataReferencia'], format='%m/%Y')
# twelve_months_data_df['DataReferencia'] = pd.to_datetime(
#     twelve_months_data_df['DataReferencia'], format='%m/%Y')
# annual_data_df['DataReferencia'] = pd.to_datetime(
#     annual_data_df['DataReferencia'], format='%m/%Y')
