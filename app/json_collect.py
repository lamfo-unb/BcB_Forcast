import urllib.request, json
import pandas as pd
from pandas.io.json import json_normalize

# coleta dados api
with urllib.request.urlopen("https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/ExpectativasMercadoInflacao12Meses?$top=100&$orderby=Data%20desc&$format=json&$select=Indicador,Data,Suavizada,baseCalculo,Media,Mediana") as url:
    twelve_months_data = json.loads(url.read().decode())
    
with urllib.request.urlopen("https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/ExpectativaMercadoMensais?$top=1000&$orderby=Data%20desc&$format=json&$select=Indicador,Data,DataReferencia,baseCalculo,Media,Mediana") as url:
    monthly_data = json.loads(url.read().decode())

with urllib.request.urlopen("https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/ExpectativasMercadoTrimestrais?$top=100&$orderby=Data%20desc&$format=json&$select=Indicador,Data,DataReferencia,Media,Mediana") as url:
    quarterly_data = json.loads(url.read().decode())

with urllib.request.urlopen("https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/ExpectativasMercadoAnuais?$top=1000&$orderby=Data%20desc&$format=json&$select=Indicador,IndicadorDetalhe,Data,DataReferencia,baseCalculo,Media,Mediana") as url:
    annual_data = json.loads(url.read().decode())

with urllib.request.urlopen("https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/ExpectativasMercadoTop5Anuais?$top=1000&$orderby=Data%20desc&$format=json&$select=Indicador,Data,tipoCalculo,DataReferencia,Media,Mediana") as url:
    top_5_anual_data = json.loads(url.read().decode())

with urllib.request.urlopen("https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/ExpectativasMercadoTop5Mensais?$top=1000&$orderby=Data%20desc&$format=json&$select=Indicador,Data,tipoCalculo,DataReferencia,Media,Mediana") as url:
    top_5_monthly_data = json.loads(url.read().decode())

indicadoresInflacao = {'IGP-DI','IGP-M','INPC','IPA-DI','IPA-M','IPCA','IPC-Fipe','IPCA-15','Preços administrados por contrato e monitorados'}
indicadoresPIB = {'PIB Agropecuária', 'PIB Industrial', 'PIB Serviços', 'PIB Total', 'Produção industrial'}
indicadoresMacro = {'Meta para taxa over-selic','Taxa de câmbio'}
indicadoresTransacionais = [{'Indicadores': 'Balança Comercial', 'IndicadorDetalhe': 'Saldo'},
{'Indicadores': 'Balança Comercial', 'IndicadorDetalhe': 'Exportações'},
{'Indicadores': 'Balança Comercial', 'IndicadorDetalhe': 'Importações'},
{'Indicadores': 'Balança Comercial', 'IndicadorDetalhe': 'Importações'}]
indicadoresFiscais = [{'Indicadores': 'Balanço de Pagamentos', 'IndicadorDetalhe': 'Conta corrente'},
{'Indicadores': 'Balanço de Pagamentos', 'IndicadorDetalhe': 'Investimento direto no país'},
{'Indicadores': 'Fiscal', 'IndicadorDetalhe': 'Resultado Primário'},
{'Indicadores': 'Fiscal', 'IndicadorDetalhe': 'Resultado Nominal'},
{'Indicadores': 'Fiscal', 'IndicadorDetalhe': 'Dívida líquida do setor público'}]
{'Conjunto': 'Fiscais', 'indicadores': {'Meta para taxa over-selic','Taxa de câmbio'}}


