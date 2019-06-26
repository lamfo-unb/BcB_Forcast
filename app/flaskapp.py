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

    expec_labels = json_collect.expec_data[json_collect.expec_data['Data'] ==
                                           expec_data].sort_values(by=['DataReferencia'])['DataReferencia'].dt.strftime("%d/%m/%Y").unique()
    expec_legend_ipca = 'IPCA'
    expec_values_ipca = json_collect.expec_data[json_collect.expec_data['Data'] ==
                                                expec_data][json_collect.expec_data['IndiNome'] == 'IPCA'].sort_values(by=['DataReferencia'])['Media']
    expec_labels_ipca = json_collect.expec_data[json_collect.expec_data['Data'] ==
                                                expec_data][json_collect.expec_data['IndiNome'] == 'IPCA'].sort_values(by=['DataReferencia'])['DataReferencia'].dt.strftime("%d/%m/%Y")


    expec_legend_igp_m = 'IGP-M'
    expec_values_igp_m = json_collect.expec_data[json_collect.expec_data['Data'] ==
                                                expec_data][json_collect.expec_data['IndiNome'] == 'IGP-M'].sort_values(by=['DataReferencia'])['Media']
    expec_labels_igp_m = json_collect.expec_data[json_collect.expec_data['Data'] ==
                                                 expec_data][json_collect.expec_data['IndiNome'] == 'IGP-M'].sort_values(by=['DataReferencia'])['DataReferencia'].dt.strftime("%d/%m/%Y")


    expec_legend_inpc = 'INPC'
    expec_values_inpc = json_collect.expec_data[json_collect.expec_data['Data'] ==
                                                expec_data][json_collect.expec_data['IndiNome'] == 'INPC'].sort_values(by=['DataReferencia'])['Media']

    expec_legend_ipa_di = 'IPA-DI'
    expec_values_ipa_di = json_collect.expec_data[json_collect.expec_data['Data'] ==
                                                expec_data][json_collect.expec_data['IndiNome'] == 'IPA-DI'].sort_values(by=['DataReferencia'])['Media']

    expec_legend_ipa_m = 'IPA-M'
    expec_values_ipa_m = json_collect.expec_data[json_collect.expec_data['Data'] ==
                                                expec_data][json_collect.expec_data['IndiNome'] == 'IPA-M'].sort_values(by=['DataReferencia'])['Media']

    expec_legend_ipca_15 = 'IPCA-15'
    expec_values_ipca_15 = json_collect.expec_data[json_collect.expec_data['Data'] ==
                                                expec_data][json_collect.expec_data['IndiNome'] == 'IPCA-15'].sort_values(by=['DataReferencia'])['Media']

    expec_legend_pacm = 'Preços administrados por contrato e monitorados'
    expec_values_pacm = json_collect.expec_data[json_collect.expec_data['Data'] ==
                                                expec_data][json_collect.expec_data['IndiNome'] == 'Preços administrados por contrato e monitorados'].sort_values(by=['DataReferencia'])['Media']

    expec_legend_igp_di = 'IGP-DI'
    expec_values_igp_di = json_collect.expec_data[json_collect.expec_data['Data'] == 
                                                  expec_data][json_collect.expec_data['IndiNome'] == 'IGP-DI'].sort_values(by=['DataReferencia'])['Media']
    
    # top_5 dataset values:
    top_5_data_values = json_collect.top_5_data["Data"].sort_values().unique()

    top_5_data = expec_data

    top_5_legend_ipca = 'IPCA'
    top_5_labels_ipca = json_collect.top_5_data[json_collect.top_5_data['Data'] ==
                                                top_5_data][json_collect.top_5_data['IndiNome'] == 'IPCA'].sort_values(by=['DataReferencia'])['DataReferencia'].dt.strftime("%d/%m/%Y").unique()
    top_5_values_ipca = json_collect.top_5_data[json_collect.top_5_data['Data'] ==
                                           top_5_data][json_collect.top_5_data['IndiNome'] == 'IPCA'].sort_values(by=['DataReferencia'])['Media']
    
    top_5_legend_igp_m = 'IGP-M'
    top_5_values_igp_m = json_collect.top_5_data[json_collect.top_5_data['Data'] ==
                                                 top_5_data][json_collect.top_5_data['IndiNome'] == 'IGP-M'].sort_values(by=['DataReferencia'])['Media']
    
    # twelve_months dataset values:
    twelve_months_data_values = json_collect.twelve_months_data_df["Data"].sort_values().unique()

    twelve_months_data = expec_data

    twelve_months_labels = json_collect.twelve_months_data_df['Data'].sort_values().unique()
    twelve_months_legend_ipca = 'IPCA'
    twelve_months_values_ipca = json_collect.twelve_months_data_df[json_collect.twelve_months_data_df['IndiNome'] == 'IPCA'].sort_values(by=['Data'])['Media']
    
    twelve_months_legend_igp_di = 'IGP-DI'
    twelve_months_values_igp_di = json_collect.twelve_months_data_df[json_collect.twelve_months_data_df['IndiNome'] == 'IGP-DI'].sort_values(by=['Data'])['Media']
    
    twelve_months_legend_igp_m = 'IGP-M'
    twelve_months_values_igp_m = json_collect.twelve_months_data_df[json_collect.twelve_months_data_df['IndiNome'] == 'IGP-M'].sort_values(by=['Data'])['Media']

    twelve_months_legend_inpc = 'INPC'
    twelve_months_values_inpc = json_collect.twelve_months_data_df[json_collect.twelve_months_data_df['IndiNome'] == 'INPC'].sort_values(by=['Data'])['Media']
    
    twelve_months_legend_ipa_di = 'IPA-DI'
    twelve_months_values_ipa_di = json_collect.twelve_months_data_df[json_collect.twelve_months_data_df['IndiNome'] == 'IPA-DI'].sort_values(by=['Data'])['Media']

    twelve_months_legend_ipa_m = 'IPA-M'
    twelve_months_values_ipa_m = json_collect.twelve_months_data_df[json_collect.twelve_months_data_df['IndiNome'] == 'IPA-M'].sort_values(by=['Data'])['Media']

    twelve_months_legend_ipc_fipe = 'IPC-Fipe'
    twelve_months_values_ipc_fipe = json_collect.twelve_months_data_df[json_collect.twelve_months_data_df['IndiNome'] == 'IPC-Fipe'].sort_values(by=['Data'])['Media']

    twelve_months_legend_ipca_15 = 'IPCA-15'
    twelve_months_values_ipca_15 = json_collect.twelve_months_data_df[json_collect.twelve_months_data_df['IndiNome'] == 'IPCA-15'].sort_values(by=['Data'])['Media']
    
    return render_template('plain_page.html',
                        expec_legend_ipca=expec_legend_ipca, expec_labels=expec_labels, expec_values_ipca=zip(expec_labels_ipca,expec_values_ipca),
                        expec_legend_igp_di=expec_legend_igp_di, expec_values_igp_di=expec_values_igp_di,
                        expec_legend_igp_m=expec_legend_igp_m, expec_values_igp_m=zip(expec_labels_igp_m, expec_values_igp_m),
                        expec_legend_inpc=expec_legend_inpc, expec_values_inpc=expec_values_inpc,
                        expec_legend_ipa_di=expec_legend_ipa_di, expec_values_ipa_di=expec_values_ipa_di,
                        expec_legend_ipa_m=expec_legend_ipa_m, expec_values_ipa_m=expec_values_ipa_m,
                        expec_legend_ipca_15=expec_legend_ipca_15, expec_values_ipca_15=expec_values_ipca_15,
                        expec_legend_pacm=expec_legend_pacm, expec_values_pacm=expec_values_pacm,
                        top_5_legend_ipca=top_5_legend_ipca, top_5_labels_ipca=top_5_labels_ipca, top_5_values_ipca=top_5_values_ipca,
                        top_5_legend_igp_m=top_5_legend_igp_m, top_5_values_igp_m=top_5_values_igp_m,
                        twelve_months_legend_ipca=twelve_months_legend_ipca,twelve_months_labels=twelve_months_labels, twelve_months_values_ipca=twelve_months_values_ipca,
                        twelve_months_legend_igp_di=twelve_months_legend_igp_di, twelve_months_values_igp_di=twelve_months_values_igp_di,
                        twelve_months_legend_igp_m=twelve_months_legend_igp_m, twelve_months_values_igp_m=twelve_months_values_igp_m,
                        twelve_months_legend_inpc=twelve_months_legend_inpc, twelve_months_values_inpc=twelve_months_values_inpc,
                        twelve_months_legend_ipa_di=twelve_months_legend_ipa_di, twelve_months_values_ipa_di=twelve_months_values_ipa_di,
                        twelve_months_legend_ipa_m=twelve_months_legend_ipa_m, twelve_months_values_ipa_m=twelve_months_values_ipa_m,
                        twelve_months_legend_ipc_fipe=twelve_months_legend_ipc_fipe, twelve_months_values_ipc_fipe=twelve_months_values_ipc_fipe,
                        twelve_months_legend_ipca_15=twelve_months_legend_ipca_15, twelve_months_values_ipca_15=twelve_months_values_ipca_15,
                        expec_data_values=expec_data_values, top_5_data_values=top_5_data_values, twelve_months_data_values=twelve_months_data_values,
                           expec_data=expec_data)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', titulo="Home")


app.run(debug=True)

# expec_data[expec_data['IndiNome'].isin(
#     indicadores[indicadores['Conjunto'] == 'Inflação']['IndiNome'].values).values][expec_data['Data'] == '2019-06-14']
