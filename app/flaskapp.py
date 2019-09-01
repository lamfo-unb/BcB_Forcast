from flask import Flask, render_template, request, jsonify
import json_collect 
import pandas as pd

app = Flask(__name__)


@app.route('/')
def home():
	color = ['#d32f2f', 'rgba(75,192,192,1)', '#7b1fa2', '#303f9f', '#0288d1', '#fbc02d', '#f57c00', '#616161']
	# expec dataset values:
	DataSelect = []
	DataSelect.extend(json_collect.expec_data["Data"].sort_values().unique())
	DataSelect.extend(json_collect.top_5_data["Data"].sort_values().unique())
	DataSelect.extend(json_collect.twelve_months_data_df["Data"].sort_values().unique())
	DataSelect = list(dict.fromkeys(DataSelect))
	DataSelect.sort()
	
	ConjIndicadores = json_collect.indicadores['Conjunto'].unique()

	DataSelecionada = DataSelect[-1] if request.args.get('DataSelecionada') == None else request.args.get('DataSelecionada')
	ConjSelecionado = 'Inflação' if request.args.get('ConjSelecionado') == None else request.args.get('ConjSelecionado')

	indicadores = json_collect.indicadores[json_collect.indicadores['Conjunto'] == ConjSelecionado]['IndiNome'].unique()

	expec_dados_t = []
	top5_dados_t = []
	E12_dados_t = []
	indicadores_list = []
	ExpecGraf = False
	ExpecTop5Graf = False
	E12Graf = False

	i=0
	for indi in indicadores:
		indicadores_list.append(i) 
		# EXPECTATIVA DO MERCADO
		indi_expec_labels = json_collect.expec_data[json_collect.expec_data['Data'] == DataSelecionada][json_collect.expec_data['IndiNome'] == indi].sort_values(by=['DataReferencia'])['DataReferencia'].dt.strftime("%d/%m/%Y")
		indi_expec_values = json_collect.expec_data[json_collect.expec_data['Data'] == DataSelecionada][json_collect.expec_data['IndiNome'] == indi].sort_values(by=['DataReferencia'])['Media']
		expec_dados_t.extend([{'label':indi, 'data': list(zip(indi_expec_labels,indi_expec_values))}])

		if not indi_expec_values.empty:
			ExpecGraf = True

		# EXPECTATIVA TOP_5
		indi_top5_labels = json_collect.top_5_data[json_collect.top_5_data['Data'] == DataSelecionada][json_collect.top_5_data['IndiNome'] == indi].sort_values(by=['DataReferencia'])['DataReferencia'].dt.strftime("%d/%m/%Y")
		indi_top5_values = json_collect.top_5_data[json_collect.top_5_data['Data'] == DataSelecionada][json_collect.top_5_data['IndiNome'] == indi].sort_values(by=['DataReferencia'])['Media']
		top5_dados_t.extend([{'label':indi, 'data': list(zip(indi_top5_labels,indi_top5_values))}])

		if not indi_top5_values.empty:
			ExpecTop5Graf = True

		# EXPECTATIVA 12 MESES
		indi_E12_labels = pd.to_datetime(json_collect.twelve_months_data_df[json_collect.twelve_months_data_df['IndiNome'] == indi].sort_values(by=['Data'])['Data']).dt.strftime("%d/%m/%Y")
		indi_E12_values = json_collect.twelve_months_data_df[json_collect.twelve_months_data_df['IndiNome'] == indi].sort_values(by=['Data'])['Media']
		E12_dados_t.extend([{'label':indi, 'data': list(zip(indi_E12_labels,indi_E12_values))}])

		if not indi_E12_values.empty:
			E12Graf = True

		i = i +1


	return render_template('comparativo.html', DataSelect = DataSelect, ConjIndicadores = ConjIndicadores, DataSelecionada = DataSelecionada, ConjSelecionado = ConjSelecionado, color = color, 
						indicadores_list = indicadores_list, expec_dados_t = expec_dados_t, top5_dados_t = top5_dados_t, E12_dados_t = E12_dados_t, 
						ExpecGraf = ExpecGraf, ExpecTop5Graf = ExpecTop5Graf, E12Graf = E12Graf)