indicadores = pd.DataFrame.from_dict(list([
  {'Conjunto': 'Inflação', 'IndiNome':'IGP-DI', 'Indicador': 'IGP-DI'},
  {'Conjunto': 'Inflação', 'IndiNome':'IGP-M', 'Indicador': 'IGP-M'},
  {'Conjunto': 'Inflação', 'IndiNome':'INPC', 'Indicador': 'INPC'},
  {'Conjunto': 'Inflação', 'IndiNome':'IPA-DI', 'Indicador': 'IPA-DI'},
  {'Conjunto': 'Inflação', 'IndiNome':'IPA-M', 'Indicador': 'IPA-M'},
  {'Conjunto': 'Inflação', 'IndiNome':'IPCA', 'Indicador': 'IPCA'},
  {'Conjunto': 'Inflação', 'IndiNome':'IPC-Fipe', 'Indicador': 'IPC-Fipe'},
  {'Conjunto': 'Inflação', 'IndiNome':'IPCA-15', 'Indicador': 'IPCA-15'},
  {'Conjunto': 'Inflação', 'IndiNome':'Preços administrados por contrato e monitorados', 'Indicador': 'Preços administrados por contrato e monitorados'},
  {'Conjunto': 'PIB', 'IndiNome':'PIB Agropecuária','Indicador': 'PIB Agropecuária'}, 
  {'Conjunto': 'PIB', 'IndiNome':'PIB Industrial','Indicador': 'PIB Industrial'}, 
  {'Conjunto': 'PIB', 'IndiNome':'PIB Serviços','Indicador': 'PIB Serviços'}, 
  {'Conjunto': 'PIB', 'IndiNome':'PIB Total','Indicador': 'PIB Total'}, 
  {'Conjunto': 'PIB', 'IndiNome':'Produção industrial','Indicador': 'Produção industrial'},
  {'Conjunto': 'Macro','IndiNome':'Meta para taxa over-selic', 'Indicador': 'Meta para taxa over-selic'},
  {'Conjunto': 'Macro','IndiNome':'Taxa de câmbio', 'Indicador': 'Taxa de câmbio'},
  {'Conjunto': 'Transacionais', 'IndiNome':'Balança Comercial - Saldo','Indicador': 'Balança Comercial', 'IndicadorDetalhe': 'Saldo'},
  {'Conjunto': 'Transacionais', 'IndiNome':'Balança Comercial - Exportações','Indicador': 'Balança Comercial', 'IndicadorDetalhe': 'Exportações'},
  {'Conjunto': 'Transacionais', 'IndiNome':'Balança Comercial - Importações','Indicador': 'Balança Comercial', 'IndicadorDetalhe': 'Importações'},
  {'Conjunto': 'Transacionais', 'IndiNome':'Balança Comercial - Importações','Indicador': 'Balança Comercial', 'IndicadorDetalhe': 'Importações'},
  {'Conjunto': 'Fiscais', 'IndiNome':'Balanço de Pagamentos - Conta corrente','Indicador': 'Balanço de Pagamentos', 'IndicadorDetalhe': 'Conta corrente'},
  {'Conjunto': 'Fiscais', 'IndiNome':'Balanço de Pagamentos - Investimento direto no país','Indicador': 'Balanço de Pagamentos', 'IndicadorDetalhe': 'Investimento direto no país'},
  {'Conjunto': 'Fiscais', 'IndiNome':'Fiscal - Resultado Primário','Indicador': 'Fiscal', 'IndicadorDetalhe': 'Resultado Primário'},
  {'Conjunto': 'Fiscais', 'IndiNome':'Fiscal - Resultado Nominal','Indicador': 'Fiscal', 'IndicadorDetalhe': 'Resultado Nominal'},
  {'Conjunto': 'Fiscais', 'IndiNome':'Fiscal - Dívida líquida do setor público','Indicador': 'Fiscal', 'IndicadorDetalhe': 'Dívida líquida do setor público'}]), orient='columns')

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






# DATA EXPECTATIVA MERCADO limpeza e preparo de dados 
monthly_data_df['Fonte'] = 'Mensal'
quarterly_data_df['Fonte'] = 'Quaternal'
annual_data_df['Fonte'] = 'Anual'

expec_data = pd.concat([monthly_data_df, quarterly_data_df, annual_data_df])

expec_data.loc[expec_data[expec_data['Fonte'] == 'Mensal']['Indicador'].isin(indicadores[indicadores['Conjunto'] == 'Inflação']['IndiNome'].values),'Media'] = ((((expec_data[expec_data['Fonte'] == 'Mensal']['Media']/100)+1)**12)-1)*100
expec_data.loc[expec_data['Fonte'] == 'Anual','DataReferencia'] = '31/12/'+expec_data[expec_data['Fonte'] == 'Anual']['DataReferencia']

