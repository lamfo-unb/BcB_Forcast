import urllib.request, json
import pandas as pd
from pandas.io.json import json_normalize

# --  AGRUPAMENTO 1
# coleta dados api
with urllib.request.urlopen("https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/ExpectativasMercadoInflacao12Meses?$top=10000&$orderby=Data%20desc&$format=json&$select=Indicador,Data,Suavizada,baseCalculo,Media,Mediana") as url:
    twelve_months_data = json.loads(url.read().decode())
    
with urllib.request.urlopen("https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/ExpectativaMercadoMensais?$top=10000&$orderby=Data%20desc&$format=json&$select=Indicador,Data,DataReferencia,baseCalculo,Media,Mediana") as url:
    monthly_data = json.loads(url.read().decode())

with urllib.request.urlopen("https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/ExpectativasMercadoTrimestrais?$top=10000&$orderby=Data%20desc&$format=json&$select=Indicador,Data,DataReferencia,Media,Mediana") as url:
    quarterly_data = json.loads(url.read().decode())

with urllib.request.urlopen("https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/ExpectativasMercadoAnuais?$top=10000&$orderby=Data%20desc&$format=json&$select=Indicador,IndicadorDetalhe,Data,DataReferencia,baseCalculo,Media,Mediana") as url:
    annual_data = json.loads(url.read().decode())

with urllib.request.urlopen("https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/ExpectativasMercadoTop5Anuais?$top=10000&$orderby=Data%20desc&$format=json&$select=Indicador,Data,tipoCalculo,DataReferencia,Media,Mediana") as url:
    top_5_anual_data = json.loads(url.read().decode())

with urllib.request.urlopen("https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/ExpectativasMercadoTop5Mensais?$top=10000&$orderby=Data%20desc&$format=json&$select=Indicador,Data,tipoCalculo,DataReferencia,Media,Mediana") as url:
    top_5_monthly_data = json.loads(url.read().decode())

indicadores = pd.DataFrame.from_dict(list([{'Conjunto': 'Inflação', 'IndiNome':'IGP-DI'},
                                              {'Conjunto': 'Inflação', 'IndiNome':'IGP-M'},
                                              {'Conjunto': 'Inflação', 'IndiNome':'INPC'},
                                              {'Conjunto': 'Inflação', 'IndiNome':'IPA-DI'},
                                              {'Conjunto': 'Inflação', 'IndiNome':'IPA-M'},
                                              {'Conjunto': 'Inflação', 'IndiNome':'IPCA'},
                                              {'Conjunto': 'Inflação', 'IndiNome':'IPC-Fipe'},
                                              {'Conjunto': 'Inflação', 'IndiNome':'IPCA-15'},
                                              {'Conjunto': 'Inflação', 'IndiNome':'Preços administrados por contrato e monitorados'},
                                              {'Conjunto': 'PIB', 'IndiNome':'PIB Agropecuária'},
                                              {'Conjunto': 'PIB', 'IndiNome':'PIB Industrial'},
                                              {'Conjunto': 'PIB', 'IndiNome':'PIB Serviços'},
                                              {'Conjunto': 'PIB', 'IndiNome':'PIB Total'},
                                              {'Conjunto': 'PIB', 'IndiNome':'Produção industrial'},
                                              {'Conjunto': 'Macro','IndiNome':'Meta para taxa over-selic',},
                                              {'Conjunto': 'Macro','IndiNome':'Taxa de câmbio'},
                                              {'Conjunto': 'Transacionais', 'IndiNome':'Balança Comercial - Saldo'},
                                              {'Conjunto': 'Transacionais', 'IndiNome':'Balança Comercial - Exportações'},
                                              {'Conjunto': 'Transacionais', 'IndiNome':'Balança Comercial - Importações'},
                                              {'Conjunto': 'Transacionais', 'IndiNome':'Balança Comercial - Importações'},
                                              {'Conjunto': 'Fiscais', 'IndiNome':'Balanço de Pagamentos - Conta corrente'},
                                              {'Conjunto': 'Fiscais', 'IndiNome':'Balanço de Pagamentos - Investimento direto no país'},
                                              {'Conjunto': 'Fiscais', 'IndiNome':'Fiscal - Resultado Primário'},
                                              {'Conjunto': 'Fiscais', 'IndiNome':'Fiscal - Resultado Nominal'},
                                              {'Conjunto': 'Fiscais', 'IndiNome':'Fiscal - Dívida líquida do setor público'}]), orient='columns')

# transforma json para df
twelve_months_data_df = pd.DataFrame.from_dict(
    twelve_months_data['value'], orient='columns') # nao possui DataReferencia

twelve_months_data_df = twelve_months_data_df[twelve_months_data_df['Suavizada'] == 'S'][twelve_months_data_df['baseCalculo'] == 0]

monthly_data_df = pd.DataFrame.from_dict(
    monthly_data['value'], orient='columns')

monthly_data_df = monthly_data_df[monthly_data_df['baseCalculo'] == 0]

quarterly_data_df = pd.DataFrame.from_dict(
    quarterly_data['value'], orient='columns')

annual_data_df = pd.DataFrame.from_dict(
    annual_data['value'], orient='columns')

annual_data_df = annual_data_df[annual_data_df['baseCalculo'] == 0]

top_5_anual_df = pd.DataFrame.from_dict(
    top_5_anual_data['value'], orient='columns')

top_5_monthly_df = pd.DataFrame.from_dict(
    top_5_monthly_data['value'], orient='columns')

df_list = {"Mensal":monthly_data_df, "Quaternal":quarterly_data_df, "Doze meses":twelve_months_data_df, "Anual":annual_data_df, "Top 5 anual":top_5_anual_df}



