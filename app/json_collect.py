import urllib.request, json
import pandas as pd
from pandas.io.json import json_normalize

# coleta dados api
with urllib.request.urlopen("https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/ExpectativasMercadoInflacao12Meses?$top=100&$orderby=Data%20desc&$format=json&$select=Indicador,Data,Suavizada,baseCalculo,Media,Mediana,Minimo,Maximo,numeroRespondentes") as url:
    twelve_months_data = json.loads(url.read().decode())
    
with urllib.request.urlopen("https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/ExpectativaMercadoMensais?$top=1000&$orderby=Data%20desc&$format=json&$select=Indicador,Data,DataReferencia,baseCalculo,Media,Mediana,Minimo,Maximo,numeroRespondentes") as url:
    monthly_data = json.loads(url.read().decode())

with urllib.request.urlopen("https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/ExpectativasMercadoTrimestrais?$top=100&$orderby=Data%20desc&$format=json&$select=Indicador,Data,DataReferencia,Media,Mediana,Minimo,Maximo,numeroRespondentes") as url:
    quarterly_data = json.loads(url.read().decode())

with urllib.request.urlopen("https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/ExpectativasMercadoAnuais?$top=1000&$orderby=Data%20desc&$format=json&$select=Indicador,IndicadorDetalhe,Data,DataReferencia,baseCalculo,Media,Mediana,Minimo,Maximo,numeroRespondentes") as url:
    annual_data = json.loads(url.read().decode())

with urllib.request.urlopen("https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/ExpectativasMercadoTop5Anuais?$top=1000&$orderby=Data%20desc&$format=json&$select=Indicador,Data,tipoCalculo,DataReferencia,Media,Mediana") as url:
    top_5_anual_data = json.loads(url.read().decode())

with urllib.request.urlopen("https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/ExpectativasMercadoTop5Mensais?$top=1000&$orderby=Data%20desc&$format=json&$select=Indicador,Data,tipoCalculo,DataReferencia,Media,Mediana") as url:
    top_5_monthly_data = json.loads(url.read().decode())

indicadoresInflacao = {'IGP-DI','IGP-M','INPC','IPA-DI','IPA-M','IPCA','IPC-Fipe','IPCA-15','Preços administrados por contrato e monitorados'}

# transforma json para df
twelve_months_data_df = pd.DataFrame.from_dict(
    twelve_months_data['value'], orient='columns') # nao possui DataReferencia

monthly_data_df = pd.DataFrame.from_dict(
    monthly_data['value'], orient='columns')

quarterly_data_df = pd.DataFrame.from_dict(
    quarterly_data['value'], orient='columns')

annual_data_df = pd.DataFrame.from_dict(
    annual_data['value'], orient='columns')

top_5_anual_df = pd.DataFrame.from_dict(
    top_5_anual_data['value'], orient='columns')

top_5_monthly_df = pd.DataFrame.from_dict(
    top_5_monthly_data['value'], orient='columns')

df_list = {"Mensal":monthly_data_df, "Quaternal":quarterly_data_df, "Doze meses":twelve_months_data_df, "Anual":annual_data_df, "Top 5 anual":top_5_anual_df}

top_5_anual_df['Fonte'] = 'Anual'
top_5_monthly_df['Fonte'] = 'Mensal'

top_5_data = pd.concat([top_5_anual_df, top_5_monthly_df])

top_5_data.loc[top_5_data[top_5_data['Fonte'] == 'Mensal']['Indicador'].isin(indicadoresInflacao),'Media'] = ((((top_5_data[top_5_data['Fonte'] == 'Mensal']['Media']/100)+1)**12)-1)*100

top_5_data = top_5_data.reset_index(drop=True)
indicador = 'IPCA'

# print('Inflação:')
# print('Doze meses:')
# print(twelve_months_data_df[twelve_months_data_df['Indicador']
#                             == indicador][twelve_months_data_df['Data'] == '2019-04-26'][twelve_months_data_df['Suavizada'] == 'S'][twelve_months_data_df['baseCalculo'] == 0])
# print('Expectativa:')
# print('Mesal:')
# print(monthly_data_df[monthly_data_df['Indicador']
#                             == indicador][monthly_data_df['Data'] == '2019-04-26'][monthly_data_df['baseCalculo'] == 0].sort_values(by=['DataReferencia']))
# print('Quaternal:')
# print(quarterly_data_df[quarterly_data_df['Indicador']
#                             == indicador][quarterly_data_df['Data'] == '2019-04-26'].sort_values(by=['DataReferencia']))
# print('Anual:')
# print(annual_data_df[annual_data_df['Indicador']
#                             == indicador][annual_data_df['Data'] == '2019-04-26'][annual_data_df['baseCalculo'] == 0].sort_values(by=['DataReferencia']))

print('Top 5:')
print('Anual:')
print(top_5_anual_df[top_5_anual_df['Indicador']
                            == indicador][top_5_anual_df['Data'] == '2019-04-26'][top_5_monthly_df['tipoCalculo'] == 'C'].sort_values(by=['tipoCalculo','DataReferencia']))
print('Mensal:')
print(top_5_monthly_df[top_5_monthly_df['Indicador'] 
                            == indicador][top_5_monthly_df['Data'] == '2019-04-26'][top_5_monthly_df['tipoCalculo'] == 'C'].sort_values(by=['DataReferencia']))

print("teste")
print(top_5_data[top_5_data['Indicador'] 
            == indicador][top_5_data['Data'] == '2019-04-26'][top_5_data['tipoCalculo'] == 'C'].sort_values(by=['DataReferencia']))

# monthly_data_df['DataReferencia'] = pd.to_datetime(
#     monthly_data_df['DataReferencia'], format='%m/%Y')
# quarterly_data_df['DataReferencia'] = pd.to_datetime(
#     quarterly_data_df['DataReferencia'], format='%m/%Y')
# twelve_months_data_df['DataReferencia'] = pd.to_datetime(
#     twelve_months_data_df['DataReferencia'], format='%m/%Y')
# annual_data_df['DataReferencia'] = pd.to_datetime(
#     annual_data_df['DataReferencia'], format='%m/%Y')