expec_data['DataReferencia'] = pd.to_datetime(expec_data['DataReferencia'])

expec_data = expec_data.reset_index(drop=True)

# TOP 5 DATA limpeza e preparo de dados 
top_5_anual_df['Fonte'] = 'Anual'
top_5_monthly_df['Fonte'] = 'Mensal'

top_5_data = pd.concat([top_5_anual_df, top_5_monthly_df])

top_5_data.loc[top_5_data[top_5_data['Fonte'] == 'Mensal']['Indicador'].isin(indicadores[indicadores['Conjunto'] == 'Inflação']['IndiNome'].values),'Media'] = ((((top_5_data[top_5_data['Fonte'] == 'Mensal']['Media']/100)+1)**12)-1)*100
top_5_data.loc[top_5_data['Fonte'] == 'Anual','DataReferencia'] = '31/12/'+top_5_data[top_5_data['Fonte'] == 'Anual']['DataReferencia']

top_5_data['DataReferencia'] = pd.to_datetime(top_5_data['DataReferencia'])

top_5_data = top_5_data.reset_index(drop=True)

indicador = 'IPCA'
data = '2019-05-10'

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

# print('Top 5:')
# print('Anual:')
# print(top_5_anual_df[top_5_anual_df['Indicador']
#                             == indicador][top_5_anual_df['Data'] == '2019-04-26'][top_5_monthly_df['tipoCalculo'] == 'C'].sort_values(by=['tipoCalculo','DataReferencia']))
# print('Mensal:')
# print(top_5_monthly_df[top_5_monthly_df['Indicador'] 
#                             == indicador][top_5_monthly_df['Data'] == '2019-04-26'][top_5_monthly_df['tipoCalculo'] == 'C'].sort_values(by=['DataReferencia']))

print('Inflação Doze meses:')
print(twelve_months_data_df[twelve_months_data_df['Data'] == data]
            [twelve_months_data_df['Indicador'] == indicador])

print('Expectativa data:')
print(expec_data[expec_data['Data'] == data]
            [expec_data['Indicador'] == indicador].sort_values(by=['DataReferencia']))

print("Top 5 data:")
print(top_5_data[top_5_data['tipoCalculo'] == 'C'][top_5_data['Data'] == data]
            [top_5_data['Indicador'] == indicador].sort_values(by=['DataReferencia']))
    


print(indicadores['Conjunto'].unique())
print(indicadores[indicadores['Conjunto'] == 'Inflação']['IndiNome'].values)

indicadores[indicadores['IndiNome'] == 'IGP-DI'][['Indicador','IndicadorDetalhe']]

indicadores[indicadores['IndiNome'] == 'Balanço de Pagamentos - Conta corrente'][['Indicador','IndicadorDetalhe']]


keys = indicadores[indicadores['IndiNome'] == 'Balanço de Pagamentos - Conta corrente'][['Indicador','IndicadorDetalhe']].keys().tolist()

for i in keys:
    indi = indicadores[indicadores['IndiNome'] == 'Balanço de Pagamentos - Conta corrente'][i].values[0]
    verdade = expec_data[i] == indi
    print(expec_data[expec_data['baseCalculo'] == 0][expec_data['Data'] == data]
            [expec_data[i] == indi].sort_values(by=['DataReferencia']))


# monthly_data_df['DataReferencia'] = pd.to_datetime(
#     monthly_data_df['DataReferencia'], format='%m/%Y')
# quarterly_data_df['DataReferencia'] = pd.to_datetime(
#     quarterly_data_df['DataReferencia'], format='%m/%Y')
# twelve_months_data_df['DataReferencia'] = pd.to_datetime(
#     twelve_months_data_df['DataReferencia'], format='%m/%Y')
# annual_data_df['DataReferencia'] = pd.to_datetime(
#     annual_data_df['DataReferencia'], format='%m/%Y')