# 12 MESES INFLAÇÃO limpeza e preparo de dados 
twelve_months_data_df = twelve_months_data_df[twelve_months_data_df['Suavizada'] == 'S'][twelve_months_data_df['baseCalculo'] == 0]

twelve_months_data_df['IndiNome'] = twelve_months_data_df['Indicador']

twelve_months_data_df.drop(['Indicador','Suavizada','baseCalculo'], axis=1, inplace=True)


# DATA EXPECTATIVA MERCADO limpeza e preparo de dados 
monthly_data_df['Fonte'] = 'Mensal'
quarterly_data_df['Fonte'] = 'Quaternal'
annual_data_df['Fonte'] = 'Anual'

monthly_data_df = monthly_data_df[monthly_data_df['baseCalculo'] == 0]
annual_data_df = annual_data_df[annual_data_df['baseCalculo'] == 0]

expec_data = pd.concat([monthly_data_df, quarterly_data_df, annual_data_df])

expec_data.loc[expec_data[expec_data['Fonte'] == 'Mensal']['Indicador'].isin(indicadores[indicadores['Conjunto'] == 'Inflação']['IndiNome'].values).values,'Media'] = ((((expec_data[expec_data['Fonte'] == 'Mensal']['Media']/100)+1)**12)-1)*100
expec_data.loc[expec_data['Fonte'] == 'Anual','DataReferencia'] = '31/12/'+expec_data[expec_data['Fonte'] == 'Anual']['DataReferencia']

expec_data = expec_data.reset_index(drop=True)

expec_data['IndiNome'] = expec_data['Indicador'] 
expec_data.loc[expec_data['IndicadorDetalhe'].notnull(),'IndiNome'] = expec_data['Indicador'] + ' - ' + expec_data['IndicadorDetalhe']

expec_data['DataReferencia'] = pd.to_datetime(expec_data['DataReferencia'])

expec_data.drop(['Indicador','IndicadorDetalhe','Fonte','baseCalculo'], axis=1, inplace=True)

expec_data = expec_data.reset_index(drop=True)


# TOP 5 DATA limpeza e preparo de dados 
top_5_anual_df['Fonte'] = 'Anual'
top_5_monthly_df['Fonte'] = 'Mensal'

top_5_data = pd.concat([top_5_anual_df, top_5_monthly_df])

top_5_data.loc[top_5_data[top_5_data['Fonte'] == 'Mensal']['Indicador'].isin(indicadores[indicadores['Conjunto'] == 'Inflação']['IndiNome'].values),'Media'] = ((((top_5_data[top_5_data['Fonte'] == 'Mensal']['Media']/100)+1)**12)-1)*100
top_5_data.loc[top_5_data['Fonte'] == 'Anual','DataReferencia'] = '31/12/'+top_5_data[top_5_data['Fonte'] == 'Anual']['DataReferencia']

top_5_data = top_5_data.reset_index(drop=True)

top_5_data['IndiNome'] = top_5_data['Indicador']

top_5_data['DataReferencia'] = pd.to_datetime(top_5_data['DataReferencia'])

top_5_data.drop(['Indicador','Fonte'], axis=1, inplace=True)

top_5_data = top_5_data.reset_index(drop=True)



indicador = 'IPCA'
data = '2019-05-17'

print(indicadores['Conjunto'].unique())
# print(indicadores[indicadores['Conjunto'] == 'Inflação']['IndiNome'].values)

# print(indicador)
# print(data)

# print('Inflação Doze meses:')
# print(twelve_months_data_df[twelve_months_data_df['Data'] == data]
#             [twelve_months_data_df['IndiNome'] == indicador])

# print('Expectativa data:')
# print(expec_data[expec_data['Data'] == data]
#             [expec_data['IndiNome'] == indicador].sort_values(by=['DataReferencia']))

# print("Top 5 data:")
# print(top_5_data[top_5_data['tipoCalculo'] == 'C'][top_5_data['Data'] == data]
#             [top_5_data['IndiNome'] == indicador].sort_values(by=['DataReferencia']))

# print(twelve_months_data_df.columns)

# print(expec_data[expec_data['Data'] ==
#                                            '2019-06-14'])

# expec_labels_ipca = expec_data[expec_data['Data'] ==
#                                             '2019-06-14'][expec_data['IndiNome'] == 'IPCA'].sort_values(by=['DataReferencia'])['DataReferencia']
print(expec_data[expec_data['Data'] == '2019-06-12'][expec_data['IndiNome'] == 'IPA-DI'].sort_values(by=['DataReferencia'])['Media'])
print(expec_data[expec_data['Data'] == '2019-06-12'][expec_data['IndiNome']
                                                     == 'IPA-DI'].sort_values(by=['DataReferencia'])['DataReferencia'])

# expec_labels_igp_di = expec_data[expec_data['Data'] ==
#                                               '2019-06-14'][expec_data['IndiNome'] == 'IGP-DI'].sort_values(by=['DataReferencia'])['DataReferencia']
# expec_values_igp_di = expec_data[expec_data['Data'] ==
#                                               '2019-06-14'][expec_data['IndiNome'] == 'IGP-DI'].sort_values(by=['DataReferencia'])['Media']
# print(expec_data[expec_data['Data'] =='2019-06-14'][expec_data['IndiNome'] == 'IPCA'].sort_values(by=['DataReferencia'])['DataReferencia'print(twelve_months_data_df[twelve_months_data_df['IndiNome'] == 'IGP-DI'].sort_values(by=['Data'])['Media'])
