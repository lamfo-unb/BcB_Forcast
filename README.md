# Projeto BcB_Forcast
## Objetivo:
Desenvolver Dashboard com analise de informações sobre expectativas do mercado e economia com dados vindos da API do Banco Central do Brasil.

## Dados & links:
### Informações Mensais:
- Keys: [ Indicador']
    - Inflação: 'IGP-DI','IGP-M','INPC','IPA-DI','IPA-M','IPC-FIPE','IPCA','IPCA-15'
    - Indicadores: 'Meta para taxa over-selic', 'Produção industrial','Taxa de câmbio'
- Link: https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/ExpectativaMercadoMensais?$top=1000&$orderby=Data%20desc&$format=json&$select=Indicador,Data,DataReferencia,Media,Mediana,Minimo,Maximo,numeroRespondentes


### Informações Trimestrais: 
- Keys:['Indicador']
    - 'PIB Total', 'PIB Industrial', 'PIB Serviços', 'PIB Agropecuária'
- Link: https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/ExpectativasMercadoTrimestrais?$top=100&$orderby=Data%20desc&$format=json&$select=Indicador,Data,DataReferencia,Media,Mediana,Minimo,Maximo,numeroRespondentes

### Informações para 12 meses de rolagem:
- Keys:[ Indicador']
    - Inflação: 'IGP-DI','IGP-M','INPC','IPA-DI','IPA-M','IPC-FIPE','IPCA','IPCA-15'
- Link:
https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/ExpectativasMercadoInflacao12Meses?$top=100&$orderby=Data%20desc&$format=json&$select=Indicador,Data,Suavizada,Media,Mediana,Minimo,Maximo,numeroRespondentes

### Informações Anuais: 
- Keys:[ Indicador', 'IndicadorDetalhe']
    - [Balança Comercial','Saldo'], [Balança Comercial','Exportações'], [Balança Comercial','Importações']
    - [Balança Comercial','Importações'], [ 'Balanço de Pagamentos','Conta corrente'], [ 'Balanço de Pagamentos','Investimento direto no país']
    - ['Fiscal','Resultado Primário'], ['Fiscal','Resultado Nominal'], ['Fiscal','Dívida líquida do setor público']
    - [ 'IGP-DI', None], [ 'IGP-M', None], [ 'INPC', None], [ 'IPA-DI', None], [ 'IPA-M', None], [ 'IPC-FIPE', None], [ 'IPCA', None], [ 'IPCA-15', None]
    - [ 'PIB Agropecuária', None], [ 'PIB Industrial', None], [ 'PIB Serviços', None], [ 'PIB Total', None]
    - [ 'Meta para taxa over-selic',‘Fim do ano’]
    - [ 'Preços administrados por contrato e monitorados', None]
    - [ 'Produção industrial', None]
    - [ 'Taxa de câmbio',‘Fim do ano’]

- Link:
https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/ExpectativasMercadoAnuais?$top=1000&$orderby=Data%20desc&$format=json&$select=Indicador,IndicadorDetalhe,Data,DataReferencia,Media,Mediana,Minimo,Maximo,numeroRespondentes

## Ferramentas:
![](keys_resume.png)
 
Dentro da key “value” temos a lista de observações que correspondem as expectativas do mercado para um indicador em um dia, com referencia em uma data futura.

A ideia é usar o Dash do Python para criar gráficos interativos com as informações.

## Etapas:

### Fase 1 (Organização dos dados ):
Coleta e estruturação dos dados da API.

### Fase 2 (Gráficos): Replicar o relatório Focus de forma dinâmica:
https://www.bcb.gov.br/pec/GCI/PORT/readout/R20180928.pdf

### Fase 3 (Gráficos):
- Mudanças na expectativa: 
Com um indicador selecionado 
Conjunto de datas futuras fixado.
Comparar como a expectativa tem mudado para uma data expecifica.
- Expectativa para datas futuras

Outras analises serão construídas apartir daqui.

	


