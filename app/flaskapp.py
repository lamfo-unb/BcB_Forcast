from flask import Flask
from flask import render_template
import json_collect 
from flask import request

app = Flask(__name__)

@app.route('/')
def home():
	# expec dataset values:
	expec_data_values = json_collect.expec_data["Data"].sort_values().unique()

	expec_data = request.args.get('expec_data')
	top_5_data = expec_data

	indicador_selecionado = 'Inflação'

	color = ['#d32f2f', 'rgba(75,192,192,1)', '#7b1fa2', '#303f9f', '#0288d1', '#fbc02d', '#f57c00', '#616161']

	indicadores = json_collect.indicadores[json_collect.indicadores['Conjunto'] == indicador_selecionado]['IndiNome'].unique()

	expec_dados_t = []
	top5_dados_t = []
	E12_dados_t = []
	indicadores_list = []
	i=0
	for indi in indicadores:
		indicadores_list.append(i) 
		# EXPECTATIVA DO MERCADO
		indi_expec_labels = json_collect.expec_data[json_collect.expec_data['Data'] == expec_data][json_collect.expec_data['IndiNome'] == indi].sort_values(by=['DataReferencia'])['DataReferencia'].dt.strftime("%d/%m/%Y")
		indi_expec_values = json_collect.expec_data[json_collect.expec_data['Data'] == expec_data][json_collect.expec_data['IndiNome'] == indi].sort_values(by=['DataReferencia'])['Media']
		expec_dados_t.extend([{'label':indi, 'data': list(zip(indi_expec_labels,indi_expec_values))}])

		# EXPECTATIVA TOP_5
		indi_top5_labels = json_collect.top_5_data[json_collect.top_5_data['Data'] == top_5_data][json_collect.top_5_data['IndiNome'] == indi].sort_values(by=['DataReferencia'])['DataReferencia'].dt.strftime("%d/%m/%Y")
		indi_top5_values = json_collect.top_5_data[json_collect.top_5_data['Data'] == top_5_data][json_collect.top_5_data['IndiNome'] == indi].sort_values(by=['DataReferencia'])['Media']
		top5_dados_t.extend([{'label':indi, 'data': list(zip(indi_top5_labels,indi_top5_values))}])

		# EXPECTATIVA 12 MESES
		indi_E12_labels = json_collect.twelve_months_data_df[json_collect.twelve_months_data_df['IndiNome'] == indi].sort_values(by=['Data'])['Data']
		indi_E12_values = json_collect.twelve_months_data_df[json_collect.twelve_months_data_df['IndiNome'] == indi].sort_values(by=['Data'])['Media']
		E12_dados_t.extend([{'label':indi, 'data': list(zip(indi_E12_labels,indi_E12_values))}])

		i = i +1


	return render_template('plain_page.html', color = color, indicadores_list = indicadores_list, expec_dados_t = expec_dados_t, 
						top5_dados_t = top5_dados_t, E12_dados_t = E12_dados_t, expec_data=expec_data)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', titulo="Home")


app.run(debug=True)

# expec_data[expec_data['IndiNome'].isin(
#     indicadores[indicadores['Conjunto'] == 'Inflação']['IndiNome'].values).values][expec_data['Data'] == '2019-06-14']
