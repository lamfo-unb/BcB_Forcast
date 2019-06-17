from flask import Flask
from flask import render_template
import json_collect 

app = Flask(__name__)

@app.route('/')
def home():
    legend = 'IPCA'
    labels = json_collect.expec_data[json_collect.expec_data['Data'] ==
                                     '2019-06-14'][json_collect.expec_data['IndiNome'] == 'IPCA'].sort_values(by=['DataReferencia'])['DataReferencia']
    values = json_collect.expec_data[json_collect.expec_data['Data'] ==
                                     '2019-06-14'][json_collect.expec_data['IndiNome'] == 'IPCA'].sort_values(by=['DataReferencia'])['Media']
    return render_template('plain_page.html', values=values, labels=labels, legend=legend)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', titulo="Home")


app.run(debug=True)

# expec_data[expec_data['IndiNome'].isin(
#     indicadores[indicadores['Conjunto'] == 'Inflação']['IndiNome'].values).values][expec_data['Data'] == '2019-06-14']