@app.route('/evolucao', methods=['POST','GET'])
def evolucao():
	color = ['#d32f2f', 'rgba(75,192,192,1)', '#7b1fa2', '#303f9f', '#0288d1', '#fbc02d', '#f57c00', '#616161']

	ConjSelecionado = 'Inflação' if request.form.get('ConjSelecionado') == None else request.form.get('ConjSelecionado')
	IndSelecionado = 'IPCA' if request.form.get('IndSelecionado') == None else request.form.get('IndSelecionado')
	
	DataSelect = []
	DataSelect.extend(json_collect.expec_data[json_collect.expec_data['IndiNome'] == IndSelecionado]["Data"].sort_values().unique())
	DataSelect.extend(json_collect.top_5_data[json_collect.top_5_data['IndiNome'] == IndSelecionado]["Data"].sort_values().unique())
	DataSelect = list(dict.fromkeys(DataSelect))
	DataSelect.sort()
	
	DataSelecionada = DataSelect[-1] if request.form.getlist('DataSelecionada') == None else request.form.getlist('DataSelecionada')
	
	ConjIndicadores = json_collect.indicadores['Conjunto'].unique()

	Indicadores = json_collect.indicadores[json_collect.indicadores['Conjunto'] == ConjSelecionado]['IndiNome'].unique()

	expec_dados_t = []
	top5_dados_t = []
	data_list = []
	ExpecGraf = False
	ExpecTop5Graf = False

	i=0
	for DtSel in DataSelecionada:
		data_list.append(i) 
		# EXPECTATIVA DO MERCADO
		indi_expec_labels = json_collect.expec_data[json_collect.expec_data['Data'] == DtSel][json_collect.expec_data['IndiNome'] == IndSelecionado].sort_values(by=['DataReferencia'])['DataReferencia'].dt.strftime("%d/%m/%Y")
		indi_expec_values = json_collect.expec_data[json_collect.expec_data['Data'] == DtSel][json_collect.expec_data['IndiNome'] == IndSelecionado].sort_values(by=['DataReferencia'])['Media']
		expec_dados_t.extend([{'label':DtSel, 'data': list(zip(indi_expec_labels,indi_expec_values))}])

		if not indi_expec_values.empty:
			ExpecGraf = True

		# EXPECTATIVA TOP_5
		indi_top5_labels = json_collect.top_5_data[json_collect.top_5_data['Data'] == DtSel][json_collect.top_5_data['IndiNome'] == IndSelecionado].sort_values(by=['DataReferencia'])['DataReferencia'].dt.strftime("%d/%m/%Y")
		indi_top5_values = json_collect.top_5_data[json_collect.top_5_data['Data'] == DtSel][json_collect.top_5_data['IndiNome'] == IndSelecionado].sort_values(by=['DataReferencia'])['Media']
		top5_dados_t.extend([{'label':DtSel, 'data': list(zip(indi_top5_labels,indi_top5_values))}])

		if not indi_top5_values.empty:
			ExpecTop5Graf = True

		i = i +1
	return render_template('evolucao.html', DataSelect = DataSelect, ConjIndicadores = ConjIndicadores, Indicadores = Indicadores,
					DataSelecionada = DataSelecionada, ConjSelecionado = ConjSelecionado, IndSelecionado = IndSelecionado,
					data_list = data_list, color = color,
					ExpecGraf = ExpecGraf, expec_dados_t = expec_dados_t,
					ExpecTop5Graf = ExpecTop5Graf, top5_dados_t = top5_dados_t)


	
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', titulo="Home")


@app.route('/GetIndicadores', methods=['POST'])
def GetIndicadores():
	ConjSelecionado = 'Inflação' if request.form.get('ConjSelecionado') == None else request.form.get('ConjSelecionado')
	Indicadores = json_collect.indicadores[json_collect.indicadores['Conjunto'] == ConjSelecionado]['IndiNome'].unique()
	Indicadores=pd.Series(Indicadores).to_json(orient='values')

	return(Indicadores)

@app.route('/GetDatas', methods=['POST'])
def GetDatas():
	IndSelecionado = 'IPCA' if request.form.get('IndSelecionado') == None else request.form.get('IndSelecionado')
	DataSelect = []
	DataSelect.extend(json_collect.expec_data[json_collect.expec_data['IndiNome'] == IndSelecionado]["Data"].sort_values().unique())
	DataSelect.extend(json_collect.top_5_data[json_collect.top_5_data['IndiNome'] == IndSelecionado]["Data"].sort_values().unique())
	DataSelect = list(dict.fromkeys(DataSelect))
	DataSelect.sort()
	DataSelect=pd.Series(DataSelect).to_json(orient='values')
	
	return(DataSelect)

app.run(debug=True)

# expec_data[expec_data['IndiNome'].isin(
#     indicadores[indicadores['Conjunto'] == 'Inflação']['IndiNome'].values).values][expec_data['Data'] == '2019-06-14']
